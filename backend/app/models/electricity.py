"""
Electricity and Power Grid Database Models.
"""
from datetime import datetime
from .user import db

class Transformer(db.Model):
    __tablename__ = "transformers"

    id = db.Column(db.Integer, primary_key=True)
    transformer_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    zone = db.Column(db.String(80), nullable=False, index=True)
    capacity_kva = db.Column(db.Float, default=500.0)
    current_load_kw = db.Column(db.Float, default=250.0)
    voltage_v = db.Column(db.Float, default=400.0)
    temperature_c = db.Column(db.Float, default=45.0)
    status = db.Column(db.String(50), default="NORMAL")  # NORMAL, OVERLOADED, OVERHEATING, OUTAGE
    last_serviced = db.Column(db.DateTime, default=datetime.utcnow)

    electricity_records = db.relationship("ElectricityRecord", back_populates="transformer", cascade="all, delete-orphan")
    outages = db.relationship("PowerOutage", back_populates="transformer", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "transformer_code": self.transformer_code,
            "zone": self.zone,
            "capacity_kva": self.capacity_kva,
            "current_load_kw": self.current_load_kw,
            "load_percentage": round((self.current_load_kw / self.capacity_kva) * 100, 2) if self.capacity_kva else 0,
            "voltage_v": self.voltage_v,
            "temperature_c": self.temperature_c,
            "status": self.status,
            "last_serviced": self.last_serviced.isoformat() if self.last_serviced else None,
        }


class ElectricityRecord(db.Model):
    __tablename__ = "electricity_records"

    id = db.Column(db.Integer, primary_key=True)
    transformer_id = db.Column(db.Integer, db.ForeignKey("transformers.id", ondelete="CASCADE"), nullable=False, index=True)
    consumption_kwh = db.Column(db.Float, nullable=False)
    peak_demand_kw = db.Column(db.Float, nullable=False)
    power_factor = db.Column(db.Float, default=0.95)
    frequency_hz = db.Column(db.Float, default=50.0)
    is_peak_hour = db.Column(db.Boolean, default=False)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    transformer = db.relationship("Transformer", back_populates="electricity_records")

    def to_dict(self):
        return {
            "id": self.id,
            "transformer_id": self.transformer_id,
            "transformer_code": self.transformer.transformer_code if self.transformer else None,
            "zone": self.transformer.zone if self.transformer else None,
            "consumption_kwh": self.consumption_kwh,
            "peak_demand_kw": self.peak_demand_kw,
            "power_factor": self.power_factor,
            "frequency_hz": self.frequency_hz,
            "is_peak_hour": self.is_peak_hour,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }


class PowerOutage(db.Model):
    __tablename__ = "power_outages"

    id = db.Column(db.Integer, primary_key=True)
    outage_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    transformer_id = db.Column(db.Integer, db.ForeignKey("transformers.id", ondelete="CASCADE"), nullable=False)
    outage_cause = db.Column(db.String(100), default="Transformer Overload")
    affected_customers = db.Column(db.Integer, default=250)
    status = db.Column(db.String(50), default="ACTIVE")  # ACTIVE, REPAIRING, RESOLVED
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)

    transformer = db.relationship("Transformer", back_populates="outages")

    def to_dict(self):
        return {
            "id": self.id,
            "outage_code": self.outage_code,
            "transformer_id": self.transformer_id,
            "transformer_code": self.transformer.transformer_code if self.transformer else None,
            "zone": self.transformer.zone if self.transformer else None,
            "outage_cause": self.outage_cause,
            "affected_customers": self.affected_customers,
            "status": self.status,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
        }
