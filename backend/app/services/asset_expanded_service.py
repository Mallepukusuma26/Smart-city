"""
Enterprise Domain Logic for Asset.
"""
from ..models.asset_module import db, AssetEntity

class AssetExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = AssetEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
