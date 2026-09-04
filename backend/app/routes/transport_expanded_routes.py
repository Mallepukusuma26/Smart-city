"""
Flask REST API Blueprint for Transport.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

transport_expanded_bp = Blueprint("transport_expanded_bp", __name__, url_prefix="/api/transport")

@transport_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "transport"}), 200
