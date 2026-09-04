"""
Parking Dynamic Pricing & Occupancy Management Service.
"""
from ..models import db, ParkingLocation, ParkingSpace, ParkingRecord

class ParkingService:
    @staticmethod
    def calculate_dynamic_hourly_rate(location_id):
        """
        Dynamic Surge Pricing Formula for Municipal Parking Lots.
        Base Rate: $2.50 / hr.
        Surge: Up to 2.5x when occupancy exceeds 85%.
        """
        loc = ParkingLocation.query.get(location_id)
        if not loc:
            return 2.50

        occupancy_rate = (loc.occupied_spaces / loc.total_capacity) if loc.total_capacity else 0.0
        base_rate = 2.50

        if occupancy_rate >= 0.90:
            multiplier = 2.5
        elif occupancy_rate >= 0.75:
            multiplier = 1.75
        elif occupancy_rate >= 0.50:
            multiplier = 1.25
        else:
            multiplier = 1.0

        dynamic_rate = round(base_rate * multiplier, 2)
        loc.hourly_rate = dynamic_rate
        db.session.commit()

        return {
            "location_code": loc.location_code,
            "occupancy_rate_percent": round(occupancy_rate * 100, 1),
            "dynamic_hourly_rate": dynamic_rate,
            "pricing_surge_multiplier": multiplier
        }
