"""
API Routes Package Exports.
"""
from .auth_routes import auth_bp
from .citizen_routes import citizen_bp
from .officer_routes import officer_bp
from .admin_routes import admin_bp
from .service_routes import service_bp

from .alert_expanded_routes import alert_expanded_bp
from .analytics_expanded_routes import analytics_expanded_bp
from .asset_expanded_routes import asset_expanded_bp
from .audit_logging_expanded_routes import audit_logging_expanded_bp
from .complaint_expanded_routes import complaint_expanded_bp
from .department_management_expanded_routes import department_management_expanded_bp
from .electricity_expanded_routes import electricity_expanded_bp
from .emergency_expanded_routes import emergency_expanded_bp
from .ml_center_expanded_routes import ml_center_expanded_bp
from .notification_expanded_routes import notification_expanded_bp
from .officer_management_expanded_routes import officer_management_expanded_bp
from .parking_expanded_routes import parking_expanded_bp
from .pollution_expanded_routes import pollution_expanded_bp
from .report_expanded_routes import report_expanded_bp
from .system_settings_expanded_routes import system_settings_expanded_bp
from .traffic_expanded_routes import traffic_expanded_bp
from .transport_expanded_routes import transport_expanded_bp
from .user_management_expanded_routes import user_management_expanded_bp
from .waste_expanded_routes import waste_expanded_bp
from .water_expanded_routes import water_expanded_bp

EXPANDED_BLUEPRINTS = [
    alert_expanded_bp,
    analytics_expanded_bp,
    asset_expanded_bp,
    audit_logging_expanded_bp,
    complaint_expanded_bp,
    department_management_expanded_bp,
    electricity_expanded_bp,
    emergency_expanded_bp,
    ml_center_expanded_bp,
    notification_expanded_bp,
    officer_management_expanded_bp,
    parking_expanded_bp,
    pollution_expanded_bp,
    report_expanded_bp,
    system_settings_expanded_bp,
    traffic_expanded_bp,
    transport_expanded_bp,
    user_management_expanded_bp,
    waste_expanded_bp,
    water_expanded_bp,
]

__all__ = [
    "auth_bp",
    "citizen_bp",
    "officer_bp",
    "admin_bp",
    "service_bp",
    "EXPANDED_BLUEPRINTS",
]
