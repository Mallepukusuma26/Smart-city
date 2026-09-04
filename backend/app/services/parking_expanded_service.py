"""
Enterprise Domain Logic for Parking.
"""
from ..models.parking_module import db, ParkingEntity

class ParkingExpandedService:
    @staticmethod
    def process_analytics(entity_id):
        entity = ParkingEntity.query.get(entity_id)
        if not entity:
            return None
        return {
            "entity": entity.to_dict(),
            "health_score": round((entity.metric_value_1 + entity.metric_value_2) / 2.0, 2)
        }
