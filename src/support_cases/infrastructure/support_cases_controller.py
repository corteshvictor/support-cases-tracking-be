from fastapi import HTTPException
from support_cases.domain.support_cases_entity import SupportCases, SupportCasesCreate
from support_cases.application.support_cases_usecase import SupportCasesUseCase

class SupportCasesController:
  def __init__(self, usecase: SupportCasesUseCase):
    self.usecase = usecase

  def get_support_case_by_id(self, id: int):
    result = self.usecase.get_support_case_by_id(id)
    if result:
      case_dict = {
        "id": result[0],
        "number": result[1],
        "description": result[2],
        "created_at": result[3],
        "updated_at": result[4],
        "status": result[5],
        "database_name": result[6],
        "schema_name": result[7],
        "query_executed": result[8],
        "executed_by": result[9],
        "requester": result[10],
        "priority": result[11]
      }

      return SupportCases(**case_dict)
    raise HTTPException(status_code=404, detail="Support case not found")
  
  def get_all_support_cases(self):
    result = self.usecase.get_all_support_cases()

    count = result["total_count"]
    pages = result["total_pages"]
    page = result["page"]
    data = result["data"]
    
    cases = []
    for row in data:
        case_dict = {
            "id": row[0],
            "number": row[1],
            "description": row[2],
            "created_at": row[3],
            "updated_at": row[4],
            "status": row[5],
            "database_name": row[6],
            "schema_name": row[7],
            "query_executed": row[8],
            "executed_by": row[9],
            "requester": row[10],
            "priority": row[11]
        }
        case = SupportCases(**case_dict)
        cases.append(case)

    return {
        "info": {
            "count": count,
            "pages": pages,
            "next": f"/support_cases?page={page + 1}" if page < pages else None,
            "prev": f"/support_cases?page={page - 1}" if page > 1 else None
        },
        "results": cases
    }
  
  def create_support_case(self, support_case: SupportCasesCreate):
    result = self.usecase.create_support_case(support_case)

    case_dict = {
      "id": result[0],
      "number": result[1],
      "description": result[2],
      "created_at": result[3],
      "updated_at": result[4],
      "status": result[5],
      "database_name": result[6],
      "schema_name": result[7],
      "query_executed": result[8],
      "executed_by": result[9],
      "requester": result[10],
      "priority": result[11]
    }
    
    return SupportCases(**case_dict)
