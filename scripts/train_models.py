"""
Trainer Script for 10 Local Scikit-Learn Machine Learning Models.
Trains, evaluates, and saves model artifacts to backend/trained_models/
"""
import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score, f1_score, mean_absolute_error, r2_score

DATASET_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend", "datasets")
MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend", "trained_models")
os.makedirs(MODELS_DIR, exist_ok=True)

def train_traffic_model():
    print("Training Model 1: Traffic Congestion Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "traffic.csv"))
    X = df[["vehicle_count", "average_speed_kmh", "peak_hour"]]
    y = df["congestion_index"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"-> Traffic Model R²: {r2:.4f}, MAE: {mae:.4f}")
    joblib.dump({"model": model, "r2": r2, "mae": mae}, os.path.join(MODELS_DIR, "traffic_congestion_model.joblib"))

def train_waste_model():
    print("Training Model 2: Waste Overflow Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "waste.csv"))
    X = df[["fill_level_percent", "waste_weight_kg", "temperature_celsius", "methane_level_ppm"]]
    y = df["overflow_risk"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"-> Waste Model Accuracy: {acc:.4f}, F1: {f1:.4f}")
    joblib.dump({"model": model, "accuracy": acc, "f1": f1}, os.path.join(MODELS_DIR, "waste_generation_model.joblib"))

def train_water_model():
    print("Training Model 3: Water Demand Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "water.csv"))
    X = df[["flow_rate_lps", "pressure_bar", "ph_level", "chlorine_ppm"]]
    y = df["consumption_liters"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"-> Water Model R²: {r2:.4f}, MAE: {mae:.4f}")
    joblib.dump({"model": model, "r2": r2, "mae": mae}, os.path.join(MODELS_DIR, "water_demand_model.joblib"))

def train_electricity_model():
    print("Training Model 4: Electricity Peak Load Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "electricity.csv"))
    X = df[["consumption_kwh", "power_factor", "frequency_hz", "is_peak_hour"]]
    y = df["peak_demand_kw"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"-> Electricity Model R²: {r2:.4f}, MAE: {mae:.4f}")
    joblib.dump({"model": model, "r2": r2, "mae": mae}, os.path.join(MODELS_DIR, "electricity_demand_model.joblib"))

def train_parking_model():
    print("Training Model 5: Parking Occupancy Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "parking.csv"))
    X = df[["location_id", "occupied_count", "available_count", "turnover_rate"]]
    y = df["occupancy_percentage"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"-> Parking Model R²: {r2:.4f}, MAE: {mae:.4f}")
    joblib.dump({"model": model, "r2": r2, "mae": mae}, os.path.join(MODELS_DIR, "parking_occupancy_model.joblib"))

def train_pollution_model():
    print("Training Model 6: Air Quality AQI Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "pollution.csv"))
    X = df[["pm2_5", "pm10", "co", "no2", "so2", "o3", "temperature_c", "humidity_percent"]]
    y = df["aqi"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"-> Pollution Model R²: {r2:.4f}, MAE: {mae:.4f}")
    joblib.dump({"model": model, "r2": r2, "mae": mae}, os.path.join(MODELS_DIR, "pollution_aqi_model.joblib"))

def train_transport_demand_model():
    print("Training Model 7: Transport Passenger Demand Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "transport.csv"))
    X = df[["route_id", "delay_minutes", "is_peak_hour"]]
    y = df["passenger_count"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"-> Transport Demand Model R²: {r2:.4f}, MAE: {mae:.4f}")
    joblib.dump({"model": model, "r2": r2, "mae": mae}, os.path.join(MODELS_DIR, "transport_demand_model.joblib"))

def train_transport_delay_model():
    print("Training Model 8: Transport Delay Predictor...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "transport.csv"))
    X = df[["route_id", "passenger_count", "is_peak_hour"]]
    y = (df["delay_minutes"] > 10).astype(int)  # 1 if severe delay, else 0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    print(f"-> Transport Delay Model Accuracy: {acc:.4f}, F1: {f1:.4f}")
    joblib.dump({"model": model, "accuracy": acc, "f1": f1}, os.path.join(MODELS_DIR, "transport_delay_model.joblib"))

def train_complaint_priority_model():
    print("Training Model 9: Complaint Priority Classifier...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "complaints.csv"))
    # Map priority labels
    prio_map = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}
    df["priority_encoded"] = df["priority"].map(prio_map)
    
    X = df[["citizen_id", "category_id", "department_id"]]
    y = df["priority_encoded"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"-> Complaint Priority Classifier Accuracy: {acc:.4f}")
    joblib.dump({"model": model, "accuracy": acc}, os.path.join(MODELS_DIR, "complaint_priority_model.joblib"))

def train_anomaly_detection_model():
    print("Training Model 10: Multi-Metric Isolation Forest Anomaly Detector...")
    df = pd.read_csv(os.path.join(DATASET_DIR, "pollution.csv"))
    X = df[["pm2_5", "pm10", "co", "no2", "so2", "o3"]]

    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X)

    print("-> Anomaly Detector Trained Successfully.")
    joblib.dump({"model": model, "type": "isolation_forest"}, os.path.join(MODELS_DIR, "anomaly_detection_model.joblib"))

def main():
    print("=== Training 10 Smart City Local Machine Learning Models ===")
    train_traffic_model()
    train_waste_model()
    train_water_model()
    train_electricity_model()
    train_parking_model()
    train_pollution_model()
    train_transport_demand_model()
    train_transport_delay_model()
    train_complaint_priority_model()
    train_anomaly_detection_model()
    print("=== All 10 ML Models Trained and Saved Successfully ===")

if __name__ == "__main__":
    main()
