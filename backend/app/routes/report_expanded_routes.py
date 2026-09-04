"""
Flask REST API Blueprint for Report.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

report_expanded_bp = Blueprint("report_expanded_bp", __name__, url_prefix="/api/report")

@report_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "report"}), 200
