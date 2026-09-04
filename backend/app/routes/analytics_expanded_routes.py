"""
Flask REST API Blueprint for Analytics.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

analytics_expanded_bp = Blueprint("analytics_expanded_bp", __name__, url_prefix="/api/analytics")

@analytics_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "analytics"}), 200
