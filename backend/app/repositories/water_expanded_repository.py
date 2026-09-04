"""
Data Access Repository for Water.
"""
from .base_repository import BaseRepository
from ..models.water_module import WaterEntity

class WaterExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(WaterEntity)

    def get_by_zone(self, zone):
        return WaterEntity.query.filter_by(zone=zone).all()
