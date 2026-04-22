import pytest
import sqlite3
import os
from app.repositories.sqlite_project_repository import SqliteProjectRepository

@pytest.fixture
def repo():
    # Use a temporary file for testing instead of :memory:
    # because :memory: creates a new DB for every connection.
    db_path = "test_glenigan_takehome_FS.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        
    repo = SqliteProjectRepository(db_path)
    
    # Setup schema
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_start TEXT NOT NULL,
            project_end TEXT NOT NULL,
            company TEXT NOT NULL,
            description TEXT NOT NULL,
            project_value INTEGER NOT NULL,
            area TEXT NOT NULL
        )
    """)
    
    # Insert test data
    projects = [
        ("Project A", "2024-01-01", "2024-12-31", "Company X", "Desc A", 1000, "London"),
        ("Project B", "2024-02-01", "2024-11-30", "Company Y", "Desc B", 2000, "Manchester"),
        ("Project C", "2024-03-01", "2024-10-31", "Company X", "Desc C", 3000, "London"),
    ]
    conn.executemany(
        "INSERT INTO projects (project_name, project_start, project_end, company, description, project_value, area) VALUES (?, ?, ?, ?, ?, ?, ?)",
        projects
    )
    conn.commit()
    conn.close()
    
    yield repo
    
    # Cleanup
    if os.path.exists(db_path):
        os.remove(db_path)


def test_find_projects_all(repo):
    result = repo.find_projects()
    assert len(result["items"]) == 3
    assert result["total_count"] == 3

def test_find_projects_filter_area(repo):
    result = repo.find_projects(area="London")
    assert len(result["items"]) == 2
    assert result["total_count"] == 2
    assert result["items"][0]["project_name"] == "Project A"

def test_find_projects_filter_keyword(repo):
    result = repo.find_projects(keyword="Project B")
    assert len(result["items"]) == 1
    assert result["total_count"] == 1
    assert result["items"][0]["area"] == "Manchester"

def test_find_projects_pagination(repo):
    # Page 1, 2 per page
    result = repo.find_projects(page=1, per_page=2)
    assert len(result["items"]) == 2
    assert result["total_count"] == 3
    
    # Page 2, 2 per page
    result = repo.find_projects(page=2, per_page=2)
    assert len(result["items"]) == 1
    assert result["total_count"] == 3
    assert result["items"][0]["project_name"] == "Project C"

def test_find_projects_no_results(repo):
    result = repo.find_projects(area="NonExistent")
    assert len(result["items"]) == 0
    assert result["total_count"] == 0
