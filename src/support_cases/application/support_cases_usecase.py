from support_cases.domain.support_cases_entity import SupportCases, SupportCasesCreate, SupportCasesFilter
from support_cases.domain.support_cases_repository import SupportCasesRepository
from typing import List

class SupportCasesUseCase:
    def __init__(self, repository: SupportCasesRepository):
        self.repository = repository

    def get_support_case_by_id(self, id: int) -> SupportCases:
        return self.repository.get_by_id(id)

    def get_all_support_cases(self, filters: SupportCasesFilter) -> List[SupportCases]:
        return self.repository.get_all(filters)
    
    def create_support_case(self, support_case: SupportCasesCreate) -> SupportCases:
        return self.repository.create(support_case)
