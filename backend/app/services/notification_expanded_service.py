"""
Enterprise Domain Logic for Notification.
"""
from ..models.notification_module import db, NotificationEntity

class NotificationExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = NotificationEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
