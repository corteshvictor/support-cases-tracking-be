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
    number: str = Field(max_length=15)
    description: str
    status: Optional[StatusEnum] = Field(default=StatusEnum.open)
    priority: Optional[PriorityEnum] = Field(default=PriorityEnum.medium)
    database_name: str = Field(max_length=63)
    schema_name: str = Field(max_length=63)
    query_executed: str
    executed_by: str = Field(max_length=50)
    requester: str = Field(max_length=50)

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
    
class SupportCasesFilter(BaseModel):
    page: int = 1
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    description: Optional[str] = None
    database_name: Optional[str] = None
    requester: Optional[str] = None
    executed_by: Optional[str] = None
