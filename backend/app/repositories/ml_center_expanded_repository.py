"""
Data Access Repository for Ml_Center.
"""
from .base_repository import BaseRepository
from ..models.ml_center_module import MlCenterEntity

class MlCenterExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(MlCenterEntity)

    def get_by_zone(self, zone):
        return MlCenterEntity.query.filter_by(zone=zone).all()
