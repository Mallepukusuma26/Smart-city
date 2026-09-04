"""
User, Role, and Permission Models for Role-Based Access Control (RBAC).
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from ..config.constants import Roles

# Shared db instance initialized in app factory
db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    users = db.relationship("UserRole", back_populates="role", cascade="all, delete-orphan")
    permissions = db.relationship("RolePermission", back_populates="role", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Role {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    module = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    roles = db.relationship("RolePermission", back_populates="permission", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Permission {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "module": self.module,
            "description": self.description,
        }


class RolePermission(db.Model):
    __tablename__ = "role_permissions"

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)

    role = db.relationship("Role", back_populates="permissions")
    permission = db.relationship("Permission", back_populates="roles")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(30), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city_zone = db.Column(db.String(80), nullable=True, default="Central Zone")
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verified = db.Column(db.Boolean, default=False, nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user_roles = db.relationship("UserRole", back_populates="user", cascade="all, delete-orphan")
    citizen_profile = db.relationship("Citizen", back_populates="user", uselist=False, cascade="all, delete-orphan")
    officer_profile = db.relationship("Officer", back_populates="user", uselist=False, cascade="all, delete-orphan")
    complaints = db.relationship("Complaint", back_populates="citizen", foreign_keys="Complaint.citizen_id")
    assigned_complaints = db.relationship("Complaint", back_populates="assigned_officer", foreign_keys="Complaint.assigned_officer_id")
    notifications = db.relationship("UserNotification", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def roles(self):
        return [ur.role.name for ur in self.user_roles if ur.role]

    def has_role(self, role_name):
        return role_name in self.roles

    def is_citizen(self):
        return Roles.CITIZEN in self.roles

    def is_officer(self):
        return Roles.OFFICER in self.roles

    def is_admin(self):
        return Roles.ADMIN in self.roles

    def __repr__(self):
        return f"<User {self.username} ({','.join(self.roles)})>"

    def to_dict(self, include_profile=False):
        data = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "address": self.address,
            "city_zone": self.city_zone,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
            "roles": self.roles,
            "last_login": self.last_login.isoformat() if self.last_login else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
        if include_profile:
            if self.is_citizen() and self.citizen_profile:
                data["citizen_details"] = self.citizen_profile.to_dict()
            if self.is_officer() and self.officer_profile:
                data["officer_details"] = self.officer_profile.to_dict()
        return data


class UserRole(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False, index=True)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="user_roles")
    role = db.relationship("Role", back_populates="users")
