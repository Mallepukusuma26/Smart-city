"""
Authentication Unit Tests.
"""
def test_valid_citizen_login(client):
    res = client.post("/api/auth/login", json={"login_identifier": "cit@test.com", "password": "Pass123!"})
    assert res.status_code == 200
    data = res.get_json()
    assert "token" in data["data"]
    assert data["data"]["user"]["username"] == "test_citizen"

def test_valid_officer_login(client):
    res = client.post("/api/auth/login", json={"login_identifier": "off@test.com", "password": "Pass123!"})
    assert res.status_code == 200
    data = res.get_json()
    assert data["data"]["redirect_url"] == "/officer/dashboard"

def test_invalid_login_password(client):
    res = client.post("/api/auth/login", json={"login_identifier": "cit@test.com", "password": "WrongPassword"})
    assert res.status_code == 401
