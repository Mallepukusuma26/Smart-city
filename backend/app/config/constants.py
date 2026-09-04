"""
System-wide Constants, Enums, and Configuration Mapping.
"""

class Roles:
    CITIZEN = "CITIZEN"
    OFFICER = "OFFICER"
    ADMIN = "ADMIN"
    
    ALL_ROLES = [CITIZEN, OFFICER, ADMIN]


class DepartmentNames:
    TRAFFIC = "Traffic Management Department"
    WASTE = "Waste Management & Sanitation Department"
    WATER = "Water Supply & Sewage Department"
    ELECTRICITY = "Power & Grid Electricity Department"
    PARKING = "City Parking Authority"
    TRANSPORT = "Public Transport Authority"
    POLLUTION = "Environmental & Pollution Control Board"
    EMERGENCY = "Emergency Disaster Response Command"
    GENERAL = "General Administration"

    ALL_DEPARTMENTS = [
        TRAFFIC,
        WASTE,
        WATER,
        ELECTRICITY,
        PARKING,
        TRANSPORT,
        POLLUTION,
        EMERGENCY,
        GENERAL,
    ]


class ComplaintStatuses:
    SUBMITTED = "SUBMITTED"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    ESCALATED = "ESCALATED"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

    ALL_STATUSES = [
        SUBMITTED,
        ASSIGNED,
        IN_PROGRESS,
        ESCALATED,
        RESOLVED,
        CLOSED,
    ]

    TRANSITIONS = {
        SUBMITTED: [ASSIGNED, ESCALATED, CLOSED],
        ASSIGNED: [IN_PROGRESS, ESCALATED, RESOLVED],
        IN_PROGRESS: [ESCALATED, RESOLVED],
        ESCALATED: [IN_PROGRESS, RESOLVED],
        RESOLVED: [CLOSED, IN_PROGRESS],
        CLOSED: [],
    }


class EmergencyTypes:
    ACCIDENT = "ACCIDENT"
    FIRE = "FIRE"
    MEDICAL = "MEDICAL"
    FLOOD = "FLOOD"
    ROAD_BLOCKAGE = "ROAD_BLOCKAGE"
    INFRASTRUCTURE_FAILURE = "INFRASTRUCTURE_FAILURE"
    SECURITY_INCIDENT = "SECURITY_INCIDENT"
    OTHER = "OTHER"

    ALL_TYPES = [
        ACCIDENT,
        FIRE,
        MEDICAL,
        FLOOD,
        ROAD_BLOCKAGE,
        INFRASTRUCTURE_FAILURE,
        SECURITY_INCIDENT,
        OTHER,
    ]


class SeverityLevels:
    INFO = "INFO"
    WARNING = "WARNING"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

    ALL_SEVERITIES = [INFO, WARNING, HIGH, CRITICAL]


class SLAConfig:
    DEFAULT_SLA_HOURS = {
        "CRITICAL": 4,
        "HIGH": 12,
        "MEDIUM": 24,
        "LOW": 48,
    }


class MLModelNames:
    TRAFFIC_CONGESTION = "traffic_congestion_model"
    WASTE_GENERATION = "waste_generation_model"
    WATER_DEMAND = "water_demand_model"
    ELECTRICITY_DEMAND = "electricity_demand_model"
    PARKING_OCCUPANCY = "parking_occupancy_model"
    POLLUTION_AQI = "pollution_aqi_model"
    TRANSPORT_DEMAND = "transport_demand_model"
    TRANSPORT_DELAY = "transport_delay_model"
    COMPLAINT_PRIORITY = "complaint_priority_model"
    ANOMALY_DETECTION = "anomaly_detection_model"

    ALL_MODELS = [
        TRAFFIC_CONGESTION,
        WASTE_GENERATION,
        WATER_DEMAND,
        ELECTRICITY_DEMAND,
        PARKING_OCCUPANCY,
        POLLUTION_AQI,
        TRANSPORT_DEMAND,
        TRANSPORT_DELAY,
        COMPLAINT_PRIORITY,
        ANOMALY_DETECTION,
    ]


class AQIRatings:
    GOOD = (0, 50, "Good", "#10B981")
    MODERATE = (51, 100, "Moderate", "#F59E0B")
    UNHEALTHY_SENSITIVE = (101, 150, "Unhealthy for Sensitive Groups", "#EF4444")
    UNHEALTHY = (151, 200, "Unhealthy", "#DC2626")
    VERY_UNHEALTHY = (201, 300, "Very Unhealthy", "#7C3AED")
    HAZARDOUS = (301, 500, "Hazardous", "#4C1D95")

    @staticmethod
    def get_rating(aqi_value):
        v = float(aqi_value)
        if v <= 50:
            return AQIRatings.GOOD
        elif v <= 100:
            return AQIRatings.MODERATE
        elif v <= 150:
            return AQIRatings.UNHEALTHY_SENSITIVE
        elif v <= 200:
            return AQIRatings.UNHEALTHY
        elif v <= 300:
            return AQIRatings.VERY_UNHEALTHY
        else:
            return AQIRatings.HAZARDOUS
