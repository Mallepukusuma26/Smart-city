"""
Flask REST API Blueprint for Asset.
"""
from flask import Blueprint, jsonify, request, g
from ..security.rbac import login_required

asset_expanded_bp = Blueprint("asset_expanded_bp", __name__, url_prefix="/api/asset")

@asset_expanded_bp.route("/overview", methods=["GET"])
@login_required
def overview():
    return jsonify({"status": "OPERATIONAL", "module": "asset"}), 200
