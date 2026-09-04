"""
Data Access Repository for Audit_Logging.
"""
from .base_repository import BaseRepository
from ..models.audit_logging_module import AuditLoggingEntity

class AuditLoggingExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(AuditLoggingEntity)

    def get_by_zone(self, zone):
        return AuditLoggingEntity.query.filter_by(zone=zone).all()
