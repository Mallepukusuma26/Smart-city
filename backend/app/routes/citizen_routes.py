"""
Citizen Dashboard API Endpoints.
"""
from flask import Blueprint, request, jsonify, g
from ..security.rbac import citizen_required
from ..services.complaint_service import ComplaintService
from ..services.city_services import CityOperationsService
from ..models import Complaint, SystemAlert, UserNotification, WasteBin, WaterTank, TransportRoute

citizen_bp = Blueprint("citizen_bp", __name__, url_prefix="/api/citizen")

@citizen_bp.route("/dashboard", methods=["GET"])
@citizen_required
def citizen_dashboard():
    user = g.current_user
    # Citizen complaints
    my_complaints = Complaint.query.filter_by(citizen_id=user.id).order_by(Complaint.created_at.desc()).all()
    pending = [c for c in my_complaints if c.status in ["SUBMITTED", "ASSIGNED", "IN_PROGRESS", "ESCALATED"]]
    resolved = [c for c in my_complaints if c.status in ["RESOLVED", "CLOSED"]]

    # City service summaries
    traffic = CityOperationsService.get_traffic_overview()
    waste = CityOperationsService.get_waste_overview()
    water = CityOperationsService.get_water_overview()
    pollution = CityOperationsService.get_pollution_overview()

    alerts = SystemAlert.query.filter(SystemAlert.status != "RESOLVED").order_by(SystemAlert.triggered_at.desc()).limit(5).all()
    notifications = UserNotification.query.filter_by(user_id=user.id, is_read=False).limit(5).all()

    return jsonify({
        "citizen": {
            "name": user.full_name,
            "citizen_id": user.citizen_profile.citizen_card_id if user.citizen_profile else f"CTZ-{user.id:06d}",
            "email": user.email,
            "zone": user.city_zone
        },
        "complaint_stats": {
            "total_my_complaints": len(my_complaints),
            "pending_count": len(pending),
            "resolved_count": len(resolved)
        },
        "recent_complaints": [c.to_dict() for c in my_complaints[:5]],
        "recent_alerts": [a.to_dict() for a in alerts],
        "recent_notifications": [n.to_dict() for n in notifications],
        "city_status": {
            "traffic": traffic,
            "waste": waste,
            "water": water,
            "pollution": pollution
        }
    }), 200


@citizen_bp.route("/complaints", methods=["GET", "POST"])
@citizen_required
def citizen_complaints():
    user = g.current_user
    if request.method == "POST":
        data = request.get_json() or {}
        title = data.get("title")
        description = data.get("description")
        location = data.get("location")
        zone = data.get("zone", user.city_zone or "Central Zone")
        category_id = data.get("category_id")
        priority = data.get("priority", "MEDIUM")

        if not title or not description or not location:
            return jsonify({"error": "Title, description, and location are required.", "code": 400}), 400

        complaint = ComplaintService.create_complaint(
            citizen_id=user.id, title=title, description=description,
            location=location, zone=zone, category_id=category_id, priority=priority
        )
        return jsonify({"message": "Complaint submitted successfully.", "complaint": complaint.to_dict()}), 201

    # GET citizen's own complaints
    complaints = Complaint.query.filter_by(citizen_id=user.id).order_by(Complaint.created_at.desc()).all()
    return jsonify({"complaints": [c.to_dict() for c in complaints]}), 200


@citizen_bp.route("/notifications", methods=["GET"])
@citizen_required
def citizen_notifications():
    user = g.current_user
    notifications = UserNotification.query.filter_by(user_id=user.id).order_by(UserNotification.received_at.desc()).all()
    return jsonify({"notifications": [n.to_dict() for n in notifications]}), 200


@citizen_bp.route("/alerts", methods=["GET"])
@citizen_required
def citizen_alerts():
    alerts = SystemAlert.query.filter(SystemAlert.status != "RESOLVED").order_by(SystemAlert.triggered_at.desc()).all()
    return jsonify({"alerts": [a.to_dict() for a in alerts]}), 200
