"""
Officer Dashboard API Endpoints.
"""
from flask import Blueprint, request, jsonify, g
from ..security.rbac import officer_required
from ..services.complaint_service import ComplaintService
from ..services.analytics_service import AnalyticsService
from ..models import Complaint, EmergencyIncident, SystemAlert, UserNotification, Officer, Department

officer_bp = Blueprint("officer_bp", __name__, url_prefix="/api/officer")

@officer_bp.route("/dashboard", methods=["GET"])
@officer_required
def officer_dashboard():
    user = g.current_user
    officer_profile = user.officer_profile

    department_id = officer_profile.department_id if officer_profile else None
    department_name = officer_profile.department.name if (officer_profile and officer_profile.department) else "General"

    # Department or assigned complaints
    assigned = Complaint.query.filter_by(assigned_officer_id=user.id).all()
    department_complaints = Complaint.query.filter_by(department_id=department_id).all() if department_id else assigned

    pending = [c for c in department_complaints if c.status in ["SUBMITTED", "ASSIGNED", "IN_PROGRESS"]]
    high_priority = [c for c in department_complaints if c.priority in ["HIGH", "CRITICAL"]]

    # Department analytics
    analytics = AnalyticsService.get_department_analytics(department_id) if department_id else {}

    alerts = SystemAlert.query.filter(SystemAlert.status != "RESOLVED").order_by(SystemAlert.triggered_at.desc()).limit(5).all()

    return jsonify({
        "officer": {
            "name": user.full_name,
            "badge_number": officer_profile.badge_number if officer_profile else "OFF-001",
            "designation": officer_profile.designation if officer_profile else "Officer",
            "department_name": department_name,
            "assigned_zone": officer_profile.assigned_zone if officer_profile else "Central Zone"
        },
        "stats": {
            "assigned_to_me": len(assigned),
            "department_total": len(department_complaints),
            "pending_count": len(pending),
            "high_priority_count": len(high_priority)
        },
        "assigned_complaints": [c.to_dict() for c in assigned[:10]],
        "recent_alerts": [a.to_dict() for a in alerts],
        "department_analytics": analytics
    }), 200


@officer_bp.route("/complaints", methods=["GET"])
@officer_required
def get_department_complaints():
    user = g.current_user
    officer_profile = user.officer_profile
    department_id = officer_profile.department_id if officer_profile else None

    status = request.args.get("status")
    query = Complaint.query
    if department_id:
        query = query.filter_by(department_id=department_id)
    if status:
        query = query.filter_by(status=status)

    complaints = query.order_by(Complaint.created_at.desc()).all()
    return jsonify({"complaints": [c.to_dict() for c in complaints]}), 200


@officer_bp.route("/complaints/<int:complaint_id>/update", methods=["POST"])
@officer_required
def update_complaint_status(complaint_id):
    user = g.current_user
    data = request.get_json() or {}
    new_status = data.get("status")
    remarks = data.get("remarks", "Updated by officer.")

    if not new_status:
        return jsonify({"error": "Status is required.", "code": 400}), 400

    success, msg = ComplaintService.update_status(complaint_id, user.id, new_status, remarks)
    if not success:
        return jsonify({"error": msg, "code": 400}), 400

    return jsonify({"message": msg}), 200
