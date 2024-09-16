from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class TrackingCreate(BaseModel):
    support_case_id: int = Field(gt=0)
    description: str
    affected_table: Optional[str] = Field(max_length=63)
    affected_column: Optional[str] = Field(max_length=63)
    affected_row_id: Optional[int]
    old_value: Optional[str]
    new_value: Optional[str]
    updated_by: str = Field(max_length=50)

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
