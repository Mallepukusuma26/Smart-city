"""
Data Access Repository for Asset.
"""
from .base_repository import BaseRepository
from ..models.asset_module import AssetEntity

class AssetExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(AssetEntity)

    def get_by_zone(self, zone):
        return AssetEntity.query.filter_by(zone=zone).all()
