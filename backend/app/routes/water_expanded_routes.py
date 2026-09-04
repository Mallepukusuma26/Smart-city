"""
Flask REST API Blueprint for Water.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

water_expanded_bp = Blueprint("water_expanded_bp", __name__, url_prefix="/api/water")

@water_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "water"}), 200
