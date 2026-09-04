"""
Data Access Repository for Alert.
"""
from .base_repository import BaseRepository
from ..models.alert_module import AlertEntity

class AlertExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(AlertEntity)

    def get_by_zone(self, zone):
        return AlertEntity.query.filter_by(zone=zone).all()
