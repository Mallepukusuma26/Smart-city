"""
Public Transport Transit Performance Service.
"""
from ..models import db, TransportRoute, TransportVehicle, PassengerRecord

class TransportService:
    @staticmethod
    def calculate_route_delay_index(route_id):
        vehicles = TransportVehicle.query.filter_by(route_id=route_id).all()
        if not vehicles:
            return {"average_delay_minutes": 0, "status": "ON_TIME"}

        avg_delay = sum(v.delay_minutes for v in vehicles) / len(vehicles)
        avg_delay = round(avg_delay, 1)

        if avg_delay >= 15.0:
            status = "SEVERE_DELAYS"
        elif avg_delay >= 5.0:
            status = "MINOR_DELAYS"
        else:
            status = "ON_TIME"

        return {
            "route_id": route_id,
            "active_vehicles_count": len(vehicles),
            "average_delay_minutes": avg_delay,
            "route_transit_status": status
        }
