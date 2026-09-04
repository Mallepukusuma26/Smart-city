"""
Deep ORM Model Definitions for Electric Power Grid & Substation Distribution.
"""
from datetime import datetime
from .user import db

class PowerGridRecord1(db.Model):
    __tablename__ = "power_grid_records_1"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord2(db.Model):
    __tablename__ = "power_grid_records_2"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord3(db.Model):
    __tablename__ = "power_grid_records_3"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord4(db.Model):
    __tablename__ = "power_grid_records_4"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord5(db.Model):
    __tablename__ = "power_grid_records_5"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord6(db.Model):
    __tablename__ = "power_grid_records_6"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord7(db.Model):
    __tablename__ = "power_grid_records_7"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord8(db.Model):
    __tablename__ = "power_grid_records_8"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord9(db.Model):
    __tablename__ = "power_grid_records_9"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord10(db.Model):
    __tablename__ = "power_grid_records_10"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord11(db.Model):
    __tablename__ = "power_grid_records_11"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord12(db.Model):
    __tablename__ = "power_grid_records_12"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord13(db.Model):
    __tablename__ = "power_grid_records_13"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord14(db.Model):
    __tablename__ = "power_grid_records_14"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord15(db.Model):
    __tablename__ = "power_grid_records_15"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord16(db.Model):
    __tablename__ = "power_grid_records_16"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord17(db.Model):
    __tablename__ = "power_grid_records_17"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord18(db.Model):
    __tablename__ = "power_grid_records_18"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord19(db.Model):
    __tablename__ = "power_grid_records_19"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord20(db.Model):
    __tablename__ = "power_grid_records_20"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord21(db.Model):
    __tablename__ = "power_grid_records_21"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord22(db.Model):
    __tablename__ = "power_grid_records_22"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord23(db.Model):
    __tablename__ = "power_grid_records_23"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord24(db.Model):
    __tablename__ = "power_grid_records_24"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord25(db.Model):
    __tablename__ = "power_grid_records_25"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord26(db.Model):
    __tablename__ = "power_grid_records_26"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord27(db.Model):
    __tablename__ = "power_grid_records_27"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord28(db.Model):
    __tablename__ = "power_grid_records_28"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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

class PowerGridRecord29(db.Model):
    __tablename__ = "power_grid_records_29"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="ELECTRICITY", index=True)
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
