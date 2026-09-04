"""
Enterprise Domain Logic for Alert.
"""
from ..models.alert_module import db, AlertEntity

class AlertExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = AlertEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
