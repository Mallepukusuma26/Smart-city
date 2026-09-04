"""
City Operations Services for Traffic, Waste, Water, Electricity, Parking, Transport, Pollution.
"""
from datetime import datetime
from sqlalchemy import func
from ..models import (
    db, Road, TrafficSignal, TrafficRecord, TrafficIncident,
    WasteBin, WasteVehicle, WasteRecord, CollectionSchedule,
    WaterTank, WaterPipeline, WaterRecord, WaterLeakage,
    Transformer, ElectricityRecord, PowerOutage,
    ParkingLocation, ParkingSpace, ParkingRecord,
    TransportRoute, TransportVehicle, TransportStop, PassengerRecord,
    PollutionStation, PollutionRecord, SystemAlert, AlertRule
)

class CityOperationsService:
    # ---------------- TRAFFIC MANAGEMENT ----------------
    @staticmethod
    def get_traffic_overview():
        roads = Road.query.all()
        incidents = TrafficIncident.query.filter_by(status="OPEN").all()
        avg_speed = db.session.query(func.avg(TrafficRecord.average_speed_kmh)).scalar() or 45.0
        avg_congestion = db.session.query(func.avg(TrafficRecord.congestion_index)).scalar() or 3.2
        return {
            "total_roads": len(roads),
            "active_incidents": len(incidents),
            "average_city_speed_kmh": round(avg_speed, 1),
            "average_congestion_index": round(avg_congestion, 2),
            "high_congestion_roads": [r.to_dict() for r in roads if r.status == "BLOCKED"]
        }

    # ---------------- WASTE MANAGEMENT ----------------
    @staticmethod
    def get_waste_overview():
        bins = WasteBin.query.all()
        critical_bins = [b for b in bins if b.current_fill_level >= 80.0]
        vehicles = WasteVehicle.query.all()
        active_schedules = CollectionSchedule.query.filter_by(status="IN_PROGRESS").all()
        avg_fill = (sum(b.current_fill_level for b in bins) / len(bins)) if bins else 0.0
        return {
            "total_bins": len(bins),
            "critical_bins_count": len(critical_bins),
            "average_fill_level_percent": round(avg_fill, 1),
            "total_vehicles": len(vehicles),
            "active_schedules_count": len(active_schedules),
            "overflow_risk_bins": [b.to_dict() for b in critical_bins]
        }

    # ---------------- WATER MANAGEMENT ----------------
    @staticmethod
    def get_water_overview():
        tanks = WaterTank.query.all()
        pipelines = WaterPipeline.query.all()
        active_leakages = WaterLeakage.query.filter(WaterLeakage.status != "REPAIRED").all()
        total_capacity = sum(t.capacity_liters for t in tanks)
        total_current = sum(t.current_level_liters for t in tanks)
        avg_ph = (sum(t.water_quality_ph for t in tanks) / len(tanks)) if tanks else 7.2
        return {
            "total_tanks": len(tanks),
            "total_capacity_liters": total_capacity,
            "current_stored_liters": total_current,
            "city_storage_percentage": round((total_current / total_capacity * 100), 1) if total_capacity else 0,
            "average_ph": round(avg_ph, 2),
            "active_leakages_count": len(active_leakages),
            "healthy_pipelines_count": len([p for p in pipelines if p.status == "HEALTHY"])
        }

    # ---------------- ELECTRICITY MANAGEMENT ----------------
    @staticmethod
    def get_electricity_overview():
        transformers = Transformer.query.all()
        outages = PowerOutage.query.filter_by(status="ACTIVE").all()
        overloaded = [t for t in transformers if (t.current_load_kw / t.capacity_kva * 100) >= 90.0]
        total_load = sum(t.current_load_kw for t in transformers)
        return {
            "total_transformers": len(transformers),
            "total_grid_load_kw": round(total_load, 1),
            "overloaded_transformers_count": len(overloaded),
            "active_power_outages": len(outages),
            "affected_customers_total": sum(o.affected_customers for o in outages)
        }

    # ---------------- PARKING MANAGEMENT ----------------
    @staticmethod
    def get_parking_overview():
        locations = ParkingLocation.query.all()
        total_cap = sum(l.total_capacity for l in locations)
        total_occ = sum(l.occupied_spaces for l in locations)
        return {
            "total_locations": len(locations),
            "total_city_capacity": total_cap,
            "total_occupied_spaces": total_occ,
            "total_available_spaces": max(0, total_cap - total_occ),
            "city_occupancy_rate": round((total_occ / total_cap * 100), 1) if total_cap else 0
        }

    # ---------------- PUBLIC TRANSPORT ----------------
    @staticmethod
    def get_transport_overview():
        routes = TransportRoute.query.filter_by(is_active=True).all()
        vehicles = TransportVehicle.query.all()
        delayed_vehicles = [v for v in vehicles if v.status == "DELAYED"]
        total_passengers = sum(v.current_passengers for v in vehicles)
        return {
            "active_routes_count": len(routes),
            "total_fleet_vehicles": len(vehicles),
            "delayed_vehicles_count": len(delayed_vehicles),
            "current_active_passengers": total_passengers
        }

    # ---------------- POLLUTION MONITORING ----------------
    @staticmethod
    def get_pollution_overview():
        stations = PollutionStation.query.all()
        records = PollutionRecord.query.order_by(PollutionRecord.recorded_at.desc()).limit(len(stations)).all()
        avg_aqi = (sum(r.aqi for r in records) / len(records)) if records else 65.0
        max_aqi = max([r.aqi for r in records], default=65.0)
        return {
            "total_stations": len(stations),
            "average_city_aqi": round(avg_aqi, 1),
            "max_station_aqi": round(max_aqi, 1),
            "stations_data": [r.to_dict() for r in records]
        }
