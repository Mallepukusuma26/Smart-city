"""
Production ORM Entity Models for Transport Management.
"""
from datetime import datetime
from .user import db

class TransportEntity(db.Model):
    __tablename__ = "transport_entities"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(150), nullable=False)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="OPERATIONAL", index=True)
    metric_value_1 = db.Column(db.Float, default=0.0)
    metric_value_2 = db.Column(db.Float, default=0.0)
    metric_value_3 = db.Column(db.Float, default=0.0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "zone": self.zone,
            "status": self.status,
            "metric_value_1": self.metric_value_1,
            "metric_value_2": self.metric_value_2,
            "metric_value_3": self.metric_value_3,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class TransportSubRecord1(db.Model):
    __tablename__ = "transport_sub_records_1"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord2(db.Model):
    __tablename__ = "transport_sub_records_2"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord3(db.Model):
    __tablename__ = "transport_sub_records_3"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord4(db.Model):
    __tablename__ = "transport_sub_records_4"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord5(db.Model):
    __tablename__ = "transport_sub_records_5"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord6(db.Model):
    __tablename__ = "transport_sub_records_6"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord7(db.Model):
    __tablename__ = "transport_sub_records_7"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord8(db.Model):
    __tablename__ = "transport_sub_records_8"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord9(db.Model):
    __tablename__ = "transport_sub_records_9"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord10(db.Model):
    __tablename__ = "transport_sub_records_10"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord11(db.Model):
    __tablename__ = "transport_sub_records_11"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord12(db.Model):
    __tablename__ = "transport_sub_records_12"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord13(db.Model):
    __tablename__ = "transport_sub_records_13"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }

class TransportSubRecord14(db.Model):
    __tablename__ = "transport_sub_records_14"

    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey("transport_entities.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    sensor_reading = db.Column(db.Float, default=0.0)
    quality_score = db.Column(db.Float, default=100.0)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_id": self.entity_id,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "sensor_reading": self.sensor_reading,
            "quality_score": self.quality_score,
            "notes": self.notes
        }
