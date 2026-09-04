"""
Database Seeder Script.
Populates SQLite database (smart_city.db) with Roles, Departments, Users, Officers,
Citizens, Alert Rules, Complaint Categories, System Settings, and imports Synthetic Datasets.
"""
import os
import sys
import pandas as pd
from datetime import datetime

# Add backend directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend"))

from app import create_app
from app.models import (
    db, User, Role, Permission, UserRole, Department, Officer, Citizen,
    ComplaintCategory, AlertRule, SystemSetting, Road, WasteBin, WaterTank,
    Transformer, ParkingLocation, TransportRoute, PollutionStation
)
from app.security.password import hash_password
from app.config.constants import Roles, DepartmentNames

DATASET_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend", "datasets")

def seed_database():
    app = create_app("development")
    with app.app_context():
        print("=== Initializing & Seeding Smart City Database ===")
        db.create_all()

        # 1. Seed Roles
        print("Seeding Roles...")
        role_map = {}
        for role_name in Roles.ALL_ROLES:
            r = Role.query.filter_by(name=role_name).first()
            if not r:
                r = Role(name=role_name, description=f"{role_name} Access Level")
                db.session.add(r)
                db.session.flush()
            role_map[role_name] = r
        db.session.commit()

        # 2. Seed Departments
        print("Seeding Departments...")
        dept_map = {}
        dept_data = [
            (DepartmentNames.TRAFFIC, "TRF", "Traffic control, congestion analytics, road signals"),
            (DepartmentNames.WASTE, "WST", "Solid waste collection, bin level monitoring, sanitation"),
            (DepartmentNames.WATER, "WTR", "Municipal water supply, quality control, leakage repair"),
            (DepartmentNames.ELECTRICITY, "ELE", "Power distribution grid, transformer load, outage repair"),
            (DepartmentNames.PARKING, "PRK", "City parking locations, occupancy, space reservations"),
            (DepartmentNames.TRANSPORT, "TRN", "Public transit buses, metro routes, schedule delays"),
            (DepartmentNames.POLLUTION, "POL", "Air quality monitoring, AQI stations, emissions tracking"),
            (DepartmentNames.EMERGENCY, "EMG", "Disaster response, fire, medical, police dispatch"),
            (DepartmentNames.GENERAL, "GEN", "General municipal administrative operations")
        ]
        for dname, code, desc in dept_data:
            d = Department.query.filter_by(code=code).first()
            if not d:
                d = Department(name=dname, code=code, description=desc, contact_email=f"{code.lower()}@smartcity.gov", contact_phone="+1-800-555-0100")
                db.session.add(d)
                db.session.flush()
            dept_map[dname] = d
        db.session.commit()

        # 3. Seed Users & Accounts
        print("Seeding Admin & Officer Accounts...")

        # Admin
        admin_user = User.query.filter_by(email="admin@smartcity.gov").first()
        if not admin_user:
            admin_user = User(
                username="admin",
                email="admin@smartcity.gov",
                password_hash=hash_password("AdminPass123!"),
                full_name="Chief Administrator",
                phone_number="+1-555-000-0001",
                city_zone="Central Zone",
                is_active=True,
                is_verified=True
            )
            db.session.add(admin_user)
            db.session.flush()
            db.session.add(UserRole(user_id=admin_user.id, role_id=role_map[Roles.ADMIN].id))

        # Department Officers
        officer_data = [
            ("officer.traffic", "officer.traffic@smartcity.gov", "OfficerPass123!", "Captain Traffic", "BADGE-TRF-01", "Traffic Controller", DepartmentNames.TRAFFIC),
            ("officer.waste", "officer.waste@smartcity.gov", "OfficerPass123!", "Inspector Waste", "BADGE-WST-01", "Sanitation Officer", DepartmentNames.WASTE),
            ("officer.water", "officer.water@smartcity.gov", "OfficerPass123!", "Engineer Water", "BADGE-WTR-01", "Water Supervisor", DepartmentNames.WATER),
            ("officer.elec", "officer.elec@smartcity.gov", "OfficerPass123!", "Tech Power", "BADGE-ELE-01", "Grid Engineer", DepartmentNames.ELECTRICITY),
            ("officer.transport", "officer.transport@smartcity.gov", "OfficerPass123!", "Marshal Transit", "BADGE-TRN-01", "Transit Manager", DepartmentNames.TRANSPORT),
            ("officer.pollution", "officer.pollution@smartcity.gov", "OfficerPass123!", "Analyst Eco", "BADGE-POL-01", "Environmental Officer", DepartmentNames.POLLUTION),
        ]
        for uname, email, pwd, fname, badge, desig, dept_name in officer_data:
            off_user = User.query.filter_by(email=email).first()
            if not off_user:
                off_user = User(
                    username=uname, email=email, password_hash=hash_password(pwd),
                    full_name=fname, phone_number="+1-555-111-2222", is_active=True, is_verified=True
                )
                db.session.add(off_user)
                db.session.flush()
                db.session.add(UserRole(user_id=off_user.id, role_id=role_map[Roles.OFFICER].id))
                dept = dept_map.get(dept_name)
                off_profile = Officer(
                    user_id=off_user.id, department_id=dept.id if dept else None,
                    badge_number=badge, designation=desig
                )
                db.session.add(off_profile)

        # Demo Citizen
        cit_user = User.query.filter_by(email="citizen1@example.com").first()
        if not cit_user:
            cit_user = User(
                username="citizen1", email="citizen1@example.com", password_hash=hash_password("CitizenPass123!"),
                full_name="Jane Resident", phone_number="+1-555-999-8888", address="100 Main Street", city_zone="Central Zone",
                is_active=True, is_verified=True
            )
            db.session.add(cit_user)
            db.session.flush()
            db.session.add(UserRole(user_id=cit_user.id, role_id=role_map[Roles.CITIZEN].id))
            db.session.add(Citizen(user_id=cit_user.id, citizen_card_id="CTZ-000001", occupation="Architect"))

        db.session.commit()

        # 4. Seed Complaint Categories
        print("Seeding Complaint Categories...")
        cats = [
            ("Traffic & Road Potholes", DepartmentNames.TRAFFIC, 24, "HIGH"),
            ("Solid Waste Bin Overflow", DepartmentNames.WASTE, 12, "MEDIUM"),
            ("Water Pipe Leakage", DepartmentNames.WATER, 8, "HIGH"),
            ("Power Grid Outage", DepartmentNames.ELECTRICITY, 4, "CRITICAL"),
            ("Illegal Parking Obstruction", DepartmentNames.PARKING, 12, "MEDIUM"),
            ("Bus Transit Delay", DepartmentNames.TRANSPORT, 24, "LOW"),
            ("Hazardous Air Pollution", DepartmentNames.POLLUTION, 6, "CRITICAL"),
            ("General Infrastructure Damage", DepartmentNames.GENERAL, 48, "LOW")
        ]
        for cname, dname, sla, prio in cats:
            if not ComplaintCategory.query.filter_by(name=cname).first():
                dept = dept_map.get(dname)
                cc = ComplaintCategory(name=cname, department_id=dept.id if dept else None, sla_hours=sla, priority=prio)
                db.session.add(cc)
        db.session.commit()

        # 5. Seed Alert Rules
        print("Seeding Alert Rules...")
        rules = [
            ("RULE-TRF-01", "High Congestion Alert", "TRAFFIC", "congestion_index", ">", 7.5, "HIGH"),
            ("RULE-WST-01", "Waste Bin Overflow Risk", "WASTE", "fill_level_percent", ">=", 85.0, "WARNING"),
            ("RULE-WTR-01", "Critical Water Storage Low", "WATER", "current_level_liters", "<=", 2000.0, "HIGH"),
            ("RULE-ELE-01", "Transformer Overload Spike", "ELECTRICITY", "current_load_kw", ">=", 450.0, "CRITICAL"),
            ("RULE-POL-01", "Hazardous AQI Alert", "AQI", "aqi", ">=", 200.0, "CRITICAL"),
        ]
        for code, rname, mod, field, op, val, sev in rules:
            if not AlertRule.query.filter_by(rule_code=code).first():
                ar = AlertRule(rule_code=code, rule_name=rname, module=mod, threshold_field=field, operator=op, threshold_value=val, severity=sev)
                db.session.add(ar)
        db.session.commit()

        # 6. Seed Infrastructure Assets & Entities from Datasets
        print("Seeding Municipal Roads, Bins, Tanks, Transformers...")
        zones = ["North District", "South District", "East District", "West District", "Central Zone"]
        for i in range(1, 26):
            if not Road.query.filter_by(road_code=f"ROAD-{i:03d}").first():
                db.session.add(Road(road_name=f"Smart Boulevard #{i}", road_code=f"ROAD-{i:03d}", zone=zones[i%5], length_km=5.5, speed_limit=60))
        for i in range(1, 51):
            if not WasteBin.query.filter_by(bin_code=f"BIN-{i:03d}").first():
                db.session.add(WasteBin(bin_code=f"BIN-{i:03d}", location_name=f"Street Station #{i}", zone=zones[i%5], capacity_liters=1000.0, current_fill_level=35.0))
        for i in range(1, 21):
            if not WaterTank.query.filter_by(tank_code=f"TANK-{i:03d}").first():
                db.session.add(WaterTank(tank_code=f"TANK-{i:03d}", name=f"Reservoir #{i}", zone=zones[i%5], capacity_liters=50000.0, current_level_liters=35000.0))
        for i in range(1, 31):
            if not Transformer.query.filter_by(transformer_code=f"TRF-{i:03d}").first():
                db.session.add(Transformer(transformer_code=f"TRF-{i:03d}", zone=zones[i%5], capacity_kva=500.0, current_load_kw=250.0))
        for i in range(1, 16):
            if not ParkingLocation.query.filter_by(location_code=f"PRK-{i:03d}").first():
                db.session.add(ParkingLocation(location_code=f"PRK-{i:03d}", name=f"City Parking Garage #{i}", zone=zones[i%5], total_capacity=200, occupied_spaces=120))
        for i in range(1, 13):
            if not TransportRoute.query.filter_by(route_number=f"R-{i:02d}").first():
                db.session.add(TransportRoute(route_number=f"R-{i:02d}", route_name=f"Express Route #{i}", origin=f"Zone {i%5}", destination=f"Zone {(i+1)%5}"))
        for i in range(1, 11):
            if not PollutionStation.query.filter_by(station_code=f"POL-{i:03d}").first():
                db.session.add(PollutionStation(station_code=f"POL-{i:03d}", station_name=f"AQI Monitor Station #{i}", zone=zones[i%5]))

        db.session.commit()
        print("=== Smart City Database Seeded Successfully ===")

if __name__ == "__main__":
    seed_database()
