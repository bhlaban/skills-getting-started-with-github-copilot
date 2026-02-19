"""Tests for the GET /activities endpoint."""


EXPECTED_ACTIVITIES = [
    "Chess Club",
    "Programming Class",
    "Gym Class",
    "Soccer Team",
    "Swimming Club",
    "Art Club",
    "Drama Club",
    "Math Olympiad",
    "Debate Club",
]

REQUIRED_FIELDS = ["description", "schedule", "max_participants", "participants"]


def test_get_activities_returns_all(client):
    """GET /activities should return all 9 activities."""
    # Arrange — no additional setup needed

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == set(EXPECTED_ACTIVITIES)


def test_activity_has_required_fields(client):
    """Each activity should contain description, schedule, max_participants, and participants."""
    # Arrange — no additional setup needed

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for name, details in data.items():
        for field in REQUIRED_FIELDS:
            assert field in details, f"Activity '{name}' is missing field '{field}'"


def test_activity_participants_is_list(client):
    """The participants field should be a list for every activity."""
    # Arrange — no additional setup needed

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for name, details in data.items():
        assert isinstance(details["participants"], list), (
            f"Activity '{name}' participants should be a list"
        )
