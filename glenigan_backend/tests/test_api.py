import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.api.deps import get_project_service
from app.interfaces.service import IProjectService

# Mock service
mock_service = MagicMock(spec=IProjectService)

def override_get_project_service():
    return mock_service

app.dependency_overrides[get_project_service] = override_get_project_service

client = TestClient(app)

def test_get_projects_success():
    # Setup mock
    mock_service.list_projects.return_value = {
        "items": [{"project_name": "Test Project", "project_start": "2024", "project_end": "2025", "company": "C", "description": "D", "project_value": 100, "area": "A"}],
        "total_count": 1
    }
    
    response = client.get("/projects?page=1&per_page=10")
    
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "metadata" in data
    assert data["metadata"]["total_count"] == 1
    assert data["metadata"]["total_pages"] == 1

def test_get_projects_filter():
    mock_service.list_projects.return_value = {"items": [], "total_count": 0}
    
    response = client.get("/projects?area=London&keyword=Search")
    
    assert response.status_code == 200
    mock_service.list_projects.assert_called_with(
        area="London", 
        keyword="Search", 
        page=1, 
        per_page=20
    )

def test_get_projects_error():
    mock_service.list_projects.side_effect = Exception("Internal error")
    
    response = client.get("/projects")
    
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal error"
