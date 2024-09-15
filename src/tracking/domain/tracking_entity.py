from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TrackingCreate(BaseModel):
    support_case_id: int
    description: str
    affected_table: Optional[str]
    affected_column: Optional[str]
    affected_row_id: Optional[int]
    old_value: Optional[str]
    new_value: Optional[str]
    updated_by: str

class Tracking(BaseModel):
    id: int
    support_case_id: int
    description: str
    affected_table: Optional[str]
    affected_column: Optional[str]
    affected_row_id: Optional[int]
    old_value: Optional[str]
    new_value: Optional[str]
    updated_by: str
    created_at: datetime
    updated_at: datetime
