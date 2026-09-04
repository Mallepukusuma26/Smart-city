"""
Password Security Utilities.
"""
import re
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """Generate a secure PBKDF2/SHA256 password hash."""
    return generate_password_hash(password, method="scrypt" if hasattr(generate_password_hash, "scrypt") else "pbkdf2:sha256")

def verify_password(stored_hash: str, password: str) -> bool:
    """Verify raw password against stored hash."""
    if not stored_hash or not password:
        return False
    return check_password_hash(stored_hash, password)

def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validate password complexity requirements:
    - Minimum 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one numeric digit."
    return True, "Password is strong."
