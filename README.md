# AI-Powered Smart City Operations & Management Platform

Enterprise-scale, full-stack Smart City Operations and Management System featuring role-based dashboards (Citizen, Officer, Admin), 20 real-time operational modules, 10 local Machine Learning prediction pipelines, rule-based alert engine, multi-format reporting, and immutable audit logs.

## Overview & Capabilities

- **3 Role-Based Portals**:
  - **Citizen Portal**: `/citizen/dashboard` — View city infrastructure status, submit & track complaints, view traffic, parking, water, transport schedules, and pollution levels.
  - **Officer Portal**: `/officer/dashboard` — Manage department-specific tasks, resolve assigned complaints, track active incidents, receive emergency alerts, and view department performance.
  - **Admin Portal**: `/admin/dashboard` — Master management of users, officers, citizens, departments, services, ML prediction center, audit logs, and city-wide configuration.
- **20 Operational Smart City Modules**:
  1. Traffic Management & Congestion Analytics
  2. Waste Management & Bin Overflow Control
  3. Water Supply & Leakage Detection
  4. Electricity Demand & Power Grid Load
  5. Parking Occupancy & Space Reservation
  6. Public Transport & Transit Management
  7. Pollution & Air Quality Index (AQI) Monitoring
  8. Complaint Lifecycle Management
  9. Emergency & Incident Command Center
  10. Infrastructure & City Assets Tracker
  11. Real-Time Alert Engine
  12. Notification Dispatcher
  13. Multi-Dimensional Analytics Engine
  14. AI / Machine Learning Prediction Center (10 local models)
  15. Enterprise Report Engine (PDF, CSV, HTML)
  16. User Account Management
  17. Officer & Staff Management
  18. Department Hierarchy & Access Control
  19. Immutable Audit Logging
  20. System Configuration & Operational Settings

## Local ML Models (No External APIs Required)
1. **Traffic Congestion Model**: Random Forest Regressor / XGBoost for congestion index prediction.
2. **Waste Generation Model**: Bin overflow risk classifier.
3. **Water Demand Model**: Hourly consumption forecasting.
4. **Electricity Demand Model**: Grid peak load forecasting.
5. **Parking Occupancy Model**: Availability predictor.
6. **Pollution / AQI Model**: Air quality index forecaster.
7. **Transport Passenger Demand Model**: Transit volume forecasting.
8. **Transport Delay Model**: Route delay classifier.
9. **Complaint Priority Classifier**: Text and metadata urgency classifier.
10. **Multi-Metric Anomaly Detector**: Isolation Forest anomaly detection across municipal sensor data.

## Getting Started

### 1. Requirements
- Python 3.11+
- SQLite3

### 2. Setup & Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Generate synthetic datasets
python scripts/generate_datasets.py

# Train local ML models
python scripts/train_models.py

# Initialize and seed database
python scripts/seed_db.py
```

### 3. Running the Server
```bash
python backend/run.py
```
Access portals:
- Citizen Portal: `http://localhost:5000/citizen/dashboard`
- Officer Portal: `http://localhost:5000/officer/dashboard`
- Admin Portal: `http://localhost:5000/admin/dashboard`

### 4. Demo Credentials
- **Admin**: `admin@smartcity.gov` / `AdminPass123!`
- **Traffic Officer**: `officer.traffic@smartcity.gov` / `OfficerPass123!`
- **Water Officer**: `officer.water@smartcity.gov` / `OfficerPass123!`
- **Waste Officer**: `officer.waste@smartcity.gov` / `OfficerPass123!`
- **Electricity Officer**: `officer.elec@smartcity.gov` / `OfficerPass123!`
- **Transport Officer**: `officer.transport@smartcity.gov` / `OfficerPass123!`
- **Pollution Officer**: `officer.pollution@smartcity.gov` / `OfficerPass123!`
- **Citizen**: `citizen1@example.com` / `CitizenPass123!`

### 5. Running Health Check & LOC Counter
```bash
# Verify system integrity
python scripts/health_check.py

# Count meaningful lines of code
python scripts/count_loc.py

# Run test suite
pytest backend/tests/
```
