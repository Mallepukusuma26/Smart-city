"""
Smart City Operational Module API Endpoints.
"""
from flask import Blueprint, request, jsonify, g, send_file
from ..security.rbac import login_required, role_required, admin_required, officer_required
from ..services.city_services import CityOperationsService
from ..services.report_service import ReportService
from ..services.alert_service import AlertService
from ..ml.pipelines import MLInferenceEngine
from ..models import (
    Road, TrafficRecord, WasteBin, WasteRecord, WaterTank, WaterRecord,
    Transformer, ElectricityRecord, ParkingLocation, ParkingRecord,
    TransportRoute, PassengerRecord, PollutionStation, PollutionRecord,
    EmergencyIncident, SystemAlert
)

service_bp = Blueprint("service_bp", __name__, url_prefix="/api/services")

# ---------------- TRAFFIC ----------------
@service_bp.route("/traffic/overview", methods=["GET"])
@login_required
def traffic_overview():
    return jsonify(CityOperationsService.get_traffic_overview()), 200

# ---------------- WASTE ----------------
@service_bp.route("/waste/overview", methods=["GET"])
@login_required
def waste_overview():
    return jsonify(CityOperationsService.get_waste_overview()), 200

# ---------------- WATER ----------------
@service_bp.route("/water/overview", methods=["GET"])
@login_required
def water_overview():
    return jsonify(CityOperationsService.get_water_overview()), 200

# ---------------- ELECTRICITY ----------------
@service_bp.route("/electricity/overview", methods=["GET"])
@login_required
def electricity_overview():
    return jsonify(CityOperationsService.get_electricity_overview()), 200

# ---------------- PARKING ----------------
@service_bp.route("/parking/overview", methods=["GET"])
@login_required
def parking_overview():
    return jsonify(CityOperationsService.get_parking_overview()), 200

# ---------------- TRANSPORT ----------------
@service_bp.route("/transport/overview", methods=["GET"])
@login_required
def transport_overview():
    return jsonify(CityOperationsService.get_transport_overview()), 200

# ---------------- POLLUTION ----------------
@service_bp.route("/pollution/overview", methods=["GET"])
@login_required
def pollution_overview():
    return jsonify(CityOperationsService.get_pollution_overview()), 200

# ---------------- EMERGENCIES ----------------
@service_bp.route("/emergencies", methods=["GET", "POST"])
@login_required
def emergencies():
    if request.method == "POST":
        data = request.get_json() or {}
        inc_code = f"EMG-{g.current_user.id}-{EmergencyIncident.query.count()+1:04d}"
        emg = EmergencyIncident(
            incident_code=inc_code,
            incident_type=data.get("incident_type", "ACCIDENT"),
            severity=data.get("severity", "CRITICAL"),
            location=data.get("location", "Unknown Location"),
            zone=data.get("zone", g.current_user.city_zone or "Central Zone"),
            description=data.get("description", "Emergency incident reported via portal."),
            reported_by_phone=data.get("phone") or g.current_user.phone_number
        )
        from ..models import db
        db.session.add(emg)
        db.session.commit()
        return jsonify({"message": "Emergency registered.", "incident": emg.to_dict()}), 201

    incidents = EmergencyIncident.query.order_by(EmergencyIncident.reported_at.desc()).limit(100).all()
    return jsonify({"emergencies": [i.to_dict() for i in incidents]}), 200

# ---------------- AI PREDICTIONS ----------------
@service_bp.route("/ai/predict", methods=["POST"])
@login_required
def ai_predict():
    data = request.get_json() or {}
    model_type = data.get("model_type", "traffic")

    if model_type == "traffic":
        res = MLInferenceEngine.predict_traffic(data.get("vehicle_count", 400), data.get("avg_speed_kmh", 35.0), data.get("is_peak_hour", 1))
    elif model_type == "waste":
        res = MLInferenceEngine.predict_waste_overflow(data.get("fill_level", 85.0), data.get("weight_kg", 850.0))
    elif model_type == "water":
        res = MLInferenceEngine.predict_water_demand(data.get("flow_rate_lps", 50.0))
    elif model_type == "electricity":
        res = MLInferenceEngine.predict_electricity_demand(data.get("consumption_kwh", 45.0))
    elif model_type == "parking":
        res = MLInferenceEngine.predict_parking_occupancy(data.get("location_id", 1), data.get("occupied_count", 150), data.get("available_count", 50))
    elif model_type == "pollution":
        res = MLInferenceEngine.predict_aqi(data.get("pm2_5", 45.0), data.get("pm10", 80.0))
    elif model_type == "transport_demand":
        res = MLInferenceEngine.predict_transport_demand(data.get("route_id", 1))
    elif model_type == "anomaly":
        res = MLInferenceEngine.detect_anomalies(data.get("pm2_5", 120.0), data.get("pm10", 250.0), data.get("co", 5.0), data.get("no2", 80.0), data.get("so2", 30.0), data.get("o3", 50.0))
    else:
        res = {"error": "Invalid model type"}

    return jsonify({"prediction": res}), 200

# ---------------- REPORTS & EXPORTS ----------------
@service_bp.route("/reports/export", methods=["GET"])
@login_required
def export_report():
    module_name = request.args.get("module", "complaints")
    fmt = request.args.get("format", "csv").lower()

    if fmt == "csv":
        csv_str = ReportService.generate_csv_report(module_name)
        return csv_str, 200, {"Content-Type": "text/csv", "Content-Disposition": f"attachment; filename={module_name}_report.csv"}
    elif fmt == "pdf":
        rows = [["ID / Code", "Zone / Description", "Status / Metrics"]]
        if module_name == "complaints":
            from ..models import Complaint
            for c in Complaint.query.limit(20).all():
                rows.append([c.ticket_number, f"{c.title[:25]}... ({c.zone})", c.status])
        else:
            rows.append(["SYS-001", "Summary Metric", "OPERATIONAL"])

        pdf_path = ReportService.generate_pdf_report(f"{module_name.upper()} Municipal Summary Report", rows, f"{module_name}_report.pdf")
        return send_file(pdf_path, as_attachment=True)

    return jsonify({"error": "Unsupported format"}), 400
