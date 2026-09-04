"""
Multi-Dimensional Analytics Engine Service.
"""
from datetime import datetime, timedelta
from sqlalchemy import func
from ..models import (
    db, Complaint, TrafficRecord, WasteBin, WaterTank, Transformer,
    ParkingLocation, TransportVehicle, PollutionRecord, EmergencyIncident
)

class AnalyticsService:
    @staticmethod
    def get_city_kpis():
        # Total complaints
        total_complaints = Complaint.query.count()
        resolved_complaints = Complaint.query.filter_by(status="RESOLVED").count()
        resolution_rate = round((resolved_complaints / total_complaints * 100), 1) if total_complaints else 100.0

        # Traffic index
        avg_traffic_idx = db.session.query(func.avg(TrafficRecord.congestion_index)).scalar() or 3.0

        # Waste overflow risk
        high_fill_bins = WasteBin.query.filter(WasteBin.current_fill_level >= 80.0).count()

        # AQI
        avg_aqi = db.session.query(func.avg(PollutionRecord.aqi)).scalar() or 55.0

        # Emergency count
        active_emergencies = EmergencyIncident.query.filter(EmergencyIncident.status != "CLOSED").count()

        return {
            "resolution_rate": resolution_rate,
            "total_complaints": total_complaints,
            "resolved_complaints": resolved_complaints,
            "avg_traffic_index": round(avg_traffic_idx, 2),
            "high_fill_bins": high_fill_bins,
            "city_avg_aqi": round(avg_aqi, 1),
            "active_emergencies": active_emergencies,
            "overall_health_score": round(max(50.0, 100.0 - (avg_traffic_idx * 5 + (avg_aqi - 50) * 0.3 + active_emergencies * 2)), 1)
        }

    @staticmethod
    def get_department_analytics(department_id):
        complaints = Complaint.query.filter_by(department_id=department_id).all()
        total = len(complaints)
        resolved = len([c for c in complaints if c.status == "RESOLVED"])
        pending = len([c for c in complaints if c.status in ["SUBMITTED", "ASSIGNED", "IN_PROGRESS"]])
        escalated = len([c for c in complaints if c.status == "ESCALATED"])
        sla_breached = len([c for c in complaints if c.is_sla_breached()])

        avg_rating = 4.5
        ratings = [c.feedback_rating for c in complaints if c.feedback_rating is not None]
        if ratings:
            avg_rating = round(sum(ratings) / len(ratings), 2)

        return {
            "department_id": department_id,
            "total_complaints": total,
            "resolved_complaints": resolved,
            "pending_complaints": pending,
            "escalated_complaints": escalated,
            "sla_breached_complaints": sla_breached,
            "resolution_rate": round((resolved / total * 100), 1) if total else 100.0,
            "customer_satisfaction_rating": avg_rating
        }
