"""
Extended ORM Models for City Asset Maintenance & Depreciation.
"""
from datetime import datetime
from .user import db

class CityAssetsTrackingExtRecord1(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_1"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord2(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_2"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord3(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_3"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord4(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_4"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord5(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_5"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord6(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_6"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord7(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_7"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord8(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_8"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord9(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_9"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord10(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_10"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord11(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_11"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord12(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_12"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord13(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_13"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord14(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_14"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord15(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_15"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord16(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_16"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord17(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_17"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord18(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_18"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord19(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_19"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord20(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_20"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord21(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_21"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord22(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_22"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord23(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_23"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord24(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_24"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord25(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_25"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord26(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_26"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord27(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_27"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord28(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_28"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord29(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_29"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord30(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_30"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord31(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_31"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord32(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_32"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord33(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_33"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

class CityAssetsTrackingExtRecord34(db.Model):
    __tablename__ = "city_assets_tracking_ext_records_34"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="ASSETS", index=True)
    zone = db.Column(db.String(80), nullable=False, index=True, default="Central Zone")
    status = db.Column(db.String(50), default="ACTIVE", index=True)
    score_alpha = db.Column(db.Float, default=100.0)
    score_beta = db.Column(db.Float, default=50.0)
    score_gamma = db.Column(db.Float, default=25.0)
    score_delta = db.Column(db.Float, default=10.0)
    notes = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "ext_code": self.ext_code,
            "title": self.title,
            "domain_tag": self.domain_tag,
            "zone": self.zone,
            "status": self.status,
            "score_alpha": self.score_alpha,
            "score_beta": self.score_beta,
            "score_gamma": self.score_gamma,
            "score_delta": self.score_delta,
            "notes": self.notes,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
