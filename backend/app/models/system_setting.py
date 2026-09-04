"""
System Settings and Module Configuration Models.
"""
from datetime import datetime
from .user import db

class SystemSetting(db.Model):
    __tablename__ = "system_settings"

    id = db.Column(db.Integer, primary_key=True)
    setting_key = db.Column(db.String(100), unique=True, nullable=False, index=True)
    setting_value = db.Column(db.Text, nullable=False)
    data_type = db.Column(db.String(20), default="string")  # string, int, float, bool, json
    description = db.Column(db.String(255), nullable=True)
    module = db.Column(db.String(50), default="GENERAL")
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "setting_key": self.setting_key,
            "setting_value": self.setting_value,
            "data_type": self.data_type,
            "description": self.description,
            "module": self.module,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
