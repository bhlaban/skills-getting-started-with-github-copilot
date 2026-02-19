import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

# Snapshot of the original activities state for test isolation
_original_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict before each test."""
    # Arrange (shared) — restore pristine state
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
    yield
    # Teardown — restore again for safety
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))


@pytest.fixture
def client():
    """Provide a TestClient instance for the FastAPI app."""
    return TestClient(app)
