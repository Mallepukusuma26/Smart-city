"""
Flask REST API Blueprint for Traffic.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

traffic_expanded_bp = Blueprint("traffic_expanded_bp", __name__, url_prefix="/api/traffic")

@traffic_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "traffic"}), 200
