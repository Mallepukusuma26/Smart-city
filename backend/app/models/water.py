"""
Water Management Database Models.
"""
from datetime import datetime
from .user import db

class WaterTank(db.Model):
    __tablename__ = "water_tanks"

    id = db.Column(db.Integer, primary_key=True)
    tank_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(150), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    capacity_liters = db.Column(db.Float, nullable=False)
    current_level_liters = db.Column(db.Float, nullable=False)
    water_quality_ph = db.Column(db.Float, default=7.2)
    turbidity_ntu = db.Column(db.Float, default=1.5)
    status = db.Column(db.String(50), default="OPERATIONAL")  # OPERATIONAL, MAINTENANCE, CRITICAL_LOW
    last_cleaned = db.Column(db.DateTime, default=datetime.utcnow)

    water_records = db.relationship("WaterRecord", back_populates="water_tank", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "tank_code": self.tank_code,
            "name": self.name,
            "zone": self.zone,
            "capacity_liters": self.capacity_liters,
            "current_level_liters": self.current_level_liters,
            "fill_percentage": round((self.current_level_liters / self.capacity_liters) * 100, 2) if self.capacity_liters else 0,
            "water_quality_ph": self.water_quality_ph,
            "turbidity_ntu": self.turbidity_ntu,
            "status": self.status,
            "last_cleaned": self.last_cleaned.isoformat() if self.last_cleaned else None,
        }


class WaterPipeline(db.Model):
    __tablename__ = "water_pipelines"

    id = db.Column(db.Integer, primary_key=True)
    pipeline_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    zone = db.Column(db.String(80), nullable=False)
    diameter_mm = db.Column(db.Integer, default=500)
    material = db.Column(db.String(50), default="Ductile Iron")
    length_meters = db.Column(db.Float, default=1500.0)
    normal_pressure_bar = db.Column(db.Float, default=4.5)
    status = db.Column(db.String(50), default="HEALTHY")  # HEALTHY, LEAKAGE_DETECTED, REPAIR_NEEDED

    leakages = db.relationship("WaterLeakage", back_populates="pipeline", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "pipeline_code": self.pipeline_code,
            "zone": self.zone,
            "diameter_mm": self.diameter_mm,
            "material": self.material,
            "length_meters": self.length_meters,
            "normal_pressure_bar": self.normal_pressure_bar,
            "status": self.status,
        }


class WaterRecord(db.Model):
    __tablename__ = "water_records"

    id = db.Column(db.Integer, primary_key=True)
    water_tank_id = db.Column(db.Integer, db.ForeignKey("water_tanks.id", ondelete="CASCADE"), nullable=False, index=True)
    flow_rate_lps = db.Column(db.Float, nullable=False)  # liters per second
    consumption_liters = db.Column(db.Float, nullable=False)
    pressure_bar = db.Column(db.Float, nullable=False)
    chlorine_ppm = db.Column(db.Float, default=0.5)
    ph_level = db.Column(db.Float, default=7.2)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    water_tank = db.relationship("WaterTank", back_populates="water_records")

    def to_dict(self):
        return {
            "id": self.id,
            "water_tank_id": self.water_tank_id,
            "tank_code": self.water_tank.tank_code if self.water_tank else None,
            "zone": self.water_tank.zone if self.water_tank else None,
            "flow_rate_lps": self.flow_rate_lps,
            "consumption_liters": self.consumption_liters,
            "pressure_bar": self.pressure_bar,
            "chlorine_ppm": self.chlorine_ppm,
            "ph_level": self.ph_level,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }


class WaterLeakage(db.Model):
    __tablename__ = "water_leakages"

    id = db.Column(db.Integer, primary_key=True)
    leakage_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    pipeline_id = db.Column(db.Integer, db.ForeignKey("water_pipelines.id", ondelete="CASCADE"), nullable=False)
    severity = db.Column(db.String(20), default="MEDIUM")  # LOW, MEDIUM, HIGH, CRITICAL
    estimated_loss_lps = db.Column(db.Float, default=10.0)
    status = db.Column(db.String(50), default="REPORTED")  # REPORTED, DISPATCHED, REPAIRED, CLOSED
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    repaired_at = db.Column(db.DateTime, nullable=True)

    pipeline = db.relationship("WaterPipeline", back_populates="leakages")

    def to_dict(self):
        return {
            "id": self.id,
            "leakage_code": self.leakage_code,
            "pipeline_id": self.pipeline_id,
            "pipeline_code": self.pipeline.pipeline_code if self.pipeline else None,
            "zone": self.pipeline.zone if self.pipeline else None,
            "severity": self.severity,
            "estimated_loss_lps": self.estimated_loss_lps,
            "status": self.status,
            "reported_at": self.reported_at.isoformat() if self.reported_at else None,
            "repaired_at": self.repaired_at.isoformat() if self.repaired_at else None,
        }
