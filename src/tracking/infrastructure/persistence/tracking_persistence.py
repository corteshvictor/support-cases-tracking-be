from config.db_connection import DBConnection

class TrackingPersistenceRepository():
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
    return {"message": "Get by id tracking Persistence Repository", "id":id}
  
  def create(self, tracking):
    return {"message": "Create tracking Persistence Repository", "tracking":tracking}
