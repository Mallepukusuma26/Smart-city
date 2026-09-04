"""
Flask REST API Blueprint for Waste.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

waste_expanded_bp = Blueprint("waste_expanded_bp", __name__, url_prefix="/api/waste")

@waste_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "waste"}), 200
