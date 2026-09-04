"""
Deep ORM Model Definitions for Environmental Air Quality & AQI Stations.
"""
from datetime import datetime
from .user import db

class AirQualityRecord1(db.Model):
    __tablename__ = "air_quality_records_1"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord2(db.Model):
    __tablename__ = "air_quality_records_2"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord3(db.Model):
    __tablename__ = "air_quality_records_3"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord4(db.Model):
    __tablename__ = "air_quality_records_4"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord5(db.Model):
    __tablename__ = "air_quality_records_5"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord6(db.Model):
    __tablename__ = "air_quality_records_6"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord7(db.Model):
    __tablename__ = "air_quality_records_7"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord8(db.Model):
    __tablename__ = "air_quality_records_8"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord9(db.Model):
    __tablename__ = "air_quality_records_9"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord10(db.Model):
    __tablename__ = "air_quality_records_10"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord11(db.Model):
    __tablename__ = "air_quality_records_11"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord12(db.Model):
    __tablename__ = "air_quality_records_12"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord13(db.Model):
    __tablename__ = "air_quality_records_13"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord14(db.Model):
    __tablename__ = "air_quality_records_14"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord15(db.Model):
    __tablename__ = "air_quality_records_15"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord16(db.Model):
    __tablename__ = "air_quality_records_16"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord17(db.Model):
    __tablename__ = "air_quality_records_17"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord18(db.Model):
    __tablename__ = "air_quality_records_18"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord19(db.Model):
    __tablename__ = "air_quality_records_19"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord20(db.Model):
    __tablename__ = "air_quality_records_20"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord21(db.Model):
    __tablename__ = "air_quality_records_21"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord22(db.Model):
    __tablename__ = "air_quality_records_22"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord23(db.Model):
    __tablename__ = "air_quality_records_23"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord24(db.Model):
    __tablename__ = "air_quality_records_24"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord25(db.Model):
    __tablename__ = "air_quality_records_25"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord26(db.Model):
    __tablename__ = "air_quality_records_26"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord27(db.Model):
    __tablename__ = "air_quality_records_27"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord28(db.Model):
    __tablename__ = "air_quality_records_28"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class AirQualityRecord29(db.Model):
    __tablename__ = "air_quality_records_29"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="POLLUTION", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    param_score_a = db.Column(db.Float, default=100.0)
    param_score_b = db.Column(db.Float, default=50.0)
    param_score_c = db.Column(db.Float, default=25.0)
    param_score_d = db.Column(db.Float, default=10.0)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "record_code": self.record_code,
            "title": self.title,
            "module_tag": self.module_tag,
            "zone": self.zone,
            "status": self.status,
            "param_score_a": self.param_score_a,
            "param_score_b": self.param_score_b,
            "param_score_c": self.param_score_c,
            "param_score_d": self.param_score_d,
            "description": self.description,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
