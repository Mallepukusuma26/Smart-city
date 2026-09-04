"""
Notification and Announcement Models.
"""
from datetime import datetime
from .user import db

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(50), default="GENERAL")  # COMPLAINT, ALERT, ANNOUNCEMENT, SYSTEM
    target_role = db.Column(db.String(30), nullable=True)  # CITIZEN, OFFICER, ADMIN, ALL
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_notifications = db.relationship("UserNotification", back_populates="notification", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "notification_type": self.notification_type,
            "target_role": self.target_role,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class UserNotification(db.Model):
    __tablename__ = "user_notifications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    notification_id = db.Column(db.Integer, db.ForeignKey("notifications.id", ondelete="CASCADE"), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    read_at = db.Column(db.DateTime, nullable=True)
    received_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="notifications")
    notification = db.relationship("Notification", back_populates="user_notifications")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "notification_id": self.notification_id,
            "title": self.notification.title if self.notification else None,
            "message": self.notification.message if self.notification else None,
            "notification_type": self.notification.notification_type if self.notification else "GENERAL",
            "is_read": self.is_read,
            "read_at": self.read_at.isoformat() if self.read_at else None,
            "received_at": self.received_at.isoformat() if self.received_at else None,
        }
