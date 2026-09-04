"""
Audit Logging Request Middleware.
"""
from flask import request, g
from ..models.user import db
from ..models.audit import AuditLog

def init_audit_middleware(app):
    @app.after_request
    def log_mutating_requests(response):
        # Record state-changing API actions (POST, PUT, PATCH, DELETE)
        if request.method in ["POST", "PUT", "PATCH", "DELETE"] and request.path.startswith("/api/"):
            try:
                user = getattr(g, "current_user", None)
                user_id = user.id if user else None
                username = user.username if user else "Anonymous"
                role = user.roles[0] if (user and user.roles) else "UNAUTHENTICATED"
                
                action_name = f"{request.method} {request.path}"
                ip_addr = request.remote_addr or "127.0.0.1"
                user_agent = request.headers.get("User-Agent", "Unknown")[:250]
                
                log_entry = AuditLog(
                    user_id=user_id,
                    username=username,
                    role=role,
                    action=action_name,
                    resource_type=request.path.split("/")[2] if len(request.path.split("/")) > 2 else "API",
                    details=f"Status: {response.status_code}",
                    ip_address=ip_addr,
                    user_agent=user_agent
                )
                db.session.add(log_entry)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
        return response
