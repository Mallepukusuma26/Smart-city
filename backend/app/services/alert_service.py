"""
Real-time Alert and Rule Evaluation Engine Service.
"""
from datetime import datetime
from ..models import db, AlertRule, SystemAlert
from ..config.constants import SeverityLevels

class AlertService:
    @staticmethod
    def trigger_alert(module, title, description, severity=SeverityLevels.WARNING, zone="Central Zone", rule_id=None):
        alert_code = f"ALT-{module[:3].upper()}-{datetime.utcnow().strftime('%M%S')}-{db.session.query(SystemAlert).count() + 1:04d}"
        alert = SystemAlert(
            alert_code=alert_code,
            rule_id=rule_id,
            module=module,
            severity=severity,
            title=title,
            description=description,
            zone=zone,
            status="ACTIVE",
        )
        db.session.add(alert)
        db.session.commit()
        return alert

    @staticmethod
    def acknowledge_alert(alert_id):
        alert = SystemAlert.query.get(alert_id)
        if alert and alert.status == "ACTIVE":
            alert.status = "ACKNOWLEDGED"
            alert.acknowledged_at = datetime.utcnow()
            db.session.commit()
            return True
        return False

    @staticmethod
    def resolve_alert(alert_id):
        alert = SystemAlert.query.get(alert_id)
        if alert:
            alert.status = "RESOLVED"
            alert.resolved_at = datetime.utcnow()
            db.session.commit()
            return True
        return False
