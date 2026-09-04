"""
Flask REST API Blueprint for Department_Management.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

department_management_expanded_bp = Blueprint("department_management_expanded_bp", __name__, url_prefix="/api/department_management")

@department_management_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "department_management"}), 200
