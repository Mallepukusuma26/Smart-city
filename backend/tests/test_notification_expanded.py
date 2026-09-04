"""
Automated Pytest for Notification.
"""
def test_notification_overview(client):
    login_res = client.post("/api/auth/login", json={"login_identifier": "cit@test.com", "password": "Pass123!"})
    token = login_res.get_json()["data"]["token"]
    res = client.get("/api/notification/overview", headers={"Authorization": f"Bearer {token}"} )
    assert res.status_code == 200
