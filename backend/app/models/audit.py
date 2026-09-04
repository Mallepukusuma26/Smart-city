"""
Audit Logging and Security Tracking Models.
"""
from datetime import datetime
from .user import db

class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    username = db.Column(db.String(80), nullable=True)
    role = db.Column(db.String(30), nullable=True)
    action = db.Column(db.String(100), nullable=False, index=True)  # LOGIN, CREATE_COMPLAINT, RESOLVE_COMPLAINT, ML_TRAIN
    resource_type = db.Column(db.String(50), nullable=True)
    resource_id = db.Column(db.String(50), nullable=True)
    details = db.Column(db.Text, nullable=True)
    ip_address = db.Column(db.String(50), default="127.0.0.1")
    user_agent = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)

    user = db.relationship("User")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "username": self.username or (self.user.username if self.user else "Anonymous"),
            "role": self.role,
            "action": self.action,
            "resource_type": self.resource_type,
            "resource_id": self.resource_id,
            "details": self.details,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }
