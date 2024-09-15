from pydantic import BaseModel
from datetime import datetime

class TrackingCreate(BaseModel):
    updated_by: str
    affected_table: str
    affected_column: str
    affected_row_id: int
    old_value: str
    new_value: str

class Tracking(TrackingCreate):
    id: int
    support_case_id: int
    description: str
    affected_table: str
    affected_column: str
    affected_row_id: int
    old_value: str
    new_value: str
    updated_by: str
    updated_at: datetime
