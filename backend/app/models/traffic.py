"""
Traffic Management Database Models.
"""
from datetime import datetime
from .user import db

class Road(db.Model):
    __tablename__ = "roads"

    id = db.Column(db.Integer, primary_key=True)
    road_name = db.Column(db.String(150), nullable=False, index=True)
    road_code = db.Column(db.String(50), unique=True, nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    length_km = db.Column(db.Float, nullable=False)
    speed_limit = db.Column(db.Integer, default=60)
    lanes_count = db.Column(db.Integer, default=4)
    road_type = db.Column(db.String(50), default="Arterial")  # Highway, Arterial, Residential
    status = db.Column(db.String(50), default="OPERATIONAL")  # OPERATIONAL, MAINTENANCE, BLOCKED
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    signals = db.relationship("TrafficSignal", back_populates="road", cascade="all, delete-orphan")
    traffic_records = db.relationship("TrafficRecord", back_populates="road", cascade="all, delete-orphan")
    incidents = db.relationship("TrafficIncident", back_populates="road", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "road_name": self.road_name,
            "road_code": self.road_code,
            "zone": self.zone,
            "length_km": self.length_km,
            "speed_limit": self.speed_limit,
            "lanes_count": self.lanes_count,
            "road_type": self.road_type,
            "status": self.status,
        }


class TrafficSignal(db.Model):
    __tablename__ = "traffic_signals"

    id = db.Column(db.Integer, primary_key=True)
    signal_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    road_id = db.Column(db.Integer, db.ForeignKey("roads.id", ondelete="CASCADE"), nullable=False)
    intersection_name = db.Column(db.String(150), nullable=False)
    state = db.Column(db.String(20), default="RED")  # RED, GREEN, YELLOW, FLASHING
    is_smart_mode = db.Column(db.Boolean, default=True)
    green_duration_sec = db.Column(db.Integer, default=45)
    red_duration_sec = db.Column(db.Integer, default=45)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    road = db.relationship("Road", back_populates="signals")

    def to_dict(self):
        return {
            "id": self.id,
            "signal_code": self.signal_code,
            "road_id": self.road_id,
            "road_name": self.road.road_name if self.road else None,
            "intersection_name": self.intersection_name,
            "state": self.state,
            "is_smart_mode": self.is_smart_mode,
            "green_duration_sec": self.green_duration_sec,
            "red_duration_sec": self.red_duration_sec,
            "last_updated": self.last_updated.isoformat() if self.last_updated else None,
        }


class TrafficRecord(db.Model):
    __tablename__ = "traffic_records"

    id = db.Column(db.Integer, primary_key=True)
    road_id = db.Column(db.Integer, db.ForeignKey("roads.id", ondelete="CASCADE"), nullable=False, index=True)
    vehicle_count = db.Column(db.Integer, nullable=False)
    average_speed_kmh = db.Column(db.Float, nullable=False)
    congestion_level = db.Column(db.String(50), nullable=False)  # LOW, MODERATE, HIGH, SEVERE
    congestion_index = db.Column(db.Float, nullable=False)  # 0.0 to 10.0 scale
    peak_hour = db.Column(db.Boolean, default=False)
    weather_condition = db.Column(db.String(50), default="Clear")
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    road = db.relationship("Road", back_populates="traffic_records")

    def to_dict(self):
        return {
            "id": self.id,
            "road_id": self.road_id,
            "road_name": self.road.road_name if self.road else None,
            "zone": self.road.zone if self.road else None,
            "vehicle_count": self.vehicle_count,
            "average_speed_kmh": self.average_speed_kmh,
            "congestion_level": self.congestion_level,
            "congestion_index": self.congestion_index,
            "peak_hour": self.peak_hour,
            "weather_condition": self.weather_condition,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }


class TrafficIncident(db.Model):
    __tablename__ = "traffic_incidents"

    id = db.Column(db.Integer, primary_key=True)
    incident_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    road_id = db.Column(db.Integer, db.ForeignKey("roads.id", ondelete="CASCADE"), nullable=False)
    incident_type = db.Column(db.String(50), nullable=False)  # ACCIDENT, ROADWORK, VEHICLE_BREAKDOWN, SIGNAL_FAILURE
    severity = db.Column(db.String(20), default="HIGH")  # LOW, MEDIUM, HIGH, CRITICAL
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default="OPEN")  # OPEN, IN_PROGRESS, RESOLVED, CLOSED
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)

    road = db.relationship("Road", back_populates="incidents")

    def to_dict(self):
        return {
            "id": self.id,
            "incident_code": self.incident_code,
            "road_id": self.road_id,
            "road_name": self.road.road_name if self.road else None,
            "incident_type": self.incident_type,
            "severity": self.severity,
            "description": self.description,
            "status": self.status,
            "reported_at": self.reported_at.isoformat() if self.reported_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
        }
