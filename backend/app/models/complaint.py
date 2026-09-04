"""
Complaint Lifecycle Database Models.
"""
from datetime import datetime, timedelta
from .user import db
from ..config.constants import ComplaintStatuses, SLAConfig

class ComplaintCategory(db.Model):
    __tablename__ = "complaint_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    sla_hours = db.Column(db.Integer, default=24)
    priority = db.Column(db.String(20), default="MEDIUM")  # LOW, MEDIUM, HIGH, CRITICAL

    complaints = db.relationship("Complaint", back_populates="category")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department_id": self.department_id,
            "sla_hours": self.sla_hours,
            "priority": self.priority,
        }


class Complaint(db.Model):
    __tablename__ = "complaints"

    id = db.Column(db.Integer, primary_key=True)
    ticket_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    citizen_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey("complaint_categories.id", ondelete="SET NULL"), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id", ondelete="SET NULL"), nullable=True, index=True)
    assigned_officer_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    priority = db.Column(db.String(20), default="MEDIUM", index=True)  # LOW, MEDIUM, HIGH, CRITICAL
    status = db.Column(db.String(30), default=ComplaintStatuses.SUBMITTED, nullable=False, index=True)
    feedback_rating = db.Column(db.Integer, nullable=True)  # 1 to 5 stars
    feedback_comment = db.Column(db.Text, nullable=True)
    sla_due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    resolved_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    citizen = db.relationship("User", foreign_keys=[citizen_id], back_populates="complaints")
    assigned_officer = db.relationship("User", foreign_keys=[assigned_officer_id], back_populates="assigned_complaints")
    category = db.relationship("ComplaintCategory", back_populates="complaints")
    department = db.relationship("Department", back_populates="complaints")
    history = db.relationship("ComplaintHistory", back_populates="complaint", cascade="all, delete-orphan", order_by="ComplaintHistory.created_at.desc()")

    def is_sla_breached(self):
        if self.status in [ComplaintStatuses.RESOLVED, ComplaintStatuses.CLOSED]:
            return False
        return datetime.utcnow() > self.sla_due_date

    def to_dict(self, include_history=False):
        data = {
            "id": self.id,
            "ticket_number": self.ticket_number,
            "citizen_id": self.citizen_id,
            "citizen_name": self.citizen.full_name if self.citizen else "Anonymous",
            "citizen_email": self.citizen.email if self.citizen else None,
            "category_id": self.category_id,
            "category_name": self.category.name if self.category else "General",
            "department_id": self.department_id,
            "department_name": self.department.name if self.department else "Unassigned",
            "assigned_officer_id": self.assigned_officer_id,
            "assigned_officer_name": self.assigned_officer.full_name if self.assigned_officer else "Unassigned",
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "zone": self.zone,
            "priority": self.priority,
            "status": self.status,
            "feedback_rating": self.feedback_rating,
            "feedback_comment": self.feedback_comment,
            "sla_due_date": self.sla_due_date.isoformat() if self.sla_due_date else None,
            "is_sla_breached": self.is_sla_breached(),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
        }
        if include_history:
            data["history"] = [h.to_dict() for h in self.history]
        return data


class ComplaintHistory(db.Model):
    __tablename__ = "complaint_history"

    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(db.Integer, db.ForeignKey("complaints.id", ondelete="CASCADE"), nullable=False, index=True)
    performed_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    previous_status = db.Column(db.String(30), nullable=True)
    new_status = db.Column(db.String(30), nullable=False)
    remarks = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    complaint = db.relationship("Complaint", back_populates="history")
    performed_by = db.relationship("User")

    def to_dict(self):
        return {
            "id": self.id,
            "complaint_id": self.complaint_id,
            "performed_by_user_id": self.performed_by_user_id,
            "performed_by_name": self.performed_by.full_name if self.performed_by else "System",
            "previous_status": self.previous_status,
            "new_status": self.new_status,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
