from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class ProjectResponse(BaseModel):
    project_name: str
    project_start: str 
    project_end: str
    company: str
    description: str
    project_value: int
    area: str

    model_config = ConfigDict(from_attributes=True)

class PaginationMetadata(BaseModel):
    total_count: int
    page: int
    per_page: int
    total_pages: int

class PaginatedProjectResponse(BaseModel):
    items: List[ProjectResponse]
    metadata: PaginationMetadata

