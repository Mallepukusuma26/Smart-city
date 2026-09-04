"""
Flask REST API Blueprint for Alert.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

alert_expanded_bp = Blueprint("alert_expanded_bp", __name__, url_prefix="/api/alert")

@alert_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "alert"}), 200
