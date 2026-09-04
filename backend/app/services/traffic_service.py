"""
Traffic Control, Signal Timing & Congestion Management Domain Service.
"""
import math
from datetime import datetime
from ..models import db, Road, TrafficSignal, TrafficRecord, TrafficIncident
from ..config.constants import SeverityLevels

class TrafficService:
    @staticmethod
    def calculate_optimal_signal_green_time(road_id, vehicle_count, lanes=4, speed_limit=60):
        """
        Dynamic Signal Phase Optimization Algorithm.
        Adjusts green light duration based on real-time vehicle density per lane.
        """
        density_per_lane = vehicle_count / max(1, lanes)
        base_green = 30
        
        # Scaling factor: +1.5 seconds for every 10 vehicles per lane
        calculated_green = base_green + (density_per_lane / 10.0) * 1.5
        
        # Clamp between min 15 sec and max 120 sec
        optimal_green = int(min(120, max(15, calculated_green)))
        optimal_red = max(20, 150 - optimal_green)

        # Update signal in database
        signals = TrafficSignal.query.filter_by(road_id=road_id).all()
        for sig in signals:
            if sig.is_smart_mode:
                sig.green_duration_sec = optimal_green
                sig.red_duration_sec = optimal_red
                sig.last_updated = datetime.utcnow()
        db.session.commit()

        return {
            "road_id": road_id,
            "optimal_green_sec": optimal_green,
            "optimal_red_sec": optimal_red,
            "vehicle_density_per_lane": round(density_per_lane, 1)
        }

    @staticmethod
    def log_traffic_sensor_data(road_id, vehicle_count, avg_speed_kmh, weather="Clear"):
        road = Road.query.get(road_id)
        if not road:
            return None

        # Congestion Index formula: 0.0 to 10.0
        lanes = road.lanes_count or 4
        capacity = lanes * 50.0
        density_ratio = min(2.0, vehicle_count / capacity)
        speed_ratio = max(0.1, avg_speed_kmh / (road.speed_limit or 60.0))
        
        congestion_index = round(min(10.0, max(0.0, (density_ratio * 6.0) + ((1.0 - speed_ratio) * 4.0))), 2)
        
        if congestion_index >= 7.5:
            level = "SEVERE"
        elif congestion_index >= 5.0:
            level = "HIGH"
        elif congestion_index >= 3.0:
            level = "MODERATE"
        else:
            level = "LOW"

        hour = datetime.utcnow().hour
        is_peak = (7 <= hour <= 10 or 17 <= hour <= 20)

        record = TrafficRecord(
            road_id=road_id,
            vehicle_count=vehicle_count,
            average_speed_kmh=avg_speed_kmh,
            congestion_level=level,
            congestion_index=congestion_index,
            peak_hour=is_peak,
            weather_condition=weather
        )
        db.session.add(record)
        db.session.commit()

        # Auto-adjust signals if high congestion
        if congestion_index >= 5.0:
            TrafficService.calculate_optimal_signal_green_time(road_id, vehicle_count, lanes, road.speed_limit)

        return record.to_dict()
