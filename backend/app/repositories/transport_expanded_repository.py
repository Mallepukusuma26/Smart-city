"""
Data Access Repository for Transport.
"""
from .base_repository import BaseRepository
from ..models.transport_module import TransportEntity

class TransportExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(TransportEntity)

    def get_by_zone(self, zone):
        return TransportEntity.query.filter_by(zone=zone).all()
