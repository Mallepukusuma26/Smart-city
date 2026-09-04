"""
Enterprise Domain Logic for Water.
"""
from ..models.water_module import db, WaterEntity

class WaterExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = WaterEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
