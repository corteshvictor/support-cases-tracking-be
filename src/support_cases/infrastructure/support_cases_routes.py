from typing import Optional
from fastapi import APIRouter, Depends, Query

from support_cases.domain.support_cases_entity import PriorityEnum, StatusEnum, SupportCasesCreate, SupportCasesFilter
from support_cases.application.support_cases_usecase import SupportCasesUseCase
from .persistence.support_cases_persistence import SupportCasesPersistenceRepository
from .support_cases_controller import SupportCasesController

support_cases_router = APIRouter()

def support_cases_controller():
    repository = SupportCasesPersistenceRepository()
    usecase = SupportCasesUseCase(repository)
    return SupportCasesController(usecase)

@support_cases_router.get("/")
def get_all_support_cases(
    page: int = Query(1, ge=1),
    status: Optional[StatusEnum] = Query(None),
    priority: Optional[PriorityEnum] = Query(None),
    description: str = Query(None),
    database_name: str = Query(None),
    requester: str = Query(None),
    executed_by: str = Query(None),
    controller: SupportCasesController = Depends(support_cases_controller)):

    filters = SupportCasesFilter(
        page=page,
        status=status,
        priority=priority,
        description=description,
        database_name=database_name,
        requester=requester,
        executed_by=executed_by
    )
    
    return controller.get_all_support_cases(filters)

@support_cases_router.get("/{id}")
def get_by_id_support_case(id: int, controller: SupportCasesController = Depends(support_cases_controller)):
    return controller.get_support_case_by_id(id)

@support_cases_router.post("/")
def create_support_case(support_case: SupportCasesCreate, controller: SupportCasesController = Depends(support_cases_controller)):
    return controller.create_support_case(support_case)
