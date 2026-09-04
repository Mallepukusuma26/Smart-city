"""
Enterprise Domain Logic for Report.
"""
from ..models.report_module import db, ReportEntity

class ReportExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = ReportEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
