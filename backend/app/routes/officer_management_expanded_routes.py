"""
Flask REST API Blueprint for Officer_Management.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

officer_management_expanded_bp = Blueprint("officer_management_expanded_bp", __name__, url_prefix="/api/officer_management")

@officer_management_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "officer_management"}), 200
