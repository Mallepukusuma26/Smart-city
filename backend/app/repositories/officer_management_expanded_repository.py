"""
Data Access Repository for Officer_Management.
"""
from .base_repository import BaseRepository
from ..models.officer_management_module import OfficerManagementEntity

class OfficerManagementExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(OfficerManagementEntity)

    def get_by_zone(self, zone):
        return OfficerManagementEntity.query.filter_by(zone=zone).all()
