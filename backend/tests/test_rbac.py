"""
Role-Based Access Control (RBAC) Security Verification Tests.
"""
def test_unauthenticated_access_denied(client):
    res = client.get("/api/citizen/dashboard")
    assert res.status_code == 401

def test_citizen_accessing_admin_endpoint_denied(client):
    # Login as citizen
    login_res = client.post("/api/auth/login", json={"login_identifier": "cit@test.com", "password": "Pass123!"})
    token = login_res.get_json()["data"]["token"]

    # Attempt accessing admin API endpoint
    res = client.get("/api/admin/dashboard", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 403

def test_officer_accessing_admin_endpoint_denied(client):
    login_res = client.post("/api/auth/login", json={"login_identifier": "off@test.com", "password": "Pass123!"})
    token = login_res.get_json()["data"]["token"]

    res = client.get("/api/admin/dashboard", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 403

def test_admin_accessing_admin_endpoint_allowed(client):
    login_res = client.post("/api/auth/login", json={"login_identifier": "adm@test.com", "password": "Pass123!"})
    token = login_res.get_json()["data"]["token"]

    res = client.get("/api/admin/dashboard", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
