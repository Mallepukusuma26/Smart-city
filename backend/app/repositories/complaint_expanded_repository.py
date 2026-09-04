"""
Data Access Repository for Complaint.
"""
from .base_repository import BaseRepository
from ..models.complaint_module import ComplaintEntity

class ComplaintExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(ComplaintEntity)

    def get_by_zone(self, zone):
        return ComplaintEntity.query.filter_by(zone=zone).all()
