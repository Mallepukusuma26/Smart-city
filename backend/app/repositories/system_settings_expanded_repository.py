"""
Data Access Repository for System_Settings.
"""
from .base_repository import BaseRepository
from ..models.system_settings_module import SystemSettingsEntity

class SystemSettingsExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(SystemSettingsEntity)

    def get_by_zone(self, zone):
        return SystemSettingsEntity.query.filter_by(zone=zone).all()
