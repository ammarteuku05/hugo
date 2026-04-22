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

    def _table_exists(self, cursor: sqlite3.Cursor, table_name: str) -> bool:
        cursor.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ? LIMIT 1",
            (table_name,),
        )
        return cursor.fetchone() is not None

    def find_projects(
        self, 
        area: Optional[str] = None, 
        keyword: Optional[str] = None, 
        page: Optional[int] = None, 
        per_page: Optional[int] = None
    ) -> Dict[str, Any]:
        conn = self._get_connection()
        cursor = conn.cursor()

        has_normalized_schema = self._table_exists(cursor, "companies") and self._table_exists(
            cursor, "project_area_map"
        )

        params: List[Any] = []

        if has_normalized_schema:
            base_join = """
                FROM projects p
                LEFT JOIN companies c ON p.company_id = c.company_id
                LEFT JOIN project_area_map pam ON p.project_id = pam.project_id
            """

            filter_clause = "WHERE 1=1"
            if area:
                filter_clause += " AND pam.area = ?"
                params.append(area)
            if keyword:
                filter_clause += " AND p.project_name LIKE ?"
                params.append(f"%{keyword}%")

            count_query = f"SELECT COUNT(DISTINCT p.project_id) {base_join} {filter_clause}"
            cursor.execute(count_query, params)
            total_count = cursor.fetchone()[0]

            data_query = f"""
                SELECT
                    p.project_id,
                    p.project_name,
                    p.project_start,
                    p.project_end,
                    c.company_name AS company,
                    p.description,
                    p.project_value,
                    GROUP_CONCAT(pam.area, ', ') AS area
                {base_join}
                {filter_clause}
                GROUP BY p.project_id
                ORDER BY p.project_value DESC
            """
        else:
            filter_clause = "WHERE 1=1"
            if area:
                filter_clause += " AND p.area = ?"
                params.append(area)
            if keyword:
                filter_clause += " AND p.project_name LIKE ?"
                params.append(f"%{keyword}%")

            count_query = f"SELECT COUNT(*) FROM projects p {filter_clause}"
            cursor.execute(count_query, params)
            total_count = cursor.fetchone()[0]

            data_query = f"""
                SELECT
                    p.id AS project_id,
                    p.project_name,
                    p.project_start,
                    p.project_end,
                    p.company AS company,
                    p.description,
                    p.project_value,
                    p.area
                FROM projects p
                {filter_clause}
                ORDER BY p.id ASC
            """

        data_params = list(params)
        if page is not None and per_page is not None:
            offset = (page - 1) * per_page
            data_query += " LIMIT ? OFFSET ?"
            data_params.extend([per_page, offset])

        cursor.execute(data_query, data_params)
        rows = cursor.fetchall()
        conn.close()

        return {"items": [dict(row) for row in rows], "total_count": total_count}
