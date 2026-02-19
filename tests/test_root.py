"""Tests for the root endpoint (GET /)."""


def test_root_redirects_to_index(client):
    """GET / should redirect to /static/index.html."""
    # Arrange — no additional setup needed

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
