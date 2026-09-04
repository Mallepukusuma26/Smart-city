"""
Extended ORM Models for Municipal Department Structure & Roles.
"""
from datetime import datetime
from .user import db

class DeptStructureExtRecord1(db.Model):
    __tablename__ = "dept_structure_ext_records_1"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord2(db.Model):
    __tablename__ = "dept_structure_ext_records_2"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord3(db.Model):
    __tablename__ = "dept_structure_ext_records_3"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord4(db.Model):
    __tablename__ = "dept_structure_ext_records_4"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord5(db.Model):
    __tablename__ = "dept_structure_ext_records_5"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord6(db.Model):
    __tablename__ = "dept_structure_ext_records_6"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord7(db.Model):
    __tablename__ = "dept_structure_ext_records_7"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord8(db.Model):
    __tablename__ = "dept_structure_ext_records_8"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord9(db.Model):
    __tablename__ = "dept_structure_ext_records_9"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord10(db.Model):
    __tablename__ = "dept_structure_ext_records_10"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord11(db.Model):
    __tablename__ = "dept_structure_ext_records_11"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord12(db.Model):
    __tablename__ = "dept_structure_ext_records_12"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord13(db.Model):
    __tablename__ = "dept_structure_ext_records_13"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord14(db.Model):
    __tablename__ = "dept_structure_ext_records_14"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord15(db.Model):
    __tablename__ = "dept_structure_ext_records_15"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord16(db.Model):
    __tablename__ = "dept_structure_ext_records_16"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord17(db.Model):
    __tablename__ = "dept_structure_ext_records_17"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord18(db.Model):
    __tablename__ = "dept_structure_ext_records_18"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord19(db.Model):
    __tablename__ = "dept_structure_ext_records_19"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord20(db.Model):
    __tablename__ = "dept_structure_ext_records_20"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord21(db.Model):
    __tablename__ = "dept_structure_ext_records_21"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord22(db.Model):
    __tablename__ = "dept_structure_ext_records_22"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord23(db.Model):
    __tablename__ = "dept_structure_ext_records_23"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord24(db.Model):
    __tablename__ = "dept_structure_ext_records_24"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord25(db.Model):
    __tablename__ = "dept_structure_ext_records_25"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord26(db.Model):
    __tablename__ = "dept_structure_ext_records_26"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord27(db.Model):
    __tablename__ = "dept_structure_ext_records_27"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord28(db.Model):
    __tablename__ = "dept_structure_ext_records_28"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord29(db.Model):
    __tablename__ = "dept_structure_ext_records_29"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord30(db.Model):
    __tablename__ = "dept_structure_ext_records_30"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord31(db.Model):
    __tablename__ = "dept_structure_ext_records_31"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord32(db.Model):
    __tablename__ = "dept_structure_ext_records_32"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord33(db.Model):
    __tablename__ = "dept_structure_ext_records_33"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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

class DeptStructureExtRecord34(db.Model):
    __tablename__ = "dept_structure_ext_records_34"

    id = db.Column(db.Integer, primary_key=True)
    ext_code = db.Column(db.String(50), unique=True, nullable=False, index=True)
    title = db.Column(db.String(150), nullable=False)
    domain_tag = db.Column(db.String(50), default="DEPARTMENTS", index=True)
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
