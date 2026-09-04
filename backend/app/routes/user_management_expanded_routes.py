"""
Flask REST API Blueprint for User_Management.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

user_management_expanded_bp = Blueprint("user_management_expanded_bp", __name__, url_prefix="/api/user_management")

@user_management_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "user_management"}), 200
