"""
Data Access Repository for Pollution.
"""
from .base_repository import BaseRepository
from ..models.pollution_module import PollutionEntity

class PollutionExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(PollutionEntity)

    def get_by_zone(self, zone):
        return PollutionEntity.query.filter_by(zone=zone).all()
