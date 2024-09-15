from abc import ABC, abstractmethod
from tracking.domain.tracking_entity import Tracking, TrackingCreate
from typing import List

class TrackingRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Tracking:
        pass

    @abstractmethod
    def get_all(self) -> List[Tracking]:
        pass

    @abstractmethod
    def create(self, support_case: TrackingCreate) -> Tracking:
        pass
