"""
Domain-Specific Repository Abstractions for Smart City Operations.
"""
from datetime import datetime
from sqlalchemy import desc, func
from .base_repository import BaseRepository
from ..models import (
    db, User, Role, Department, Officer, Citizen,
    Road, TrafficSignal, TrafficRecord, TrafficIncident,
    WasteBin, WasteVehicle, WasteRecord, CollectionSchedule,
    WaterTank, WaterPipeline, WaterRecord, WaterLeakage,
    Transformer, ElectricityRecord, PowerOutage,
    ParkingLocation, ParkingSpace, ParkingRecord,
    TransportRoute, TransportVehicle, TransportStop, PassengerRecord,
    PollutionStation, PollutionRecord,
    Complaint, ComplaintHistory, EmergencyIncident,
    CityAsset, Notification, UserNotification, AlertRule, SystemAlert, AuditLog
)

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def find_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_users_by_role(self, role_name, page=1, per_page=20):
        query = User.query.join(User.user_roles).join(Role).filter(Role.name == role_name)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total


class ComplaintRepository(BaseRepository):
    def __init__(self):
        super().__init__(Complaint)

    def get_by_ticket_number(self, ticket_number):
        return Complaint.query.filter_by(ticket_number=ticket_number).first()

    def get_citizen_complaints(self, citizen_id, page=1, per_page=20, status=None):
        query = Complaint.query.filter_by(citizen_id=citizen_id)
        if status:
            query = query.filter_by(status=status)
        query = query.order_by(desc(Complaint.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total

    def get_department_complaints(self, department_id, page=1, per_page=20, status=None):
        query = Complaint.query.filter_by(department_id=department_id)
        if status:
            query = query.filter_by(status=status)
        query = query.order_by(desc(Complaint.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total

    def get_officer_assigned_complaints(self, officer_id, page=1, per_page=20):
        query = Complaint.query.filter_by(assigned_officer_id=officer_id).order_by(desc(Complaint.created_at))
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total


class TrafficRepository(BaseRepository):
    def __init__(self):
        super().__init__(TrafficRecord)

    def get_latest_road_records(self):
        subquery = db.session.query(
            TrafficRecord.road_id,
            func.max(TrafficRecord.recorded_at).label("max_time")
        ).group_by(TrafficRecord.road_id).subquery()

        query = TrafficRecord.query.join(
            subquery,
            (TrafficRecord.road_id == subquery.c.road_id) & (TrafficRecord.recorded_at == subquery.c.max_time)
        )
        return query.all()


class WasteRepository(BaseRepository):
    def __init__(self):
        super().__init__(WasteBin)

    def get_critical_bins(self, threshold_percent=80.0):
        return WasteBin.query.filter(WasteBin.current_fill_level >= threshold_percent).all()


class WaterRepository(BaseRepository):
    def __init__(self):
        super().__init__(WaterTank)

    def get_low_level_tanks(self, percent=20.0):
        return WaterTank.query.filter((WaterTank.current_level_liters / WaterTank.capacity_liters * 100) <= percent).all()


class ElectricityRepository(BaseRepository):
    def __init__(self):
        super().__init__(Transformer)

    def get_overloaded_transformers(self, load_percent=90.0):
        return Transformer.query.filter((Transformer.current_load_kw / Transformer.capacity_kva * 100) >= load_percent).all()


class ParkingRepository(BaseRepository):
    def __init__(self):
        super().__init__(ParkingLocation)

    def get_available_parking_zones(self, zone=None):
        query = ParkingLocation.query.filter(ParkingLocation.occupied_spaces < ParkingLocation.total_capacity)
        if zone:
            query = query.filter_by(zone=zone)
        return query.all()


class TransportRepository(BaseRepository):
    def __init__(self):
        super().__init__(TransportRoute)

    def get_active_routes_with_vehicles(self):
        return TransportRoute.query.filter_by(is_active=True).all()


class PollutionRepository(BaseRepository):
    def __init__(self):
        super().__init__(PollutionRecord)

    def get_latest_station_readings(self):
        subquery = db.session.query(
            PollutionRecord.station_id,
            func.max(PollutionRecord.recorded_at).label("max_time")
        ).group_by(PollutionRecord.station_id).subquery()

        query = PollutionRecord.query.join(
            subquery,
            (PollutionRecord.station_id == subquery.c.station_id) & (PollutionRecord.recorded_at == subquery.c.max_time)
        )
        return query.all()


class EmergencyRepository(BaseRepository):
    def __init__(self):
        super().__init__(EmergencyIncident)

    def get_active_emergencies(self):
        return EmergencyIncident.query.filter(EmergencyIncident.status != "CLOSED").order_by(desc(EmergencyIncident.reported_at)).all()


class AlertRepository(BaseRepository):
    def __init__(self):
        super().__init__(SystemAlert)

    def get_active_alerts(self, severity=None):
        query = SystemAlert.query.filter(SystemAlert.status != "RESOLVED")
        if severity:
            query = query.filter_by(severity=severity)
        return query.order_by(desc(SystemAlert.triggered_at)).all()


class NotificationRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserNotification)

    def get_unread_user_notifications(self, user_id):
        return UserNotification.query.filter_by(user_id=user_id, is_read=False).order_by(desc(UserNotification.received_at)).all()


class AuditRepository(BaseRepository):
    def __init__(self):
        super().__init__(AuditLog)

    def get_recent_logs(self, limit=100):
        return AuditLog.query.order_by(desc(AuditLog.timestamp)).limit(limit).all()
