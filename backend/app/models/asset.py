"""
City Infrastructure Asset Database Models.
"""
from datetime import datetime
from .user import db

class CityAsset(db.Model):
    __tablename__ = "city_assets"

    id = db.Column(db.Integer, primary_key=True)
    asset_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(80), nullable=False, index=True)  # Signal, Bin, Pipe, Transformer, Bus, Camera
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    zone = db.Column(db.String(80), nullable=False)
    installation_date = db.Column(db.String(20), nullable=True)
    estimated_lifespan_years = db.Column(db.Integer, default=10)
    current_condition = db.Column(db.String(50), default="EXCELLENT")  # EXCELLENT, GOOD, FAIR, POOR, CRITICAL
    valuation_usd = db.Column(db.Float, default=5000.0)
    status = db.Column(db.String(50), default="ACTIVE")  # ACTIVE, MAINTENANCE, DECOMMISSIONED
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    department = db.relationship("Department")
    maintenance_records = db.relationship("MaintenanceRecord", back_populates="asset", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "asset_code": self.asset_code,
            "name": self.name,
            "category": self.category,
            "department_id": self.department_id,
            "department_name": self.department.name if self.department else None,
            "zone": self.zone,
            "installation_date": self.installation_date,
            "estimated_lifespan_years": self.estimated_lifespan_years,
            "current_condition": self.current_condition,
            "valuation_usd": self.valuation_usd,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class MaintenanceRecord(db.Model):
    __tablename__ = "maintenance_records"

    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey("city_assets.id", ondelete="CASCADE"), nullable=False)
    work_order_number = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost_usd = db.Column(db.Float, default=150.0)
    performed_by = db.Column(db.String(100), default="Maintenance Team A")
    performed_at = db.Column(db.DateTime, default=datetime.utcnow)

    asset = db.relationship("CityAsset", back_populates="maintenance_records")

    def to_dict(self):
        return {
            "id": self.id,
            "asset_id": self.asset_id,
            "asset_code": self.asset.asset_code if self.asset else None,
            "asset_name": self.asset.name if self.asset else None,
            "work_order_number": self.work_order_number,
            "description": self.description,
            "cost_usd": self.cost_usd,
            "performed_by": self.performed_by,
            "performed_at": self.performed_at.isoformat() if self.performed_at else None,
        }
