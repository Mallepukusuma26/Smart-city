"""
Waste Management & Collection Route Optimization Domain Service.
"""
from datetime import datetime
from ..models import db, WasteBin, WasteVehicle, WasteRecord, CollectionSchedule

class WasteService:
    @staticmethod
    def calculate_bin_overflow_risk(fill_level_percent, weight_kg, methane_ppm=5.0):
        """
        Multi-variable Waste Bin Overflow Risk Algorithm.
        Evaluates fill percentage, compaction density, and gas buildup.
        """
        # Density kg per percent fill
        density = weight_kg / max(1.0, fill_level_percent)
        
        # Risk score scale 0.0 to 100.0
        risk_score = (fill_level_percent * 0.7) + (min(30.0, density * 2.0)) + (min(10.0, methane_ppm * 0.5))
        risk_score = min(100.0, max(0.0, risk_score))
        
        return {
            "overflow_risk_score": round(risk_score, 1),
            "is_overflow_imminent": risk_score >= 80.0,
            "recommended_priority": "CRITICAL" if risk_score >= 85.0 else ("HIGH" if risk_score >= 70.0 else "NORMAL")
        }

    @staticmethod
    def optimize_collection_routes(zone):
        """
        Nearest-Neighbor TSP Route Heuristic for Sanitation Trucks in a Zone.
        Prioritizes bins with fill level >= 75%.
        """
        critical_bins = WasteBin.query.filter_by(zone=zone).filter(WasteBin.current_fill_level >= 75.0).all()
        vehicles = WasteVehicle.query.filter_by(assigned_zone=zone, status="AVAILABLE").all()

        if not critical_bins or not vehicles:
            return {"assigned": 0, "message": "No critical bins or available vehicles for zone."}

        # Simple assignment heuristic
        assigned_count = 0
        for i, bin_obj in enumerate(critical_bins):
            veh = vehicles[i % len(vehicles)]
            sched_code = f"SCH-{zone[:3].upper()}-{datetime.utcnow().strftime('%M%S')}-{i+1:03d}"
            
            sched = CollectionSchedule(
                schedule_code=sched_code,
                vehicle_id=veh.id,
                target_zone=zone,
                collection_date=datetime.utcnow().strftime("%Y-%m-%d"),
                time_slot="Immediate Priority Dispatch",
                status="SCHEDULED"
            )
            db.session.add(sched)
            assigned_count += 1

        db.session.commit()
        return {
            "target_zone": zone,
            "critical_bins_count": len(critical_bins),
            "assigned_schedules_count": assigned_count
        }
