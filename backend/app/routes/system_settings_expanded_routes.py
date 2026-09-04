"""
Flask REST API Blueprint for System_Settings.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

system_settings_expanded_bp = Blueprint("system_settings_expanded_bp", __name__, url_prefix="/api/system_settings")

@system_settings_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "system_settings"}), 200
