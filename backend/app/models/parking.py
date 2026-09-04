"""
Parking Management Database Models.
"""
from datetime import datetime
from .user import db

class ParkingLocation(db.Model):
    __tablename__ = "parking_locations"

    id = db.Column(db.Integer, primary_key=True)
    location_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(150), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    total_capacity = db.Column(db.Integer, nullable=False)
    occupied_spaces = db.Column(db.Integer, default=0)
    hourly_rate = db.Column(db.Float, default=2.50)
    is_ev_charging = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(50), default="OPEN")  # OPEN, FULL, CLOSED
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    spaces = db.relationship("ParkingSpace", back_populates="location", cascade="all, delete-orphan")
    records = db.relationship("ParkingRecord", back_populates="location", cascade="all, delete-orphan")

    def to_dict(self):
        available = max(0, self.total_capacity - self.occupied_spaces)
        occupancy_rate = round((self.occupied_spaces / self.total_capacity) * 100, 2) if self.total_capacity else 0.0
        return {
            "id": self.id,
            "location_code": self.location_code,
            "name": self.name,
            "zone": self.zone,
            "total_capacity": self.total_capacity,
            "occupied_spaces": self.occupied_spaces,
            "available_spaces": available,
            "occupancy_rate": occupancy_rate,
            "hourly_rate": self.hourly_rate,
            "is_ev_charging": self.is_ev_charging,
            "status": self.status,
        }


class ParkingSpace(db.Model):
    __tablename__ = "parking_spaces"

    id = db.Column(db.Integer, primary_key=True)
    space_number = db.Column(db.String(50), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("parking_locations.id", ondelete="CASCADE"), nullable=False)
    is_handicapped = db.Column(db.Boolean, default=False)
    is_ev_charger = db.Column(db.Boolean, default=False)
    is_occupied = db.Column(db.Boolean, default=False)
    sensor_id = db.Column(db.String(50), unique=True, nullable=True)

    location = db.relationship("ParkingLocation", back_populates="spaces")

    def to_dict(self):
        return {
            "id": self.id,
            "space_number": self.space_number,
            "location_id": self.location_id,
            "location_name": self.location.name if self.location else None,
            "is_handicapped": self.is_handicapped,
            "is_ev_charger": self.is_ev_charger,
            "is_occupied": self.is_occupied,
            "sensor_id": self.sensor_id,
        }


class ParkingRecord(db.Model):
    __tablename__ = "parking_records"

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("parking_locations.id", ondelete="CASCADE"), nullable=False, index=True)
    occupied_count = db.Column(db.Integer, nullable=False)
    available_count = db.Column(db.Integer, nullable=False)
    occupancy_percentage = db.Column(db.Float, nullable=False)
    turnover_rate = db.Column(db.Float, default=1.2)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    location = db.relationship("ParkingLocation", back_populates="records")

    def to_dict(self):
        return {
            "id": self.id,
            "location_id": self.location_id,
            "location_name": self.location.name if self.location else None,
            "zone": self.location.zone if self.location else None,
            "occupied_count": self.occupied_count,
            "available_count": self.available_count,
            "occupancy_percentage": self.occupancy_percentage,
            "turnover_rate": self.turnover_rate,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }
