"""Tests for the POST /activities/{name}/signup endpoint."""


def test_signup_success(client):
    """A new student should be able to sign up for an activity."""
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert email in data["message"]
    assert activity in data["message"]

    # Verify the participant now appears in the activity
    activities_response = client.get("/activities")
    assert email in activities_response.json()[activity]["participants"]


def test_signup_duplicate(client):
    """Signing up the same student twice should return 400."""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # already registered

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_signup_activity_not_found(client):
    """Signing up for a non-existent activity should return 404."""
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
