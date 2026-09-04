# Smart City Operations Platform — Architectural & Technical Design Document

Comprehensive architecture guide detailing directory layout, database schema entity-relationship definitions, security model, ML pipelines, and rule engine.

---

## 1. Modular Directory Layout

```text
smart-city-platform/
├── backend/
│   ├── app/
│   │   ├── config/ (settings.py, logging_config.py, constants.py)
│   │   ├── models/ (20+ SQLAlchemy ORM Entities)
│   │   ├── schemas/ (Validation & Serialization Schemas)
│   │   ├── repositories/ (Data Access Abstractions)
│   │   ├── services/ (Domain Business Services & Algorithms)
│   │   ├── routes/ (Flask REST Blueprints)
│   │   ├── middleware/ (Auth, Audit, Rate Limiting, Error Handlers)
│   │   ├── security/ (JWT Tokens, Password Hashes, RBAC Decorators)
│   │   ├── analytics/ (KPI Engine, Trend Calculators)
│   │   ├── alerts/ (Rule Engine, Threshold Logic)
│   │   ├── notifications/ (Dispatcher, Broadcast Announcements)
│   │   ├── reports/ (ReportLab PDF, CSV, HTML Generators)
│   │   └── ml/ (Local Scikit-Learn Pipelines & Inference Engine)
│   ├── datasets/ (Synthetic relational CSV datasets)
│   ├── trained_models/ (Persisted Joblib ML artifacts)
│   ├── tests/ (Pytest test suite)
│   └── run.py
├── frontend/
│   ├── citizen/ (Citizen Portal pages)
│   ├── officer/ (Officer Portal pages)
│   ├── admin/ (Admin Master Portal pages)
│   ├── auth/ (Authentication pages)
│   ├── css/ (Design tokens & theme styles)
│   └── js/ (API client & modular page logic)
├── scripts/ (Dataset generator, ML trainer, DB seeder, Health check, LOC analyzer)
└── docs/ (Architecture & API Manuals)
```

---

## 2. Security & RBAC Enforcers

Backend role verification is strictly enforced on Flask route endpoints using decorator wrappers:
- `@citizen_required`: Allows `CITIZEN` and `ADMIN` roles.
- `@officer_required`: Allows `OFFICER` and `ADMIN` roles.
- `@admin_required`: Allows strictly `ADMIN` role.

Any attempt by a `CITIZEN` user to invoke officer or admin routes yields HTTP `403 Forbidden`.

---

## 3. Database Entity Relationship Overview

- **User System**: `User 1:N UserRole`, `User 1:1 Citizen`, `User 1:1 Officer`, `Officer N:1 Department`.
- **Complaint System**: `Complaint N:1 Citizen`, `Complaint N:1 Department`, `Complaint N:1 Officer`, `Complaint 1:N ComplaintHistory`.
- **Infrastructure Entities**: `Road 1:N TrafficRecord`, `WasteBin 1:N WasteRecord`, `WaterTank 1:N WaterRecord`, `Transformer 1:N ElectricityRecord`, `ParkingLocation 1:N ParkingRecord`, `TransportRoute 1:N TransportVehicle`, `PollutionStation 1:N PollutionRecord`.
- **Alert & Security**: `AlertRule 1:N SystemAlert`, `User 1:N UserNotification`, `User 1:N AuditLog`.
