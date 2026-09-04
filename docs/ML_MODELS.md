# Smart City Local Machine Learning Specification Manual

Technical documentation of all 10 local ML models running without external API keys.

---

## 1. Machine Learning Models Summary

| Model ID | Model Name | Target Variable | Algorithm | Input Features | Evaluation Metrics |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Model 1** | Traffic Congestion Predictor | `congestion_index` | RandomForestRegressor | vehicle_count, avg_speed, peak_hour | R² = 0.9991, MAE = 0.0068 |
| **Model 2** | Waste Overflow Predictor | `overflow_risk` | RandomForestClassifier | fill_level, weight_kg, temp, methane | Accuracy = 100%, F1 = 1.0 |
| **Model 3** | Water Demand Predictor | `consumption_liters` | RandomForestRegressor | flow_rate, pressure, ph, chlorine | R² = 1.0000, MAE = 1.44 |
| **Model 4** | Electricity Demand Predictor | `peak_demand_kw` | RandomForestRegressor | consumption, power_factor, freq, peak_hour | R² = 1.0000, MAE = 0.02 |
| **Model 5** | Parking Occupancy Predictor | `occupancy_percentage` | RandomForestRegressor | location_id, occupied, available, turnover | R² = 1.0000, MAE = 0.001 |
| **Model 6** | Pollution / AQI Predictor | `aqi` | RandomForestRegressor | pm2_5, pm10, co, no2, so2, o3, temp, humidity | R² = 0.9999, MAE = 0.13 |
| **Model 7** | Transport Demand Predictor | `passenger_count` | RandomForestRegressor | route_id, delay_minutes, peak_hour | R² = 0.8190, MAE = 10.05 |
| **Model 8** | Transport Delay Predictor | `severe_delay` | RandomForestClassifier | route_id, passenger_count, peak_hour | Accuracy = 85.70%, F1 = 0.52 |
| **Model 9** | Complaint Priority Classifier | `priority_encoded` | RandomForestClassifier | citizen_id, category_id, department_id | Accuracy = 24.80% |
| **Model 10** | Multi-Metric Anomaly Detector | `is_anomaly` | IsolationForest | pm2_5, pm10, co, no2, so2, o3 | Contamination = 5.0% |

---

## 2. ML Pipeline Lifecycle

Every model executes the standardized 12-stage pipeline:
```text
Dataset -> Data Cleaning -> Validation -> Preprocessing -> Feature Engineering -> Train/Test Split -> Model Training -> Evaluation -> Model Saving -> Prediction -> Prediction Logging -> Dashboard Visualization
```
