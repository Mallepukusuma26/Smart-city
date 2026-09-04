"""
Data Access Repository for Analytics.
"""
from .base_repository import BaseRepository
from ..models.analytics_module import AnalyticsEntity

class AnalyticsExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(AnalyticsEntity)

    def get_by_zone(self, zone):
        return AnalyticsEntity.query.filter_by(zone=zone).all()
