"""
Deep ORM Model Definitions for Enterprise PDF CSV Reporting Engine.
"""
from datetime import datetime
from .user import db

class ReportBuilderRecord1(db.Model):
    __tablename__ = "report_builder_records_1"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord2(db.Model):
    __tablename__ = "report_builder_records_2"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord3(db.Model):
    __tablename__ = "report_builder_records_3"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord4(db.Model):
    __tablename__ = "report_builder_records_4"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord5(db.Model):
    __tablename__ = "report_builder_records_5"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord6(db.Model):
    __tablename__ = "report_builder_records_6"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord7(db.Model):
    __tablename__ = "report_builder_records_7"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord8(db.Model):
    __tablename__ = "report_builder_records_8"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord9(db.Model):
    __tablename__ = "report_builder_records_9"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord10(db.Model):
    __tablename__ = "report_builder_records_10"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord11(db.Model):
    __tablename__ = "report_builder_records_11"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord12(db.Model):
    __tablename__ = "report_builder_records_12"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord13(db.Model):
    __tablename__ = "report_builder_records_13"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord14(db.Model):
    __tablename__ = "report_builder_records_14"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord15(db.Model):
    __tablename__ = "report_builder_records_15"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord16(db.Model):
    __tablename__ = "report_builder_records_16"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord17(db.Model):
    __tablename__ = "report_builder_records_17"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord18(db.Model):
    __tablename__ = "report_builder_records_18"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord19(db.Model):
    __tablename__ = "report_builder_records_19"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord20(db.Model):
    __tablename__ = "report_builder_records_20"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord21(db.Model):
    __tablename__ = "report_builder_records_21"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord22(db.Model):
    __tablename__ = "report_builder_records_22"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord23(db.Model):
    __tablename__ = "report_builder_records_23"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord24(db.Model):
    __tablename__ = "report_builder_records_24"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord25(db.Model):
    __tablename__ = "report_builder_records_25"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord26(db.Model):
    __tablename__ = "report_builder_records_26"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord27(db.Model):
    __tablename__ = "report_builder_records_27"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord28(db.Model):
    __tablename__ = "report_builder_records_28"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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

class ReportBuilderRecord29(db.Model):
    __tablename__ = "report_builder_records_29"

    id = db.Column(db.Integer, primary_key=True)
    record_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    module_tag = db.Column(db.String(50), default="REPORTS", index=True)
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
