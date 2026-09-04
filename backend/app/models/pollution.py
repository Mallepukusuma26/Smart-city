"""
Environmental & Pollution Monitoring Database Models.
"""
from datetime import datetime
from .user import db
from ..config.constants import AQIRatings

class PollutionStation(db.Model):
    __tablename__ = "pollution_stations"

    id = db.Column(db.Integer, primary_key=True)
    station_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    station_name = db.Column(db.String(150), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    records = db.relationship("PollutionRecord", back_populates="station", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "station_code": self.station_code,
            "station_name": self.station_name,
            "zone": self.zone,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "is_active": self.is_active,
        }


class PollutionRecord(db.Model):
    __tablename__ = "pollution_records"

    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey("pollution_stations.id", ondelete="CASCADE"), nullable=False, index=True)
    aqi = db.Column(db.Float, nullable=False)
    pm2_5 = db.Column(db.Float, nullable=False)  # ug/m3
    pm10 = db.Column(db.Float, nullable=False)   # ug/m3
    co = db.Column(db.Float, nullable=False)     # mg/m3
    no2 = db.Column(db.Float, nullable=False)    # ug/m3
    so2 = db.Column(db.Float, nullable=False)    # ug/m3
    o3 = db.Column(db.Float, nullable=False)     # ug/m3
    temperature_c = db.Column(db.Float, default=28.0)
    humidity_percent = db.Column(db.Float, default=55.0)
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    station = db.relationship("PollutionStation", back_populates="records")

    def to_dict(self):
        min_val, max_val, category, color = AQIRatings.get_rating(self.aqi)
        return {
            "id": self.id,
            "station_id": self.station_id,
            "station_name": self.station.station_name if self.station else None,
            "zone": self.station.zone if self.station else None,
            "aqi": self.aqi,
            "aqi_category": category,
            "aqi_color": color,
            "pm2_5": self.pm2_5,
            "pm10": self.pm10,
            "co": self.co,
            "no2": self.no2,
            "so2": self.so2,
            "o3": self.o3,
            "temperature_c": self.temperature_c,
            "humidity_percent": self.humidity_percent,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None,
        }
