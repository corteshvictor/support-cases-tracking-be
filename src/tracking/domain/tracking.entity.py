from pydantic import BaseModel

class Tracking(BaseModel):
    description: str
    updated_by: str
    affected_table: str
    affected_column: str
    affected_row_id: int
    old_value: str
    new_value: str
