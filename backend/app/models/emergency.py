"""
Emergency & Incident Management Database Models.
"""
from datetime import datetime
from .user import db
from ..config.constants import EmergencyTypes

class EmergencyIncident(db.Model):
    __tablename__ = "emergency_incidents"

    id = db.Column(db.Integer, primary_key=True)
    incident_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    incident_type = db.Column(db.String(50), nullable=False, index=True)
    severity = db.Column(db.String(20), default="CRITICAL", index=True)  # LOW, MEDIUM, HIGH, CRITICAL
    location = db.Column(db.String(255), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    reported_by_phone = db.Column(db.String(30), nullable=True)
    assigned_team = db.Column(db.String(100), default="Quick Response Force #1")
    status = db.Column(db.String(50), default="REPORTED")  # REPORTED, DISPATCHED, ON_SITE, RESOLVED, CLOSED
    response_time_minutes = db.Column(db.Float, nullable=True)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    dispatched_at = db.Column(db.DateTime, nullable=True)
    resolved_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "incident_code": self.incident_code,
            "incident_type": self.incident_type,
            "severity": self.severity,
            "location": self.location,
            "zone": self.zone,
            "description": self.description,
            "reported_by_phone": self.reported_by_phone,
            "assigned_team": self.assigned_team,
            "status": self.status,
            "response_time_minutes": self.response_time_minutes,
            "reported_at": self.reported_at.isoformat() if self.reported_at else None,
            "dispatched_at": self.dispatched_at.isoformat() if self.dispatched_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
        }
