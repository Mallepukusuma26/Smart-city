"""
Enterprise Domain Logic for System_Settings.
"""
from ..models.system_settings_module import db, SystemSettingsEntity

class SystemSettingsExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = SystemSettingsEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
