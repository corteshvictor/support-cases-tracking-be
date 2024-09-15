from fastapi import APIRouter, Depends

from support_cases.domain.support_cases_entity import SupportCasesCreate
from support_cases.application.support_cases_usecase import SupportCasesUseCase
from .persistence.support_cases_persistence import SupportCasesPersistenceRepository
from .support_cases_controller import SupportCasesController

support_cases_router = APIRouter()

def support_cases_controller():
    repository = SupportCasesPersistenceRepository()
    usecase = SupportCasesUseCase(repository)
    return SupportCasesController(usecase)

@support_cases_router.get("/")
def get_all_support_cases(controller: SupportCasesController = Depends(support_cases_controller)):
    return controller.get_all_support_cases()

@support_cases_router.get("/{id}")
def get_by_id_support_case(id: int, controller: SupportCasesController = Depends(support_cases_controller)):
    return controller.get_support_case_by_id(id)

@support_cases_router.post("/")
def create_support_case(support_case: SupportCasesCreate, controller: SupportCasesController = Depends(support_cases_controller)):
    return controller.create_support_case(support_case)
