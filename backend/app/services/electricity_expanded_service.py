"""
Enterprise Domain Logic for Electricity.
"""
from ..models.electricity_module import db, ElectricityEntity

class ElectricityExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = ElectricityEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
