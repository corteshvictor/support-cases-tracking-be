from abc import ABC, abstractmethod
from support_cases.domain.support_cases_entity import SupportCases, SupportCasesCreate
from typing import List

class SupportCasesRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> SupportCases:
        pass

    @abstractmethod
    def get_all(self) -> List[SupportCases]:
        pass

    @abstractmethod
    def create(self, support_case: SupportCasesCreate) -> SupportCases:
        pass