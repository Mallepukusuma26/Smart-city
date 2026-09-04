"""
Flask REST API Blueprint for Parking.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

parking_expanded_bp = Blueprint("parking_expanded_bp", __name__, url_prefix="/api/parking")

@parking_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "parking"}), 200
