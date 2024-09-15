from fastapi import HTTPException

from tracking.domain.tracking_entity import TrackingCreate
from tracking.application.tracking_usecase import TrackingUseCase
from .tracking_mapper import map_to_tracking

class TrackingController:
    def __init__(self, usecase: TrackingUseCase):
        self.usecase = usecase

    def get_tracking_by_id(self, id: int):
        result = self.usecase.get_tracking_by_id(id)
        if result:
            return map_to_tracking(result)
        raise HTTPException(status_code=404, detail="Tracking not found")

    def get_all_tracking(self):
        result = self.usecase.get_all_tracking()

        count = result["total_count"]
        pages = result["total_pages"]
        page = result["page"]
        data = result["data"]
        
        return {
            "info": {
                "count": count,
                "pages": pages,
                "next": f"/tracking?page={page + 1}" if page < pages else None,
                "prev": f"/tracking?page={page - 1}" if page > 1 else None
            },
            "results": [map_to_tracking(row) for row in data]
        }

    def create_tracking(self, tracking: TrackingCreate):
        result = self.usecase.create_tracking(tracking)
        
        return map_to_tracking(result)
