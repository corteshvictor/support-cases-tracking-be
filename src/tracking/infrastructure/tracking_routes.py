from fastapi import APIRouter, Depends, Path

from tracking.domain.tracking_entity import TrackingCreate
from tracking.application.tracking_usecase import TrackingUseCase
from .persistence.tracking_persistence import TrackingPersistenceRepository
from .tracking_controller import TrackingController

tracking_router = APIRouter()

def tracking_controller():
    repository = TrackingPersistenceRepository()
    usecase = TrackingUseCase(repository)
    return TrackingController(usecase)

@tracking_router.get("/")
def get_all_tracking(controller: TrackingController = Depends(tracking_controller)):
    return controller.get_all_tracking()

@tracking_router.get("/{id}")
def get_by_id_tracking(id: int = Path(gt=0), controller: TrackingController = Depends(tracking_controller)):
    return controller.get_tracking_by_id(id)

@tracking_router.post("/")
def create_tracking(tracking: TrackingCreate, controller: TrackingController = Depends(tracking_controller)):
    return controller.create_tracking(tracking)
