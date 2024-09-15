from config.db_connection import DBConnection
from support_cases.domain.support_cases_repository import SupportCasesRepository
from support_cases.domain.support_cases_entity import SupportCases, SupportCasesCreate

class SupportCasesPersistenceRepository(SupportCasesRepository):
    def __init__(self):
        self.conn = DBConnection().get_connection()
    
    def create(self, support_case: SupportCasesCreate) -> SupportCases:
        print('support_casa.number', support_case.number)
        print('support_casa.status', support_case.status.value)
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

    def get_all(self, page: int = 1, page_size: int = 10) -> dict:
        cursor = self.conn.cursor()

        offset = (page - 1) * page_size
        cursor.execute("SELECT COUNT(*) FROM support_cases")
        total_count = cursor.fetchone()[0]
        total_pages = (total_count + page_size - 1) // page_size

        cursor.execute(
            """
            SELECT * FROM support_cases
            ORDER BY id
            LIMIT %s OFFSET %s
            """, 
            (page_size, offset)
        )

        return {
            "total_count": total_count,
            "total_pages": total_pages,
            "page": page,
            "data": cursor.fetchall()
        }
    
    def get_by_id(self, support_case_id: int) -> list:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM support_cases WHERE id = %s", (support_case_id,)
        )
        print('support_case_id', support_case_id)
        
        return cursor.fetchone()
    
    def __del__(self):
        self.conn.close()
