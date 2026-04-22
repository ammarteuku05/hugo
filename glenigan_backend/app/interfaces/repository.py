from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IProjectRepository(ABC):
    @abstractmethod
    def find_projects(
        self, 
        area: Optional[str] = None, 
        keyword: Optional[str] = None, 
        page: Optional[int] = 1, 
        per_page: Optional[int] = 20
    ) -> Dict[str, Any]: # Returns {'items': [...], 'total_count': ...}
        pass

