from config.db_connection import DBConnection
from tracking.domain.tracking_entity import Tracking, TrackingCreate
from tracking.domain.tracking_repository import TrackingRepository

class TrackingPersistenceRepository(TrackingRepository):
  def __init__(self):
    self.conn = DBConnection().get_connection()
  
  def get_all(self, page: int = 1, page_size: int = 10) -> dict:
    cursor = self.conn.cursor()

    offset = (page - 1) * page_size
    cursor.execute("SELECT COUNT(*) FROM tracking")
    total_count = cursor.fetchone()[0]
    total_pages = (total_count + page_size - 1) // page_size

    cursor.execute(
        """
        SELECT * FROM tracking
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
  
  def get_by_id(self, id: int):
    cursor = self.conn.cursor()
    cursor.execute(
        "SELECT * FROM tracking WHERE id = %s", (id,)
    )

    return cursor.fetchone()
  
  def create(self, tracking: TrackingCreate) -> Tracking:
    with self.conn.cursor() as cursor:
      
      cursor.execute(
          """
          INSERT INTO tracking (support_case_id, description, affected_table, affected_column, affected_row_id, old_value, new_value, updated_by)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
          """,
          (
              tracking.support_case_id,
              tracking.description,
              tracking.affected_table,
              tracking.affected_column,
              tracking.affected_row_id,
              tracking.old_value,
              tracking.new_value,
              tracking.updated_by
          )
      )

      tracking_id = cursor.fetchone()[0]
      self.conn.commit()

      return self.get_by_id(tracking_id)
    
  
  def __del__(self):
    self.conn.close()
