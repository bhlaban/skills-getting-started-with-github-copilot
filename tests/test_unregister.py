"""Tests for the DELETE /activities/{name}/unregister endpoint."""


def test_unregister_success(client):
    """An existing participant should be able to unregister from an activity."""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # pre-seeded participant

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert email in data["message"]
    assert activity in data["message"]

    # Verify the participant is no longer in the activity
    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity]["participants"]


def test_unregister_not_signed_up(client):
    """Unregistering a student who is not signed up should return 400."""
    # Arrange
    activity = "Chess Club"
    email = "nobody@mergington.edu"  # not a participant

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"].lower()


def test_unregister_activity_not_found(client):
    """Unregistering from a non-existent activity should return 404."""
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
