"""
Data Access Repository for Emergency.
"""
from .base_repository import BaseRepository
from ..models.emergency_module import EmergencyEntity

class EmergencyExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(EmergencyEntity)

    def get_by_zone(self, zone):
        return EmergencyEntity.query.filter_by(zone=zone).all()
