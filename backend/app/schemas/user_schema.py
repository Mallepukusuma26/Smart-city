"""
Input Data Payload Validation & Entity Serialization Schemas for User & RBAC Entities.
"""
from dataclasses import dataclass, asdict
from typing import Optional, List
import re

class ValidationError(Exception):
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)


@dataclass
class UserRegisterSchema:
    username: str
    email: str
    password: str
    full_name: str
    role: str = "CITIZEN"
    phone_number: Optional[str] = None
    address: Optional[str] = None
    city_zone: Optional[str] = "Central Zone"
    badge_number: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None

    def validate(self):
        if not self.username or len(self.username) < 3:
            raise ValidationError("Username must be at least 3 characters long.", "username")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Invalid email address format.", "email")
        if len(self.password) < 8:
            raise ValidationError("Password must be at least 8 characters long.", "password")
        if not self.full_name or len(self.full_name) < 2:
            raise ValidationError("Full name is required.", "full_name")
        if self.role == "OFFICER" and not self.badge_number:
            raise ValidationError("Badge number is required for officer registration.", "badge_number")
        return True


@dataclass
class UserLoginSchema:
    login_identifier: str
    password: str

    def validate(self):
        if not self.login_identifier:
            raise ValidationError("Username or email is required.", "login_identifier")
        if not self.password:
            raise ValidationError("Password is required.", "password")
        return True


@dataclass
class UserProfileUpdateSchema:
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    city_zone: Optional[str] = None
    emergency_contact: Optional[str] = None
    occupation: Optional[str] = None

    def validate(self):
        if self.full_name and len(self.full_name) < 2:
            raise ValidationError("Full name must be at least 2 characters.", "full_name")
        return True
