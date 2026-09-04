"""
Enterprise Domain Logic for Waste.
"""
from ..models.waste_module import db, WasteEntity

class WasteExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = WasteEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
