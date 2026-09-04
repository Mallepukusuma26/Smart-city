"""
Data Access Repository for Report.
"""
from .base_repository import BaseRepository
from ..models.report_module import ReportEntity

class ReportExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(ReportEntity)

    def get_by_zone(self, zone):
        return ReportEntity.query.filter_by(zone=zone).all()
