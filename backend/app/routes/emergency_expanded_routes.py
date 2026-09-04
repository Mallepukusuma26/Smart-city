"""
Flask REST API Blueprint for Emergency.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

emergency_expanded_bp = Blueprint("emergency_expanded_bp", __name__, url_prefix="/api/emergency")

@emergency_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "emergency"}), 200
