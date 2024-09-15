from fastapi import HTTPException

from support_cases.domain.support_cases_entity import SupportCases, SupportCasesCreate
from support_cases.application.support_cases_usecase import SupportCasesUseCase
from .support_cases_mapper import map_to_support_cases

class SupportCasesController:
  def __init__(self, usecase: SupportCasesUseCase):
    self.usecase = usecase

  def get_support_case_by_id(self, id: int):
    result = self.usecase.get_support_case_by_id(id)
    if result:
      return map_to_support_cases(result)
    raise HTTPException(status_code=404, detail="Support case not found")
  
  def get_all_support_cases(self):
    result = self.usecase.get_all_support_cases()

    count = result["total_count"]
    pages = result["total_pages"]
    page = result["page"]
    data = result["data"]

    return {
        "info": {
            "count": count,
            "pages": pages,
            "next": f"/support_cases?page={page + 1}" if page < pages else None,
            "prev": f"/support_cases?page={page - 1}" if page > 1 else None
        },
        "results": [map_to_support_cases(row) for row in data]
    }
  
  def create_support_case(self, support_case: SupportCasesCreate):
    result = self.usecase.create_support_case(support_case)
    
    return map_to_support_cases(result)
