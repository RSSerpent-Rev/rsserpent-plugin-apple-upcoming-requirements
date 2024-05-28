from starlette.testclient import TestClient


def test_route(client: TestClient) -> None:
    """Test `rsserpent_plugin_apple_upcoming_requirements.route`."""
    response = client.get("/apple-upcoming-requirements")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    assert "Apple developer news - Upcoming requirements" in response.text
