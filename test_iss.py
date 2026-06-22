import requests

def test_iss_api_returns_200():
    """Verify the ISS API is reachable and returns valid data."""
    response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert "iss_position" in data
    assert "latitude" in data["iss_position"]
    assert "longitude" in data["iss_position"]
