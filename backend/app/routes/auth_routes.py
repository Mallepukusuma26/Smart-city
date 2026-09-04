"""
Authentication API Endpoints.
"""
from flask import Blueprint, request, jsonify, session, g
from ..services.auth_service import AuthService
from ..security.rbac import login_required

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    full_name = data.get("full_name")

    if not username or not email or not password or not full_name:
        return jsonify({"error": "Missing required registration fields.", "code": 400}), 400

    role = data.get("role", "CITIZEN").upper()
    if role == "OFFICER":
        badge_number = data.get("badge_number")
        designation = data.get("designation", "Junior Officer")
        if not badge_number:
            return jsonify({"error": "Badge number is required for officer registration.", "code": 400}), 400
        success, msg, result = AuthService.register_officer(
            username=username, email=email, password=password, full_name=full_name,
            badge_number=badge_number, designation=designation, department_id=data.get("department_id")
        )
    else:
        success, msg, result = AuthService.register_citizen(
            username=username, email=email, password=password, full_name=full_name,
            phone_number=data.get("phone_number"), address=data.get("address")
        )

    if not success:
        return jsonify({"error": msg, "code": 400}), 400

    session["user_id"] = result["user"]["id"]
    return jsonify({"message": msg, "data": result}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username_or_email = data.get("username") or data.get("email") or data.get("login_identifier")
    password = data.get("password")

    if not username_or_email or not password:
        return jsonify({"error": "Please provide username/email and password.", "code": 400}), 400

    success, msg, result = AuthService.authenticate_user(username_or_email, password)
    if not success:
        return jsonify({"error": msg, "code": 401}), 401

    session["user_id"] = result["user"]["id"]
    return jsonify({"message": msg, "data": result}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Successfully logged out."}), 200


@auth_bp.route("/profile", methods=["GET"])
@login_required
def get_profile():
    user = getattr(g, "current_user", None)
    if not user:
        return jsonify({"error": "Unauthorized", "code": 401}), 401
    return jsonify({"user": user.to_dict(include_profile=True)}), 200
