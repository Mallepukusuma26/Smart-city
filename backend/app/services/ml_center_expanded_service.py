"""
Enterprise Domain Logic for Ml_Center.
"""
from ..models.ml_center_module import db, MlCenterEntity

class MlCenterExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = MlCenterEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
