"""
Admin Master Operations API Endpoints.
"""
from flask import Blueprint, request, jsonify, g
from ..security.rbac import admin_required
from ..services.analytics_service import AnalyticsService
from ..services.city_services import CityOperationsService
from ..models import (
    db, User, Role, Department, Officer, Citizen, Complaint,
    EmergencyIncident, SystemAlert, AuditLog, MLModelRegistry, PredictionLog
)

admin_bp = Blueprint("admin_bp", __name__, url_prefix="/api/admin")

@admin_bp.route("/dashboard", methods=["GET"])
@admin_required
def admin_dashboard():
    # Master platform overview stats
    total_users = User.query.count()
    citizens_count = Citizen.query.count()
    officers_count = Officer.query.count()
    departments_count = Department.query.count()
    complaints_count = Complaint.query.count()
    emergencies_count = EmergencyIncident.query.filter(EmergencyIncident.status != "CLOSED").count()
    active_alerts = SystemAlert.query.filter(SystemAlert.status != "RESOLVED").count()
    trained_models_count = MLModelRegistry.query.count()

    kpis = AnalyticsService.get_city_kpis()

    return jsonify({
        "admin_stats": {
            "total_users": total_users,
            "total_citizens": citizens_count,
            "total_officers": officers_count,
            "total_departments": departments_count,
            "total_complaints": complaints_count,
            "active_emergencies": emergencies_count,
            "active_alerts": active_alerts,
            "trained_ml_models": trained_models_count
        },
        "city_kpis": kpis,
        "recent_alerts": [a.to_dict() for a in SystemAlert.query.order_by(SystemAlert.triggered_at.desc()).limit(5).all()],
        "recent_audit_logs": [log.to_dict() for log in AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(5).all()]
    }), 200


@admin_bp.route("/users", methods=["GET", "POST"])
@admin_required
def manage_users():
    if request.method == "POST":
        data = request.get_json() or {}
        # Create or update user
        return jsonify({"message": "User action performed."}), 200

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)
    pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "users": [u.to_dict(include_profile=True) for u in pagination.items],
        "total": pagination.total,
        "page": page,
        "pages": pagination.pages
    }), 200


@admin_bp.route("/departments", methods=["GET", "POST"])
@admin_required
def manage_departments():
    if request.method == "POST":
        data = request.get_json() or {}
        dept = Department(
            name=data.get("name"),
            code=data.get("code"),
            description=data.get("description"),
            contact_email=data.get("contact_email"),
            contact_phone=data.get("contact_phone")
        )
        db.session.add(dept)
        db.session.commit()
        return jsonify({"message": "Department created.", "department": dept.to_dict()}), 201

    depts = Department.query.all()
    return jsonify({"departments": [d.to_dict() for d in depts]}), 200


@admin_bp.route("/ai", methods=["GET"])
@admin_required
def get_ai_registry():
    models = MLModelRegistry.query.all()
    recent_logs = PredictionLog.query.order_by(PredictionLog.created_at.desc()).limit(20).all()
    return jsonify({
        "ml_models": [m.to_dict() for m in models],
        "recent_predictions": [p.to_dict() for p in recent_logs]
    }), 200


@admin_bp.route("/audit-logs", methods=["GET"])
@admin_required
def get_audit_logs():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 50, type=int)
    pagination = AuditLog.query.order_by(AuditLog.timestamp.desc()).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "audit_logs": [log.to_dict() for log in pagination.items],
        "total": pagination.total,
        "page": page,
        "pages": pagination.pages
    }), 200
