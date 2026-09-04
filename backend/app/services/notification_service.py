"""
Notification Dispatcher Service.
"""
from datetime import datetime
from ..models import db, Notification, UserNotification, User

class NotificationService:
    @staticmethod
    def send_user_notification(user_id, title, message, notification_type="GENERAL"):
        notif = Notification(
            title=title,
            message=message,
            notification_type=notification_type,
            target_role=None,
        )
        db.session.add(notif)
        db.session.flush()

        un = UserNotification(
            user_id=user_id,
            notification_id=notif.id,
            is_read=False,
        )
        db.session.add(un)
        db.session.commit()
        return un

    @staticmethod
    def broadcast_to_role(target_role, title, message, notification_type="ANNOUNCEMENT"):
        notif = Notification(
            title=title,
            message=message,
            notification_type=notification_type,
            target_role=target_role,
        )
        db.session.add(notif)
        db.session.flush()

        users = User.query.all()
        target_users = [u for u in users if target_role in u.roles or target_role == "ALL"]
        for u in target_users:
            un = UserNotification(user_id=u.id, notification_id=notif.id)
            db.session.add(un)
        db.session.commit()
        return len(target_users)
