"""
Data Access Repository for Electricity.
"""
from .base_repository import BaseRepository
from ..models.electricity_module import ElectricityEntity

class ElectricityExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(ElectricityEntity)

    def get_by_zone(self, zone):
        return ElectricityEntity.query.filter_by(zone=zone).all()
