from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IProjectService(ABC):
    @abstractmethod
    def list_projects(
        self, 
        area: Optional[str] = None, 
        keyword: Optional[str] = None, 
        page: Optional[int] = None, 
        per_page: Optional[int] = None
    ) -> Dict[str, Any]:
        pass

