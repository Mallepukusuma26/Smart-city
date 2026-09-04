"""
Data Access Repository for Waste.
"""
from .base_repository import BaseRepository
from ..models.waste_module import WasteEntity

class WasteExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(WasteEntity)

    def get_by_zone(self, zone):
        return WasteEntity.query.filter_by(zone=zone).all()
