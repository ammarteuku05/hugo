import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.api.deps import get_project_service
from app.interfaces.service import IProjectService


@pytest.fixture
def mock_service():
    return MagicMock(spec=IProjectService)


@pytest.fixture
def client(mock_service):
    app.dependency_overrides[get_project_service] = lambda: mock_service
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_root_healthcheck(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Glenigan Project API is running" in response.json()["message"]


def test_get_projects_success(client, mock_service):
    mock_service.list_projects.return_value = {
        "items": [
            {
                "project_id": "1",
                "project_name": "Test Project",
                "project_start": "2024",
                "project_end": "2025",
                "company": "C",
                "description": "D",
                "project_value": 100,
                "area": "A",
            }
        ],
        "total_count": 1,
    }

    response = client.get("/projects?page=1&per_page=10")

    assert response.status_code == 200
    data = response.json()
    assert data["items"][0]["project_id"] == "1"
    assert data["metadata"]["total_pages"] == 1
    mock_service.list_projects.assert_called_once_with(
        area=None, keyword=None, page=1, per_page=10
    )


def test_get_projects_default_pagination(client, mock_service):
    mock_service.list_projects.return_value = {"items": [], "total_count": 0}

    response = client.get("/projects")

    assert response.status_code == 200
    assert response.json()["metadata"]["page"] == 1
    assert response.json()["metadata"]["per_page"] == 20
    mock_service.list_projects.assert_called_once_with(
        area=None, keyword=None, page=1, per_page=20
    )


def test_get_projects_error(client, mock_service):
    mock_service.list_projects.side_effect = Exception("Internal error")

    response = client.get("/projects")

    assert response.status_code == 500
    assert response.json()["detail"] == "Internal error"
