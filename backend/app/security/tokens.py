"""
JSON Web Token (JWT) and Session Token Management.
"""
import time
import jwt
from flask import current_app

def generate_access_token(user_id: int, username: str, roles: list, expires_in: int = 86400) -> str:
    """Generate JWT payload containing user ID, username, roles, and expiration timestamp."""
    secret = current_app.config.get("JWT_SECRET_KEY", "fallback_secret_key_2026")
    payload = {
        "sub": user_id,
        "username": username,
        "roles": roles,
        "iat": int(time.time()),
        "exp": int(time.time()) + expires_in,
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def decode_access_token(token: str) -> dict:
    """Decode and validate a JWT access token."""
    secret = current_app.config.get("JWT_SECRET_KEY", "fallback_secret_key_2026")
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
