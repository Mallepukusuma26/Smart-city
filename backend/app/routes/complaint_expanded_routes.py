"""
Flask REST API Blueprint for Complaint.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

complaint_expanded_bp = Blueprint("complaint_expanded_bp", __name__, url_prefix="/api/complaint")

@complaint_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "complaint"}), 200
