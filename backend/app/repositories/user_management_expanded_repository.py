"""
Data Access Repository for User_Management.
"""
from .base_repository import BaseRepository
from ..models.user_management_module import UserManagementEntity

class UserManagementExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserManagementEntity)

    def get_by_zone(self, zone):
        return UserManagementEntity.query.filter_by(zone=zone).all()
