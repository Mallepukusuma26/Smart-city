"""
Waste Management Database Models.
"""
from datetime import datetime
from .user import db

class WasteBin(db.Model):
    __tablename__ = "waste_bins"

    id = db.Column(db.Integer, primary_key=True)
    bin_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    location_name = db.Column(db.String(150), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    capacity_liters = db.Column(db.Float, default=1000.0)
    current_fill_level = db.Column(db.Float, default=0.0)  # Percentage 0.0 - 100.0
    waste_type = db.Column(db.String(50), default="General")  # Organic, Recyclable, Hazardous, General
    status = db.Column(db.String(50), default="NORMAL")  # NORMAL, FULL, OVERFLOW_RISK, OUT_OF_SERVICE
    last_emptied_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    waste_records = db.relationship("WasteRecord", back_populates="waste_bin", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "bin_code": self.bin_code,
            "location_name": self.location_name,
            "zone": self.zone,
            "capacity_liters": self.capacity_liters,
            "current_fill_level": self.current_fill_level,
            "waste_type": self.waste_type,
            "status": self.status,
            "last_emptied_at": self.last_emptied_at.isoformat() if self.last_emptied_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class WasteVehicle(db.Model):
    __tablename__ = "waste_vehicles"

    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    driver_name = db.Column(db.String(100), nullable=False)
    driver_phone = db.Column(db.String(30), nullable=True)
    assigned_zone = db.Column(db.String(80), nullable=False)
    capacity_tons = db.Column(db.Float, default=10.0)
    status = db.Column(db.String(50), default="AVAILABLE")  # AVAILABLE, ON_ROUTE, MAINTENANCE
    last_maintenance = db.Column(db.DateTime, default=datetime.utcnow)

    schedules = db.relationship("CollectionSchedule", back_populates="vehicle", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_number": self.vehicle_number,
            "driver_name": self.driver_name,
            "driver_phone": self.driver_phone,
            "assigned_zone": self.assigned_zone,
            "capacity_tons": self.capacity_tons,
            "status": self.status,
            "last_maintenance": self.last_maintenance.isoformat() if self.last_maintenance else None,
        }


class WasteRecord(db.Model):
    __tablename__ = "waste_records"

    id = db.Column(db.Integer, primary_key=True)
    waste_bin_id = db.Column(db.Integer, db.ForeignKey("waste_bins.id", ondelete="CASCADE"), nullable=False, index=True)
    fill_level_percent = db.Column(db.Float, nullable=False)
    waste_weight_kg = db.Column(db.Float, nullable=False)
    temperature_celsius = db.Column(db.Float, default=25.0)
    methane_level_ppm = db.Column(db.Float, default=5.0)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    waste_bin = db.relationship("WasteBin", back_populates="waste_records")

    def to_dict(self):
        return {
            "id": self.id,
            "waste_bin_id": self.waste_bin_id,
            "bin_code": self.waste_bin.bin_code if self.waste_bin else None,
            "zone": self.waste_bin.zone if self.waste_bin else None,
            "fill_level_percent": self.fill_level_percent,
            "waste_weight_kg": self.waste_weight_kg,
            "temperature_celsius": self.temperature_celsius,
            "methane_level_ppm": self.methane_level_ppm,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }


class CollectionSchedule(db.Model):
    __tablename__ = "collection_schedules"

    id = db.Column(db.Integer, primary_key=True)
    schedule_code = db.Column(db.String(50), unique=True, nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("waste_vehicles.id", ondelete="CASCADE"), nullable=False)
    target_zone = db.Column(db.String(80), nullable=False)
    collection_date = db.Column(db.String(20), nullable=False)  # YYYY-MM-DD
    time_slot = db.Column(db.String(50), default="Morning (08:00 - 12:00)")
    status = db.Column(db.String(50), default="SCHEDULED")  # SCHEDULED, IN_PROGRESS, COMPLETED, CANCELLED

    vehicle = db.relationship("WasteVehicle", back_populates="schedules")

    def to_dict(self):
        return {
            "id": self.id,
            "schedule_code": self.schedule_code,
            "vehicle_id": self.vehicle_id,
            "vehicle_number": self.vehicle.vehicle_number if self.vehicle else None,
            "driver_name": self.vehicle.driver_name if self.vehicle else None,
            "target_zone": self.target_zone,
            "collection_date": self.collection_date,
            "time_slot": self.time_slot,
            "status": self.status,
        }
