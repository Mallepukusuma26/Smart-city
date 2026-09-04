"""
Flask REST API Blueprint for Audit_Logging.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

audit_logging_expanded_bp = Blueprint("audit_logging_expanded_bp", __name__, url_prefix="/api/audit_logging")

@audit_logging_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "audit_logging"}), 200
