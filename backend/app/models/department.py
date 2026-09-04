"""
Department, Officer, and Citizen Profile Models.
"""
from datetime import datetime
from .user import db

class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    contact_email = db.Column(db.String(120), nullable=True)
    contact_phone = db.Column(db.String(30), nullable=True)
    head_officer_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    officers = db.relationship("Officer", back_populates="department")
    complaints = db.relationship("Complaint", back_populates="department")

    def __repr__(self):
        return f"<Department {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "description": self.description,
            "contact_email": self.contact_email,
            "contact_phone": self.contact_phone,
            "officer_count": len(self.officers) if self.officers else 0,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Officer(db.Model):
    __tablename__ = "officers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    badge_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    designation = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=True)
    assigned_zone = db.Column(db.String(80), nullable=True, default="All Zones")
    is_available = db.Column(db.Boolean, default=True)
    performance_score = db.Column(db.Float, default=100.0)
    resolved_complaints_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = db.relationship("User", back_populates="officer_profile")
    department = db.relationship("Department", back_populates="officers")

    def __repr__(self):
        return f"<Officer {self.badge_number} - {self.designation}>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "badge_number": self.badge_number,
            "designation": self.designation,
            "specialization": self.specialization,
            "assigned_zone": self.assigned_zone,
            "department_id": self.department_id,
            "department_name": self.department.name if self.department else None,
            "is_available": self.is_available,
            "performance_score": self.performance_score,
            "resolved_complaints_count": self.resolved_complaints_count,
            "full_name": self.user.full_name if self.user else None,
            "email": self.user.email if self.user else None,
            "phone": self.user.phone_number if self.user else None,
        }


class Citizen(db.Model):
    __tablename__ = "citizens"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    citizen_card_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    emergency_contact = db.Column(db.String(30), nullable=True)
    occupation = db.Column(db.String(100), nullable=True)
    household_size = db.Column(db.Integer, default=1)
    blood_group = db.Column(db.String(5), nullable=True)
    registered_vehicles_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship("User", back_populates="citizen_profile")

    def __repr__(self):
        return f"<Citizen Card ID: {self.citizen_card_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "citizen_card_id": self.citizen_card_id,
            "emergency_contact": self.emergency_contact,
            "occupation": self.occupation,
            "household_size": self.household_size,
            "blood_group": self.blood_group,
            "registered_vehicles_count": self.registered_vehicles_count,
            "full_name": self.user.full_name if self.user else None,
            "email": self.user.email if self.user else None,
            "phone": self.user.phone_number if self.user else None,
            "address": self.user.address if self.user else None,
            "city_zone": self.user.city_zone if self.user else None,
        }
