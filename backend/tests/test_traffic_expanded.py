"""
Automated Pytest for Traffic.
"""
def test_traffic_overview(client):
    login_res = client.post("/api/auth/login", json={"login_identifier": "cit@test.com", "password": "Pass123!"})
    token = login_res.get_json()["data"]["token"]
    res = client.get("/api/traffic/overview", headers={"Authorization": f"Bearer {token}"} )
    assert res.status_code == 200
