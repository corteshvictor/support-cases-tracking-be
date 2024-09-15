from tracking.domain.tracking_entity import TrackingCreate
from tracking.application.tracking_usecase import TrackingUseCase


class TrackingController:
    def __init__(self, usecase: TrackingUseCase):
        self.usecase = usecase

    def get_tracking_by_id(self, id: int):
        return self.usecase.get_tracking_by_id(id)

    def get_all_tracking(self):
        return self.usecase.get_all_tracking()

    def create_tracking(self, tracking: TrackingCreate):
        return self.usecase.create_tracking(tracking)