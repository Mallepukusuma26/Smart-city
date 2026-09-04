"""
Authentication Request Middleware.
"""
from flask import request, g, session
from ..models.user import User
from ..security.tokens import decode_access_token

def init_auth_middleware(app):
    @app.before_request
    def load_authenticated_user():
        g.current_user = None
        g.user_roles = []

        # 1. Check Authorization Bearer Header
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            payload = decode_access_token(token)
            if payload and "sub" in payload:
                user = User.query.get(payload["sub"])
                if user and user.is_active:
                    g.current_user = user
                    g.user_roles = user.roles
                    return

        # 2. Check Flask Session
        user_id = session.get("user_id")
        if user_id:
            user = User.query.get(user_id)
            if user and user.is_active:
                g.current_user = user
                g.user_roles = user.roles
                return
