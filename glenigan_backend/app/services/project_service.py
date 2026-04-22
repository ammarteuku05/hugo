from typing import List, Optional, Dict, Any
from app.interfaces.service import IProjectService
from app.interfaces.repository import IProjectRepository

class ProjectService(IProjectService):
    def __init__(self, repository: IProjectRepository):
        self.repository = repository

    def list_projects(
        self, 
        area: Optional[str] = None, 
        keyword: Optional[str] = None, 
        page: Optional[int] = None, 
        per_page: Optional[int] = None
    ) -> Dict[str, Any]:
        return self.repository.find_projects(
            area=area,
            keyword=keyword,
            page=page,
            per_page=per_page
        )

