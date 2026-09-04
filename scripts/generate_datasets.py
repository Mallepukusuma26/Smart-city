"""
Synthetic Dataset Generator for Local AI/ML Models and Database Seeding.
Generates 10 realistic CSV datasets:
- citizens.csv (5,000+ rows)
- traffic.csv (10,000+ rows)
- waste.csv (10,000+ rows)
- water.csv (10,000+ rows)
- electricity.csv (10,000+ rows)
- parking.csv (5,000+ rows)
- transport.csv (5,000+ rows)
- pollution.csv (10,000+ rows)
- complaints.csv (5,000+ rows)
- emergencies.csv (2,000+ rows)
"""
import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

DATASET_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend", "datasets")
os.makedirs(DATASET_DIR, exist_ok=True)

ZONES = ["North District", "South District", "East District", "West District", "Central Zone", "Industrial Zone"]
WEATHER_TYPES = ["Clear", "Rainy", "Foggy", "Overcast", "Hot"]

def generate_citizens(count=5000):
    print(f"Generating {count} Citizens dataset...")
    first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    occupations = ["Engineer", "Teacher", "Doctor", "Manager", "Student", "Civil Servant", "Business Owner", "Technician", "Accountant", "Architect"]
    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    data = []
    for i in range(1, count + 1):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        data.append({
            "id": i,
            "username": f"citizen_{i}",
            "email": f"citizen_{i}@example.com",
            "full_name": f"{fn} {ln}",
            "phone_number": f"+1-555-{random.randint(100,999):03d}-{random.randint(1000,9999):04d}",
            "address": f"{random.randint(10,999)} Smart City Ave, Street {random.randint(1,50)}",
            "city_zone": random.choice(ZONES),
            "citizen_card_id": f"CTZ-{i:06d}",
            "emergency_contact": f"+1-555-{random.randint(100,999):03d}-{random.randint(1000,9999):04d}",
            "occupation": random.choice(occupations),
            "household_size": random.randint(1, 6),
            "blood_group": random.choice(blood_groups),
            "registered_vehicles_count": random.choice([0, 1, 1, 2, 3]),
            "created_at": (datetime.utcnow() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "citizens.csv"), index=False)
    return df

def generate_traffic(count=10000):
    print(f"Generating {count} Traffic records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=60)
    for i in range(1, count + 1):
        rec_time = base_time + timedelta(minutes=i * 8)
        hour = rec_time.hour
        is_peak = 1 if (7 <= hour <= 10 or 17 <= hour <= 20) else 0
        lanes = random.choice([2, 4, 6])
        road_id = random.randint(1, 25)
        
        # Vehicle count depends on peak hour and lanes
        base_veh = 150 * lanes
        vehicle_count = int(np.random.normal(base_veh * (1.8 if is_peak else 0.7), 80))
        vehicle_count = max(20, vehicle_count)

        # Speed inversely correlated with vehicle count
        avg_speed = max(10.0, round(85.0 - (vehicle_count / (lanes * 40.0)) * 25.0 + random.uniform(-5, 5), 1))
        
        # Congestion index scale 0.0 to 10.0
        congestion_index = round(min(10.0, max(0.5, (vehicle_count / (lanes * 50.0)) * 3.5 + (0.5 if is_peak else 0))), 2)
        if congestion_index > 7.5:
            c_level = "SEVERE"
        elif congestion_index > 5.0:
            c_level = "HIGH"
        elif congestion_index > 3.0:
            c_level = "MODERATE"
        else:
            c_level = "LOW"

        data.append({
            "id": i,
            "road_id": road_id,
            "vehicle_count": vehicle_count,
            "average_speed_kmh": avg_speed,
            "congestion_level": c_level,
            "congestion_index": congestion_index,
            "peak_hour": is_peak,
            "weather_condition": random.choice(WEATHER_TYPES),
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "traffic.csv"), index=False)
    return df

def generate_waste(count=10000):
    print(f"Generating {count} Waste records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=60)
    for i in range(1, count + 1):
        bin_id = random.randint(1, 50)
        rec_time = base_time + timedelta(minutes=i * 8)
        
        # Fill level increases with time
        fill_percent = round(min(100.0, max(5.0, (i % 100) * 1.0 + random.uniform(-3, 3))), 1)
        weight_kg = round(fill_percent * random.uniform(8.0, 12.0), 1)
        temp = round(20.0 + fill_percent * 0.15 + random.uniform(-2, 2), 1)
        methane = round(max(0.5, fill_percent * 0.4 + random.uniform(-1, 1)), 2)

        data.append({
            "id": i,
            "waste_bin_id": bin_id,
            "fill_level_percent": fill_percent,
            "waste_weight_kg": weight_kg,
            "temperature_celsius": temp,
            "methane_level_ppm": methane,
            "overflow_risk": 1 if fill_percent >= 85.0 else 0,
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "waste.csv"), index=False)
    return df

def generate_water(count=10000):
    print(f"Generating {count} Water records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=60)
    for i in range(1, count + 1):
        tank_id = random.randint(1, 20)
        rec_time = base_time + timedelta(minutes=i * 8)
        hour = rec_time.hour
        is_morning = 1 if 6 <= hour <= 9 else 0
        
        flow_lps = round(max(5.0, 45.0 + (30.0 if is_morning else 0.0) + random.uniform(-10, 10)), 2)
        consumption = round(flow_lps * 60 * 8, 1)
        pressure = round(max(1.0, 4.5 - (flow_lps / 50.0) * 1.2 + random.uniform(-0.3, 0.3)), 2)
        ph = round(7.2 + random.uniform(-0.4, 0.4), 2)
        chlorine = round(0.5 + random.uniform(-0.15, 0.15), 2)

        data.append({
            "id": i,
            "water_tank_id": tank_id,
            "flow_rate_lps": flow_lps,
            "consumption_liters": consumption,
            "pressure_bar": pressure,
            "ph_level": ph,
            "chlorine_ppm": chlorine,
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "water.csv"), index=False)
    return df

def generate_electricity(count=10000):
    print(f"Generating {count} Electricity records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=60)
    for i in range(1, count + 1):
        trans_id = random.randint(1, 30)
        rec_time = base_time + timedelta(minutes=i * 8)
        hour = rec_time.hour
        is_peak = 1 if (14 <= hour <= 21) else 0

        demand_kw = round(max(50.0, 320.0 * (1.6 if is_peak else 0.8) + random.uniform(-30, 30)), 2)
        kwh = round(demand_kw * 0.133, 2)
        pf = round(min(0.99, max(0.85, 0.96 - (demand_kw / 600.0) * 0.08 + random.uniform(-0.02, 0.02))), 2)

        data.append({
            "id": i,
            "transformer_id": trans_id,
            "consumption_kwh": kwh,
            "peak_demand_kw": demand_kw,
            "power_factor": pf,
            "frequency_hz": round(50.0 + random.uniform(-0.1, 0.1), 2),
            "is_peak_hour": is_peak,
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "electricity.csv"), index=False)
    return df

def generate_parking(count=5000):
    print(f"Generating {count} Parking records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=40)
    for i in range(1, count + 1):
        loc_id = random.randint(1, 15)
        rec_time = base_time + timedelta(minutes=i * 11)
        hour = rec_time.hour
        is_business_hours = 1 if 9 <= hour <= 18 else 0

        capacity = 200
        occ = int(np.random.normal(capacity * (0.85 if is_business_hours else 0.30), 20))
        occ = min(capacity, max(5, occ))
        avail = capacity - occ
        percent = round((occ / capacity) * 100, 1)

        data.append({
            "id": i,
            "location_id": loc_id,
            "occupied_count": occ,
            "available_count": avail,
            "occupancy_percentage": percent,
            "turnover_rate": round(1.0 + (percent / 100.0) * 0.8, 2),
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "parking.csv"), index=False)
    return df

def generate_transport(count=5000):
    print(f"Generating {count} Transport records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=40)
    for i in range(1, count + 1):
        route_id = random.randint(1, 12)
        rec_time = base_time + timedelta(minutes=i * 11)
        hour = rec_time.hour
        is_peak = 1 if (7 <= hour <= 9 or 17 <= hour <= 19) else 0

        passengers = int(np.random.normal(55 * (1.7 if is_peak else 0.6), 15))
        passengers = min(120, max(5, passengers))
        delay = int(max(0, (passengers / 20) + (random.randint(0, 15) if is_peak else random.randint(0, 3))))

        data.append({
            "id": i,
            "route_id": route_id,
            "passenger_count": passengers,
            "delay_minutes": delay,
            "weather_condition": random.choice(WEATHER_TYPES),
            "is_peak_hour": is_peak,
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "transport.csv"), index=False)
    return df

def generate_pollution(count=10000):
    print(f"Generating {count} Pollution records...")
    data = []
    base_time = datetime.utcnow() - timedelta(days=60)
    for i in range(1, count + 1):
        station_id = random.randint(1, 10)
        rec_time = base_time + timedelta(minutes=i * 8)
        
        # AQI calculation with environmental noise
        pm25 = round(max(5.0, np.random.normal(35.0, 15.0)), 1)
        pm10 = round(pm25 * random.uniform(1.4, 2.1), 1)
        co = round(max(0.1, pm25 * 0.03 + random.uniform(-0.1, 0.1)), 2)
        no2 = round(max(10.0, pm25 * 0.9 + random.uniform(-5, 5)), 1)
        so2 = round(max(5.0, pm25 * 0.4 + random.uniform(-2, 2)), 1)
        o3 = round(max(10.0, 40.0 + random.uniform(-15, 15)), 1)
        aqi = round(min(500.0, max(15.0, pm25 * 1.8 + no2 * 0.5)), 1)

        data.append({
            "id": i,
            "station_id": station_id,
            "aqi": aqi,
            "pm2_5": pm25,
            "pm10": pm10,
            "co": co,
            "no2": no2,
            "so2": so2,
            "o3": o3,
            "temperature_c": round(random.uniform(18.0, 38.0), 1),
            "humidity_percent": round(random.uniform(30.0, 85.0), 1),
            "recorded_at": rec_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "pollution.csv"), index=False)
    return df

def generate_complaints(count=5000):
    print(f"Generating {count} Complaints dataset...")
    titles = [
        "Pothole on Main Road causing traffic delay", "Waste bin overflowing for 3 days", "Water pipeline leakage detected",
        "Streetlight out of order", "Transformer sparking near residential block", "Illegal parking blocking emergency lane",
        "Bus route delay over 30 minutes", "High air pollution near factory site", "Water pressure severely low", "Power outage in West Zone"
    ]
    priorities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    statuses = ["SUBMITTED", "ASSIGNED", "IN_PROGRESS", "ESCALATED", "RESOLVED", "CLOSED"]

    data = []
    base_time = datetime.utcnow() - timedelta(days=90)
    for i in range(1, count + 1):
        c_time = base_time + timedelta(minutes=i * 25)
        prio = random.choice(priorities)
        stat = random.choice(statuses)
        data.append({
            "id": i,
            "ticket_number": f"TKT-{c_time.strftime('%Y%m%d')}-{i:04d}",
            "citizen_id": random.randint(1, 1000),
            "category_id": random.randint(1, 10),
            "department_id": random.randint(1, 8),
            "title": random.choice(titles),
            "description": "Citizen reported an urgent civic issue requiring immediate municipal officer resolution.",
            "location": f"Zone {random.randint(1,6)} Street {random.randint(1,100)}",
            "zone": random.choice(ZONES),
            "priority": prio,
            "status": stat,
            "created_at": c_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "complaints.csv"), index=False)
    return df

def generate_emergencies(count=2000):
    print(f"Generating {count} Emergencies dataset...")
    types = ["ACCIDENT", "FIRE", "MEDICAL", "FLOOD", "ROAD_BLOCKAGE", "INFRASTRUCTURE_FAILURE", "SECURITY_INCIDENT"]
    data = []
    base_time = datetime.utcnow() - timedelta(days=90)
    for i in range(1, count + 1):
        e_time = base_time + timedelta(minutes=i * 60)
        data.append({
            "id": i,
            "incident_code": f"EMG-{e_time.strftime('%Y%m%d')}-{i:04d}",
            "incident_type": random.choice(types),
            "severity": random.choice(["HIGH", "CRITICAL"]),
            "location": f"Location Marker #{i}",
            "zone": random.choice(ZONES),
            "description": "Urgent emergency alert dispatched to response command center.",
            "status": random.choice(["REPORTED", "DISPATCHED", "ON_SITE", "RESOLVED", "CLOSED"]),
            "response_time_minutes": round(random.uniform(4.0, 25.0), 1),
            "reported_at": e_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATASET_DIR, "emergencies.csv"), index=False)
    return df

def main():
    print("=== Starting Smart City Synthetic Data Generation ===")
    generate_citizens(5000)
    generate_traffic(10000)
    generate_waste(10000)
    generate_water(10000)
    generate_electricity(10000)
    generate_parking(5000)
    generate_transport(5000)
    generate_pollution(10000)
    generate_complaints(5000)
    generate_emergencies(2000)
    print("=== Synthetic Datasets Generation Completed Successfully ===")

if __name__ == "__main__":
    main()
