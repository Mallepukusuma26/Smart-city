"""
Flask REST API Blueprint for Pollution.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

pollution_expanded_bp = Blueprint("pollution_expanded_bp", __name__, url_prefix="/api/pollution")

@pollution_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "pollution"}), 200
