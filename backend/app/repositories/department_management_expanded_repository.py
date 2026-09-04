"""
Data Access Repository for Department_Management.
"""
from .base_repository import BaseRepository
from ..models.department_management_module import DepartmentManagementEntity

class DepartmentManagementExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(DepartmentManagementEntity)

    def get_by_zone(self, zone):
        return DepartmentManagementEntity.query.filter_by(zone=zone).all()
