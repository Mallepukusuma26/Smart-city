"""
Flask REST API Blueprint for Ml_Center.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

ml_center_expanded_bp = Blueprint("ml_center_expanded_bp", __name__, url_prefix="/api/ml_center")

@ml_center_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "ml_center"}), 200
