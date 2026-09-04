"""
Real-time Alert and Rule Engine Models.
"""
from datetime import datetime
from .user import db
from ..config.constants import SeverityLevels

class AlertRule(db.Model):
    __tablename__ = "alert_rules"

    id = db.Column(db.Integer, primary_key=True)
    rule_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    rule_name = db.Column(db.String(150), nullable=False)
    module = db.Column(db.String(50), nullable=False, index=True)  # TRAFFIC, WASTE, WATER, ELECTRICITY, AQI, EMERGENCY
    threshold_field = db.Column(db.String(50), nullable=False)
    operator = db.Column(db.String(10), nullable=False)  # '>', '>=', '<', '<=', '==', '!=', 'ANOMALY'
    threshold_value = db.Column(db.Float, nullable=False)
    severity = db.Column(db.String(20), default=SeverityLevels.WARNING)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    alerts = db.relationship("SystemAlert", back_populates="rule", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "rule_code": self.rule_code,
            "rule_name": self.rule_name,
            "module": self.module,
            "threshold_field": self.threshold_field,
            "operator": self.operator,
            "threshold_value": self.threshold_value,
            "severity": self.severity,
            "is_active": self.is_active,
        }


class SystemAlert(db.Model):
    __tablename__ = "system_alerts"

    id = db.Column(db.Integer, primary_key=True)
    alert_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    rule_id = db.Column(db.Integer, db.ForeignKey("alert_rules.id", ondelete="SET NULL"), nullable=True)
    module = db.Column(db.String(50), nullable=False, index=True)
    severity = db.Column(db.String(20), default=SeverityLevels.WARNING, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    zone = db.Column(db.String(80), nullable=True)
    status = db.Column(db.String(30), default="ACTIVE", index=True)  # ACTIVE, ACKNOWLEDGED, RESOLVED
    triggered_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    acknowledged_at = db.Column(db.DateTime, nullable=True)
    resolved_at = db.Column(db.DateTime, nullable=True)

    rule = db.relationship("AlertRule", back_populates="alerts")

    def to_dict(self):
        return {
            "id": self.id,
            "alert_code": self.alert_code,
            "rule_id": self.rule_id,
            "rule_name": self.rule.rule_name if self.rule else None,
            "module": self.module,
            "severity": self.severity,
            "title": self.title,
            "description": self.description,
            "zone": self.zone,
            "status": self.status,
            "triggered_at": self.triggered_at.isoformat() if self.triggered_at else None,
            "acknowledged_at": self.acknowledged_at.isoformat() if self.acknowledged_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
        }
