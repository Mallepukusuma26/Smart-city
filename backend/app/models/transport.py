"""
Public Transport Database Models.
"""
from datetime import datetime
from .user import db

class TransportRoute(db.Model):
    __tablename__ = "transport_routes"

    id = db.Column(db.Integer, primary_key=True)
    route_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    route_name = db.Column(db.String(150), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    total_stops = db.Column(db.Integer, default=10)
    distance_km = db.Column(db.Float, default=15.0)
    fare_amount = db.Column(db.Float, default=2.50)
    is_active = db.Column(db.Boolean, default=True)

    vehicles = db.relationship("TransportVehicle", back_populates="route", cascade="all, delete-orphan")
    stops = db.relationship("TransportStop", back_populates="route", cascade="all, delete-orphan")
    passenger_records = db.relationship("PassengerRecord", back_populates="route", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "route_number": self.route_number,
            "route_name": self.route_name,
            "origin": self.origin,
            "destination": self.destination,
            "total_stops": self.total_stops,
            "distance_km": self.distance_km,
            "fare_amount": self.fare_amount,
            "is_active": self.is_active,
        }


class TransportVehicle(db.Model):
    __tablename__ = "transport_vehicles"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    route_id = db.Column(db.Integer, db.ForeignKey("transport_routes.id", ondelete="CASCADE"), nullable=False)
    vehicle_type = db.Column(db.String(50), default="Metro Bus")  # Metro Bus, Electric Bus, Tram
    capacity = db.Column(db.Integer, default=60)
    current_passengers = db.Column(db.Integer, default=0)
    driver_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="ON_TIME")  # ON_TIME, DELAYED, MAINTENANCE, OUT_OF_SERVICE
    delay_minutes = db.Column(db.Integer, default=0)
    last_gps_update = db.Column(db.DateTime, default=datetime.utcnow)

    route = db.relationship("TransportRoute", back_populates="vehicles")

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_code": self.vehicle_code,
            "route_id": self.route_id,
            "route_number": self.route.route_number if self.route else None,
            "vehicle_type": self.vehicle_type,
            "capacity": self.capacity,
            "current_passengers": self.current_passengers,
            "occupancy_rate": round((self.current_passengers / self.capacity) * 100, 2) if self.capacity else 0,
            "driver_name": self.driver_name,
            "status": self.status,
            "delay_minutes": self.delay_minutes,
            "last_gps_update": self.last_gps_update.isoformat() if self.last_gps_update else None,
        }


class TransportStop(db.Model):
    __tablename__ = "transport_stops"

    id = db.Column(db.Integer, primary_key=True)
    stop_code = db.Column(db.String(50), unique=True, nullable=False)
    stop_name = db.Column(db.String(150), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("transport_routes.id", ondelete="CASCADE"), nullable=False)
    stop_sequence = db.Column(db.Integer, nullable=False)
    zone = db.Column(db.String(80), nullable=False)

    route = db.relationship("TransportRoute", back_populates="stops")

    def to_dict(self):
        return {
            "id": self.id,
            "stop_code": self.stop_code,
            "stop_name": self.stop_name,
            "route_id": self.route_id,
            "route_number": self.route.route_number if self.route else None,
            "stop_sequence": self.stop_sequence,
            "zone": self.zone,
        }


class PassengerRecord(db.Model):
    __tablename__ = "passenger_records"

    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey("transport_routes.id", ondelete="CASCADE"), nullable=False, index=True)
    passenger_count = db.Column(db.Integer, nullable=False)
    delay_minutes = db.Column(db.Integer, default=0)
    weather_condition = db.Column(db.String(50), default="Clear")
    is_peak_hour = db.Column(db.Boolean, default=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    route = db.relationship("TransportRoute", back_populates="passenger_records")

    def to_dict(self):
        return {
            "id": self.id,
            "route_id": self.route_id,
            "route_number": self.route.route_number if self.route else None,
            "passenger_count": self.passenger_count,
            "delay_minutes": self.delay_minutes,
            "weather_condition": self.weather_condition,
            "is_peak_hour": self.is_peak_hour,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }
