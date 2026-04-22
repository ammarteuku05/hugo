from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class ProjectResponse(BaseModel):
    project_id: str
    project_name: str
    project_start: str
    project_end: str
    company: Optional[str] = None       # LEFT JOIN from companies table
    description: Optional[str] = None   # Can be null
    project_value: int
    area: Optional[str] = None         # GROUP_CONCAT from project_area_map; can be null

    model_config = ConfigDict(from_attributes=True)

class PaginationMetadata(BaseModel):
    total_count: int
    page: int
    per_page: int
    total_pages: int

class PaginatedProjectResponse(BaseModel):
    items: List[ProjectResponse]
    metadata: PaginationMetadata
