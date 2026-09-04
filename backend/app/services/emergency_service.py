"""
Emergency Dispatch & Haversine Distance Minimization Service.
"""
import math
from datetime import datetime
from ..models import db, EmergencyIncident

class EmergencyService:
    @staticmethod
    def haversine_distance_km(lat1, lon1, lat2, lon2):
        """Calculates distance between two coordinates in kilometers using Haversine formula."""
        R = 6371.0 # Earth radius km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2.0)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(R * c, 2)

    @staticmethod
    def dispatch_response_team(incident_id, team_name="Quick Response Force #1"):
        inc = EmergencyIncident.query.get(incident_id)
        if not inc:
            return False

        inc.status = "DISPATCHED"
        inc.assigned_team = team_name
        inc.dispatched_at = datetime.utcnow()
        db.session.commit()
        return True
