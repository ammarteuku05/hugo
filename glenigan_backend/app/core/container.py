import sqlite3
from typing import Optional
from app.core.config import settings
from app.repositories.sqlite_project_repository import SqliteProjectRepository
from app.services.project_service import ProjectService
from app.interfaces.service import IProjectService

class Container:
    _instance: Optional['Container'] = None

    def __init__(self):
        # In a real app, we might handle connection pools. 
        # For SQLite, we can just pass the DB path to the repository.
        self.db_path = settings.DATABASE_PATH
        
        # Initialize Repositories
        self.project_repository = SqliteProjectRepository(self.db_path)
        
        # Initialize Services
        self.project_service: IProjectService = ProjectService(self.project_repository)

    @classmethod
    def get_instance(cls) -> 'Container':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
