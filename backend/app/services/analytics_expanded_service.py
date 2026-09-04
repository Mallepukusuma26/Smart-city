"""
Enterprise Domain Logic for Analytics.
"""
from ..models.analytics_module import db, AnalyticsEntity

class AnalyticsExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = AnalyticsEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
