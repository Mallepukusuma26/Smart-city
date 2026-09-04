"""
Enterprise Domain Logic for User_Management.
"""
from ..models.user_management_module import db, UserManagementEntity

class UserManagementExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = UserManagementEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
