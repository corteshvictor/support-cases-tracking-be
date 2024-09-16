from shared.infrastructure.db_connection import DBConnection
from support_cases.domain.support_cases_repository import SupportCasesRepository
from support_cases.domain.support_cases_entity import SupportCases, SupportCasesCreate, SupportCasesFilter

class SupportCasesPersistenceRepository(SupportCasesRepository):
    def __init__(self):
        self.conn = DBConnection().get_connection()
    
    def create(self, support_case: SupportCasesCreate) -> SupportCases:
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO support_cases (number, description, status, priority, database_name, schema_name, query_executed, executed_by, requester)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
                """,
                (
                    support_case.number,
                    support_case.description,
                    support_case.status.value,
                    support_case.priority.value,
                    support_case.database_name,
                    support_case.schema_name,
                    support_case.query_executed,
                    support_case.executed_by,
                    support_case.requester
                )
            )

            support_case_id = cursor.fetchone()[0]
            self.conn.commit()

            return self.get_by_id(support_case_id)

    def get_all(self, filters: SupportCasesFilter) -> dict:
        cursor = self.conn.cursor()
        PAGE_SIZE = 10

        # Base query with filters
        query = """
            SELECT * FROM support_cases WHERE 1=1
        """
        params = []

        # Apply filters
        if filters.status:
            query += " AND status = %s"
            params.append(filters.status.value)
        if filters.priority:
            query += " AND priority = %s"
            params.append(filters.priority.value)
        if filters.description:
            query += " AND description ILIKE %s"
            params.append(f"%{filters.description}%")
        if filters.database_name:
            query += " AND database_name ILIKE %s"
            params.append(f"%{filters.database_name}%")
        if filters.requester:
            query += " AND requester ILIKE %s"
            params.append(f"%{filters.requester}%")
        if filters.executed_by:
            query += " AND executed_by ILIKE %s"
            params.append(f"%{filters.executed_by}%")

        # Calculate total_count
        count_query = f"SELECT COUNT(*) FROM ({query}) AS subquery"
        cursor.execute(count_query, params)
        total_count = cursor.fetchone()[0]

        # Apply pagination
        paginated_query = f"""
            {query}
            ORDER BY id
            LIMIT %s OFFSET %s
        """
        params.extend([PAGE_SIZE, (filters.page - 1) * PAGE_SIZE])

        # Execute paginated query
        cursor.execute(paginated_query, params)
        rows = cursor.fetchall()
        total_pages = (total_count + PAGE_SIZE - 1) // PAGE_SIZE

        return {
            "total_count": total_count,
            "total_pages": total_pages,
            "data": rows # exclude the last row containing total_count
        }

    def get_by_id(self, id: int) -> list:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM support_cases WHERE id = %s", (id,)
        )
    
    def __del__(self):
        self.conn.close()
