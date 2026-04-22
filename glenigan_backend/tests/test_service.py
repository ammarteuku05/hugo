import pytest
from unittest.mock import MagicMock
from app.services.project_service import ProjectService
from app.interfaces.repository import IProjectRepository

@pytest.fixture
def mock_repo():
    return MagicMock(spec=IProjectRepository)

@pytest.fixture
def service(mock_repo):
    return ProjectService(mock_repo)

def test_list_projects_calls_repo(service, mock_repo):
    # Setup mock return value
    mock_data = {
        "items": [{"project_name": "Test"}],
        "total_count": 1
    }
    mock_repo.find_projects.return_value = mock_data
    
    # Call service
    result = service.list_projects(area="London", keyword="Search", page=1, per_page=10)
    
    # Assertions
    mock_repo.find_projects.assert_called_once_with(
        area="London", 
        keyword="Search", 
        page=1, 
        per_page=10
    )
    assert result == mock_data

def test_list_projects_default_params(service, mock_repo):
    mock_repo.find_projects.return_value = {"items": [], "total_count": 0}
    
    service.list_projects()
    
    mock_repo.find_projects.assert_called_once_with(
        area=None, 
        keyword=None, 
        page=None, 
        per_page=None
    )
