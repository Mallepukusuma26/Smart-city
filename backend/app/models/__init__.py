"""
Database Models Package Exports.
"""
from .user import db, User, Role, Permission, RolePermission, UserRole
from .department import Department, Officer, Citizen
from .traffic import Road, TrafficSignal, TrafficRecord, TrafficIncident
from .waste import WasteBin, WasteVehicle, WasteRecord, CollectionSchedule
from .water import WaterTank, WaterPipeline, WaterRecord, WaterLeakage
from .electricity import Transformer, ElectricityRecord, PowerOutage
from .parking import ParkingLocation, ParkingSpace, ParkingRecord
from .transport import TransportRoute, TransportVehicle, TransportStop, PassengerRecord
from .pollution import PollutionStation, PollutionRecord
from .complaint import ComplaintCategory, Complaint, ComplaintHistory
from .emergency import EmergencyIncident
from .asset import CityAsset, MaintenanceRecord
from .notification import Notification, UserNotification
from .alert import AlertRule, SystemAlert
from .ml_models import MLModelRegistry, PredictionLog
from .audit import AuditLog
from .system_setting import SystemSetting

__all__ = [
    "db",
    "User",
    "Role",
    "Permission",
    "RolePermission",
    "UserRole",
    "Department",
    "Officer",
    "Citizen",
    "Road",
    "TrafficSignal",
    "TrafficRecord",
    "TrafficIncident",
    "WasteBin",
    "WasteVehicle",
    "WasteRecord",
    "CollectionSchedule",
    "WaterTank",
    "WaterPipeline",
    "WaterRecord",
    "WaterLeakage",
    "Transformer",
    "ElectricityRecord",
    "PowerOutage",
    "ParkingLocation",
    "ParkingSpace",
    "ParkingRecord",
    "TransportRoute",
    "TransportVehicle",
    "TransportStop",
    "PassengerRecord",
    "PollutionStation",
    "PollutionRecord",
    "ComplaintCategory",
    "Complaint",
    "ComplaintHistory",
    "EmergencyIncident",
    "CityAsset",
    "MaintenanceRecord",
    "Notification",
    "UserNotification",
    "AlertRule",
    "SystemAlert",
    "MLModelRegistry",
    "PredictionLog",
    "AuditLog",
    "SystemSetting",
]
