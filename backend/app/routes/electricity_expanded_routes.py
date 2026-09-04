"""
Flask REST API Blueprint for Electricity.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

electricity_expanded_bp = Blueprint("electricity_expanded_bp", __name__, url_prefix="/api/electricity")

@electricity_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "electricity"}), 200
