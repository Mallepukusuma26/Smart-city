"""
Inference Pipeline Wrappers for All 10 Machine Learning Models.
"""
import os
import joblib
import numpy as np
from ...config.settings import Config

class MLInferenceEngine:
    @staticmethod
    def _load(filename):
        path = os.path.join(Config.TRAINED_MODELS_DIR, filename)
        if not os.path.exists(path):
            return None
        return joblib.load(path)

    @staticmethod
    def predict_traffic(vehicle_count, avg_speed_kmh, is_peak_hour=1):
        pkg = MLInferenceEngine._load("traffic_congestion_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        idx = float(model.predict([[vehicle_count, avg_speed_kmh, is_peak_hour]])[0])
        return {
            "predicted_congestion_index": round(idx, 2),
            "congestion_level": "SEVERE" if idx > 7.5 else ("HIGH" if idx > 5.0 else ("MODERATE" if idx > 3.0 else "LOW")),
            "r2_score": pkg.get("r2"),
        }

    @staticmethod
    def predict_waste_overflow(fill_level, weight_kg, temp_c=25.0, methane_ppm=5.0):
        pkg = MLInferenceEngine._load("waste_generation_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        pred = int(model.predict([[fill_level, weight_kg, temp_c, methane_ppm]])[0])
        probs = model.predict_proba([[fill_level, weight_kg, temp_c, methane_ppm]])[0]
        return {
            "overflow_risk_predicted": bool(pred == 1),
            "confidence_probability": round(float(probs[pred]), 4),
            "model_accuracy": pkg.get("accuracy"),
        }

    @staticmethod
    def predict_water_demand(flow_rate_lps, pressure_bar=4.0, ph_level=7.2, chlorine_ppm=0.5):
        pkg = MLInferenceEngine._load("water_demand_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        consumption = float(model.predict([[flow_rate_lps, pressure_bar, ph_level, chlorine_ppm]])[0])
        return {
            "predicted_consumption_liters": round(consumption, 1),
            "mae": pkg.get("mae"),
        }

    @staticmethod
    def predict_electricity_demand(consumption_kwh, power_factor=0.95, frequency_hz=50.0, is_peak_hour=1):
        pkg = MLInferenceEngine._load("electricity_demand_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        demand = float(model.predict([[consumption_kwh, power_factor, frequency_hz, is_peak_hour]])[0])
        return {
            "predicted_peak_demand_kw": round(demand, 2),
            "mae": pkg.get("mae"),
        }

    @staticmethod
    def predict_parking_occupancy(location_id, occupied_count, available_count, turnover_rate=1.2):
        pkg = MLInferenceEngine._load("parking_occupancy_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        occ_pct = float(model.predict([[location_id, occupied_count, available_count, turnover_rate]])[0])
        return {
            "predicted_occupancy_percentage": round(occ_pct, 1),
            "r2_score": pkg.get("r2"),
        }

    @staticmethod
    def predict_aqi(pm2_5, pm10, co=1.0, no2=25.0, so2=10.0, o3=30.0, temp_c=25.0, humidity=50.0):
        pkg = MLInferenceEngine._load("pollution_aqi_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        aqi = float(model.predict([[pm2_5, pm10, co, no2, so2, o3, temp_c, humidity]])[0])
        return {
            "predicted_aqi": round(aqi, 1),
            "r2_score": pkg.get("r2"),
        }

    @staticmethod
    def predict_transport_demand(route_id, delay_minutes=5, is_peak_hour=1):
        pkg = MLInferenceEngine._load("transport_demand_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        passengers = float(model.predict([[route_id, delay_minutes, is_peak_hour]])[0])
        return {
            "predicted_passenger_demand": int(round(passengers)),
            "r2_score": pkg.get("r2"),
        }

    @staticmethod
    def predict_transport_delay(route_id, passenger_count, is_peak_hour=1):
        pkg = MLInferenceEngine._load("transport_delay_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        is_delayed = int(model.predict([[route_id, passenger_count, is_peak_hour]])[0])
        return {
            "severe_delay_predicted": bool(is_delayed == 1),
            "model_accuracy": pkg.get("accuracy"),
        }

    @staticmethod
    def predict_complaint_priority(citizen_id, category_id, department_id):
        pkg = MLInferenceEngine._load("complaint_priority_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        pred_code = int(model.predict([[citizen_id, category_id, department_id]])[0])
        prio_names = {0: "LOW", 1: "MEDIUM", 2: "HIGH", 3: "CRITICAL"}
        return {
            "predicted_priority": prio_names.get(pred_code, "MEDIUM"),
            "model_accuracy": pkg.get("accuracy"),
        }

    @staticmethod
    def detect_anomalies(pm2_5, pm10, co, no2, so2, o3):
        pkg = MLInferenceEngine._load("anomaly_detection_model.joblib")
        if not pkg:
            return {"error": "Model not trained"}
        model = pkg["model"]
        # Isolation forest returns -1 for anomaly, 1 for normal
        pred = model.predict([[pm2_5, pm10, co, no2, so2, o3]])[0]
        return {
            "is_anomaly": bool(pred == -1),
            "anomaly_score": round(float(model.score_samples([[pm2_5, pm10, co, no2, so2, o3]])[0]), 4),
        }
