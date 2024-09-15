from tracking.domain.tracking_entity import Tracking, TrackingCreate
from tracking.domain.tracking_repository import TrackingRepository
from typing import List

class TrackingUseCase:
    def __init__(self, repository: TrackingRepository):
        self.repository = repository

    def get_tracking_by_id(self, id: int) -> Tracking:
        return self.repository.get_by_id(id)

    def get_all_tracking(self) -> List[Tracking]:
        return self.repository.get_all()
    
    def create_tracking(self, tracking: TrackingCreate) -> Tracking:
        return self.repository.create(tracking)
