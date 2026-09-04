"""
Flask REST API Blueprint for Notification.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

notification_expanded_bp = Blueprint("notification_expanded_bp", __name__, url_prefix="/api/notification")

@notification_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "notification"}), 200
