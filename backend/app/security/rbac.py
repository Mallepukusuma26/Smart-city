"""
Role-Based Access Control (RBAC) Decorators and Permission Verification.
"""
from functools import wraps
from flask import request, jsonify, g, session, redirect, url_for
from ..config.constants import Roles

def login_required(f):
    """Ensure user is authenticated via Session or Bearer Token."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = getattr(g, "current_user", None)
        if not user:
            # Check session
            session_user_id = session.get("user_id")
            if not session_user_id:
                if request.is_json or request.path.startswith("/api/"):
                    return jsonify({"error": "Unauthorized. Authentication required.", "code": 401}), 401
                return redirect("/auth/login")
        return f(*args, **kwargs)
    return decorated_function


def role_required(*allowed_roles):
    """
    Enforce backend Role-Based Access Control on Flask routes.
    If authenticated user does NOT have one of allowed_roles:
    - For API routes -> return 403 Forbidden JSON
    - For Web pages -> redirect to user's assigned dashboard or login
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = getattr(g, "current_user", None)
            if not user:
                if request.is_json or request.path.startswith("/api/"):
                    return jsonify({"error": "Unauthorized. Please log in.", "code": 401}), 401
                return redirect("/auth/login")

            user_roles = user.roles if hasattr(user, "roles") else getattr(g, "user_roles", [])
            
            # Check if any allowed role matches user's assigned roles
            has_permission = any(r in user_roles for r in allowed_roles)
            if not has_permission:
                if request.is_json or request.path.startswith("/api/"):
                    return jsonify({
                        "error": "Forbidden. Access denied for your user role.",
                        "user_roles": user_roles,
                        "required_roles": list(allowed_roles),
                        "code": 403
                    }), 403
                
                # Redirect user safely based on their actual role
                if Roles.CITIZEN in user_roles:
                    return redirect("/citizen/dashboard")
                elif Roles.OFFICER in user_roles:
                    return redirect("/officer/dashboard")
                elif Roles.ADMIN in user_roles:
                    return redirect("/admin/dashboard")
                return redirect("/auth/login")

            return f(*args, **kwargs)
        return decorated_function
    return decorator


def citizen_required(f):
    return role_required(Roles.CITIZEN, Roles.ADMIN)(f)

def officer_required(f):
    return role_required(Roles.OFFICER, Roles.ADMIN)(f)

def admin_required(f):
    return role_required(Roles.ADMIN)(f)
