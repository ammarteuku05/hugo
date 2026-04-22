from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
import math
from app.api.schemas import PaginatedProjectResponse, PaginationMetadata
from app.api.deps import get_project_service
from app.interfaces.service import IProjectService

router = APIRouter()

@router.get("", response_model=PaginatedProjectResponse)
def get_projects(
    area: Optional[str] = Query(None, description="Filter projects by area"),
    keyword: Optional[str] = Query(None, description="Search project name"),
    page: Optional[int] = Query(None, ge=1, description="Pagination page (1-based)"),
    per_page: Optional[int] = Query(None, ge=1, description="Projects per page"),
    service: IProjectService = Depends(get_project_service)
):
    try:
        actual_page = page or 1
        actual_per_page = per_page or 20
        
        # If both are None in the request, logic in frontend determines if it wants "all" or specific pagination.
        # But the API will now always return metadata.
        if page is None and per_page is None:
            # Reverting to "no pagination" behavior if both are missing if desired, 
            # but usually better to have default. 
            # The repo handles None as "unlimited" if we pass None.
            # Let's keep defaults for consistent response structure.
            pass

        result = service.list_projects(
            area=area,
            keyword=keyword,
            page=actual_page,
            per_page=actual_per_page
        )
        
        items = result["items"]
        total_count = result["total_count"]
        total_pages = math.ceil(total_count / actual_per_page) if actual_per_page > 0 else 1

        return {
            "items": items,
            "metadata": {
                "total_count": total_count,
                "page": actual_page,
                "per_page": actual_per_page,
                "total_pages": total_pages
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

