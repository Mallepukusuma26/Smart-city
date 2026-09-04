"""
Enterprise Domain Logic for Traffic.
"""
from ..models.traffic_module import db, TrafficEntity

class TrafficExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = TrafficEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
