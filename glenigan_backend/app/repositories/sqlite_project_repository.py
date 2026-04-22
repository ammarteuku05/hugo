import sqlite3
import math
from typing import List, Optional, Dict, Any
from app.interfaces.repository import IProjectRepository

class SqliteProjectRepository(IProjectRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def find_projects(
        self, 
        area: Optional[str] = None, 
        keyword: Optional[str] = None, 
        page: Optional[int] = None, 
        per_page: Optional[int] = None
    ) -> Dict[str, Any]:
        conn = self._get_connection()
        cursor = conn.cursor()

        # Base filter logic
        filter_query = " WHERE 1=1"
        params = []

        if area:
            filter_query += " AND area = ?"
            params.append(area)
        
        if keyword:
            filter_query += " AND project_name LIKE ?"
            params.append(f"%{keyword}%")

        # 1. Get Total Count
        count_query = "SELECT COUNT(*) FROM projects" + filter_query
        cursor.execute(count_query, params)
        total_count = cursor.fetchone()[0]

        # 2. Get Paginated Data
        data_query = "SELECT * FROM projects" + filter_query
        data_params = list(params)

        if page is not None and per_page is not None:
            limit = per_page
            offset = (page - 1) * per_page
            data_query += " LIMIT ? OFFSET ?"
            data_params.extend([limit, offset])

        cursor.execute(data_query, data_params)
        rows = cursor.fetchall()
        
        items = [dict(row) for row in rows]
        conn.close()
        
        return {
            "items": items,
            "total_count": total_count
        }

