from pydantic import BaseModel
from enum import Enum

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

class SupportCases(BaseModel):
    number: str
    description: str
    status: StatusEnum
    priority: PriorityEnum
    database_name: str
    schema_name: str
    query_executed: str
    executed_by: str
    requester: str
