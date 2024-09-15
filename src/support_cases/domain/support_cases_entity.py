from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class PriorityEnum(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"
    critical = "Critical"

class StatusEnum(str, Enum):
    open = "Open"
    in_progress = "In Progress"
    resolved = "Resolved"
    closed = "Closed"

class SupportCasesCreate(BaseModel):
    number: str
    description: str
    status: Optional[StatusEnum] = Field(default=StatusEnum.open)
    priority: Optional[PriorityEnum] = Field(default=PriorityEnum.medium)
    database_name: str
    schema_name: str
    query_executed: str
    executed_by: str
    requester: str

class SupportCases(BaseModel):
    id: int
    number: str
    description: str
    status: StatusEnum
    priority: PriorityEnum
    database_name: str
    schema_name: str
    query_executed: str
    executed_by: str
    requester: str
    created_at: datetime
    updated_at: datetime
