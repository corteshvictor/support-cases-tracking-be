from config.db_connection import DBConnection

class TrackingPersistenceRepository():
  def __init__(self):
    self.conn = DBConnection().get_connection()
  
  def get_all(self):
    return {"message": "Get all tracking Persistence Repository"}
  
  def get_by_id(self, id: int):
    return {"message": "Get by id tracking Persistence Repository", "id":id}
  
  def create(self, tracking):
    return {"message": "Create tracking Persistence Repository", "tracking":tracking}
