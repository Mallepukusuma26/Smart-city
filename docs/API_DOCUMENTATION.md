# Smart City Operations Platform — REST API Reference Manual

Comprehensive documentation for all REST API namespaces, authentication flow, headers, status codes, and JSON response models.

---

## 1. Global Headers & Authentication

All protected endpoints require either a JWT Bearer Token in the `Authorization` header or a valid Flask Session cookie.

```http
Authorization: Bearer <jwt_token_string>
Content-Type: application/json
```

---

## 2. Authentication API Namespace (`/api/auth`)

### `POST /api/auth/register`
Registers a new Citizen or Officer user account.

**Request Payload:**
```json
{
  "username": "citizen_john",
  "email": "john@example.com",
  "password": "Password123!",
  "full_name": "John Smith",
  "role": "CITIZEN",
  "phone_number": "+1-555-0199",
  "address": "123 Smart Ave"
}
```

**Response (201 Created):**
```json
{
  "message": "Citizen registration successful.",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsIn...",
    "user": {
      "id": 1,
      "username": "citizen_john",
      "roles": ["CITIZEN"]
    }
  }
}
```

### `POST /api/auth/login`
Authenticates a user account and returns JWT token & redirect path.

**Request Payload:**
```json
{
  "login_identifier": "admin@smartcity.gov",
  "password": "AdminPass123!"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful.",
  "data": {
    "token": "eyJhbGciOiJIUzI1...",
    "redirect_url": "/admin/dashboard",
    "user": {
      "id": 1,
      "username": "admin",
      "roles": ["ADMIN"]
    }
  }
}
```

---

## 3. Citizen Portal API Namespace (`/api/citizen`)

### `GET /api/citizen/dashboard`
Fetches citizen profile, personal complaint stats, city service overview, and recent notifications.
Requires `CITIZEN` role. Unauthorized requests yield `403 Forbidden`.

### `POST /api/citizen/complaints`
Submits a new civic complaint.
Requires `CITIZEN` role.

---

## 4. Officer Portal API Namespace (`/api/officer`)

### `GET /api/officer/dashboard`
Fetches department officer command center data, assigned complaint queue, and department performance score.
Requires `OFFICER` role.

### `POST /api/officer/complaints/<id>/update`
Updates status of an assigned complaint (`IN_PROGRESS`, `RESOLVED`, `ESCALATED`) with officer remarks.

---

## 5. Admin Master API Namespace (`/api/admin`)

### `GET /api/admin/dashboard`
Returns platform-wide KPIs, total users, trained ML models, active emergencies, and security audit logs.
Requires `ADMIN` role.

---

## 6. Smart City Services API Namespace (`/api/services`)

- `GET /api/services/traffic/overview`
- `GET /api/services/waste/overview`
- `GET /api/services/water/overview`
- `GET /api/services/electricity/overview`
- `GET /api/services/parking/overview`
- `GET /api/services/transport/overview`
- `GET /api/services/pollution/overview`
- `POST /api/services/ai/predict`
- `GET /api/services/reports/export?module=complaints&format=csv`
