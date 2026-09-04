# AI-Powered Smart City Operations & Management Platform

Enterprise-scale, full-stack Smart City Operations and Management System featuring role-based dashboards (Citizen, Officer, Admin), 20 real-time operational modules, 10 local Machine Learning prediction pipelines, rule-based alert engine, multi-format reporting, and immutable audit logs.

---

## Executive Summary & Capabilities

- **3 Role-Based Portals**:
  - **Citizen Portal**: `/citizen/dashboard.html` — View city infrastructure status, submit & track complaints, view traffic, parking, water, transport schedules, and pollution levels.
  - **Officer Portal**: `/officer/dashboard.html` — Manage department-specific tasks, resolve assigned complaints, track active incidents, receive emergency alerts, and view department performance.
  - **Admin Portal**: `/admin/dashboard.html` — Master management of users, officers, citizens, departments, services, ML prediction center, audit logs, and city-wide configuration.
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

---

## 1. System Requirements
- Python 3.11+
- SQLite3
- Git

---

## 2. Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Mallepukusuma26/Smart-city.git
cd Smart-city

# Install direct project dependencies
pip install -r requirements.txt

# Or install from reproducible lockfile
pip install -r requirements-lock.txt
```

---

## 3. Database & ML Initialization

```bash
# 1. Generate local synthetic datasets
python scripts/generate_datasets.py

# 2. Train local machine learning models
python scripts/train_models.py

# 3. Seed SQLite database with demo accounts and infrastructure entities
python scripts/seed_db.py
```

---

## 4. Running the Web Application

```bash
python backend/run.py
```

Open your browser to the central application URL:
👉 **[http://localhost:5000/](http://localhost:5000/)**

The application will present the **Central Authentication Portal** and automatically route you to the appropriate dashboard based on your user role:
- **Citizen Portal**: `http://localhost:5000/citizen/dashboard.html`
- **Officer Portal**: `http://localhost:5000/officer/dashboard.html`
- **Admin Portal**: `http://localhost:5000/admin/dashboard.html`

---

## 5. Demo Credentials

| Role | Username / Email | Password | Assigned Portal |
| :--- | :--- | :--- | :--- |
| **Admin Master** | `admin@smartcity.gov` | `AdminPass123!` | `/admin/dashboard.html` |
| **Traffic Officer** | `officer.traffic@smartcity.gov` | `OfficerPass123!` | `/officer/dashboard.html` |
| **Water Officer** | `officer.water@smartcity.gov` | `OfficerPass123!` | `/officer/dashboard.html` |
| **Waste Officer** | `officer.waste@smartcity.gov` | `OfficerPass123!` | `/officer/dashboard.html` |
| **Power Officer** | `officer.elec@smartcity.gov` | `OfficerPass123!` | `/officer/dashboard.html` |
| **Citizen User** | `citizen1@example.com` | `CitizenPass123!` | `/citizen/dashboard.html` |

---

## 6. Testing, Health Check & Coverage

```bash
# Run automated system health check (5 core component checks)
python scripts/health_check.py

# Run Pytest suite (638 test scenarios)
pytest

# Run test coverage reporting
pytest --cov=backend --cov-report=term-missing

# Run LOC verification counter
python scripts/count_loc.py
```

---

## 7. Containerized Deployment (Docker)

```bash
# Build Docker image
docker build -t smart-city-platform .

# Run container
docker run -p 5000:5000 smart-city-platform
```

---

## 8. Project Architecture

```text
Smart City/
├── backend/
│   ├── app/
│   │   ├── config/ (settings.py, logging_config.py, constants.py)
│   │   ├── models/ (60+ SQLAlchemy ORM entities & sub-records)
│   │   ├── schemas/ (Validation & serialization dataclasses)
│   │   ├── repositories/ (Data access layer abstractions)
│   │   ├── services/ (Domain business services & algorithms)
│   │   ├── routes/ (Flask REST blueprints for all 20 modules)
│   │   ├── middleware/ (Auth, Audit logger, Rate limiter, Error handlers)
│   │   ├── security/ (JWT, Password hashing, RBAC decorators)
│   │   ├── analytics/ (Multi-dimensional KPI calculators)
│   │   ├── alerts/ (Real-time rule engine & severity matrix)
│   │   ├── notifications/ (Notification & announcement dispatcher)
│   │   ├── reports/ (ReportLab PDF, CSV, HTML generators)
│   │   └── ml/ (10 scikit-learn model pipelines & predictors)
│   ├── datasets/ (Generated synthetic CSV datasets)
│   ├── trained_models/ (Persisted .joblib trained model artifacts)
│   ├── tests/ (Comprehensive pytest test suite)
│   └── run.py
├── frontend/
│   ├── citizen/ (15 dedicated Citizen portal views)
│   ├── officer/ (12 dedicated Officer portal views)
│   ├── admin/ (20 dedicated Admin portal views)
│   ├── auth/ (Login & Registration views)
│   ├── css/ (main.css, citizen.css, officer.css, admin.css, components.css)
│   └── js/ (api.js, auth.js, citizen.js, officer.js, admin.js)
├── scripts/
│   ├── generate_datasets.py (Synthetic data generator)
│   ├── train_models.py (ML pipeline trainer)
│   ├── seed_db.py (Database population script)
│   ├── health_check.py (System integrity verifier)
│   └── count_loc.py (LOC analyzer)
├── docs/ (PROJECT_AUDIT.md, API_DOCUMENTATION.md, ARCHITECTURE.md, USER_GUIDE.md, ML_MODELS.md)
├── requirements.txt
├── requirements-lock.txt
├── Dockerfile
├── pytest.ini
└── README.md

```
