"""
Data Access Repository for Traffic.
"""
from .base_repository import BaseRepository
from ..models.traffic_module import TrafficEntity

class TrafficExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(TrafficEntity)

    def get_by_zone(self, zone):
        return TrafficEntity.query.filter_by(zone=zone).all()
