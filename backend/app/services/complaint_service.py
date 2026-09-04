"""
Complaint Lifecycle Management Service.
"""
from datetime import datetime, timedelta
from ..models import db, Complaint, ComplaintHistory, ComplaintCategory, Department, Officer, User
from ..config.constants import ComplaintStatuses, SLAConfig

class ComplaintService:
    @staticmethod
    def create_complaint(citizen_id, title, description, location, zone, category_id=None, priority="MEDIUM"):
        # Auto ticket code
        ticket_number = f"TKT-{datetime.utcnow().strftime('%Y%m%d')}-{db.session.query(Complaint).count() + 1:04d}"
        
        category = ComplaintCategory.query.get(category_id) if category_id else None
        department_id = category.department_id if category else None
        sla_hours = category.sla_hours if category else SLAConfig.DEFAULT_SLA_HOURS.get(priority, 24)
        sla_due_date = datetime.utcnow() + timedelta(hours=sla_hours)

        complaint = Complaint(
            ticket_number=ticket_number,
            citizen_id=citizen_id,
            category_id=category_id,
            department_id=department_id,
            title=title,
            description=description,
            location=location,
            zone=zone,
            priority=priority,
            status=ComplaintStatuses.SUBMITTED,
            sla_due_date=sla_due_date,
        )
        db.session.add(complaint)
        db.session.flush()

        history = ComplaintHistory(
            complaint_id=complaint.id,
            performed_by_user_id=citizen_id,
            previous_status=None,
            new_status=ComplaintStatuses.SUBMITTED,
            remarks="Complaint submitted by citizen.",
        )
        db.session.add(history)
        db.session.commit()
        return complaint

    @staticmethod
    def assign_officer(complaint_id, officer_id, admin_user_id=None, remarks="Assigned to officer"):
        complaint = Complaint.query.get(complaint_id)
        if not complaint:
            return False, "Complaint not found"

        officer = User.query.get(officer_id)
        if not officer or not officer.is_officer():
            return False, "Invalid officer"

        prev_status = complaint.status
        complaint.assigned_officer_id = officer_id
        complaint.status = ComplaintStatuses.ASSIGNED

        history = ComplaintHistory(
            complaint_id=complaint.id,
            performed_by_user_id=admin_user_id or officer_id,
            previous_status=prev_status,
            new_status=ComplaintStatuses.ASSIGNED,
            remarks=remarks,
        )
        db.session.add(history)
        db.session.commit()
        return True, "Officer assigned successfully"

    @staticmethod
    def update_status(complaint_id, user_id, new_status, remarks="Status update"):
        complaint = Complaint.query.get(complaint_id)
        if not complaint:
            return False, "Complaint not found"

        if new_status not in ComplaintStatuses.ALL_STATUSES:
            return False, "Invalid status"

        prev_status = complaint.status
        complaint.status = new_status

        if new_status == ComplaintStatuses.RESOLVED:
            complaint.resolved_at = datetime.utcnow()
            if complaint.assigned_officer and complaint.assigned_officer.officer_profile:
                complaint.assigned_officer.officer_profile.resolved_complaints_count += 1

        history = ComplaintHistory(
            complaint_id=complaint.id,
            performed_by_user_id=user_id,
            previous_status=prev_status,
            new_status=new_status,
            remarks=remarks,
        )
        db.session.add(history)
        db.session.commit()
        return True, f"Complaint status updated to {new_status}"

    @staticmethod
    def add_citizen_feedback(complaint_id, citizen_id, rating, comment=None):
        complaint = Complaint.query.filter_by(id=complaint_id, citizen_id=citizen_id).first()
        if not complaint:
            return False, "Complaint not found or unauthorized"

        complaint.feedback_rating = rating
        complaint.feedback_comment = comment
        db.session.commit()
        return True, "Feedback recorded"
