"""
Enterprise Domain Logic for Emergency.
"""
from ..models.emergency_module import db, EmergencyEntity

class EmergencyExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = EmergencyEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
