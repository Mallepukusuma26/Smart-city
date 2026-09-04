"""
Data Access Repository for Notification.
"""
from .base_repository import BaseRepository
from ..models.notification_module import NotificationEntity

class NotificationExpandedRepository(BaseRepository):
    def __init__(self):
        super().__init__(NotificationEntity)

    def get_by_zone(self, zone):
        return NotificationEntity.query.filter_by(zone=zone).all()
