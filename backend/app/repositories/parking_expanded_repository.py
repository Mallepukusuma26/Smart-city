"""
Data Access Repository for Parking.
"""
from .base_repository import BaseRepository
from ..models.parking_module import ParkingEntity

class ParkingExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(ParkingEntity)

    def get_by_zone(self, zone):
        return ParkingEntity.query.filter_by(zone=zone).all()
