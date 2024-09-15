from tracking.domain.tracking_entity import Tracking, TrackingCreate
from tracking.application.tracking_usecase import TrackingUseCase


class TrackingController:
    def __init__(self, usecase: TrackingUseCase):
        self.usecase = usecase

    def get_tracking_by_id(self, id: int):
        return self.usecase.get_tracking_by_id(id)

    def get_all_tracking(self):
        result = self.usecase.get_all_tracking()

        count = result["total_count"]
        pages = result["total_pages"]
        page = result["page"]
        data = result["data"]

        trackings = []
        for row in data:
            tracking_dict = {
                "id": row[0],
                "support_case_id": row[1],
                "description": row[2],
                "affected_table": row[3],
                "affected_column": row[4],
                "affected_row_id": row[5],
                "old_value": row[6],
                "new_value": row[7],
                "updated_by": row[8],
                "created_at": row[9],
                "updated_at": row[10],

            }
            tracking = Tracking(**tracking_dict)
            trackings.append(tracking)
        
        return {
            "info": {
                "count": count,
                "pages": pages,
                "next": f"/tracking?page={page + 1}" if page < pages else None,
                "prev": f"/tracking?page={page - 1}" if page > 1 else None
            },
            "results": trackings
        }

    def create_tracking(self, tracking: TrackingCreate):
        return self.usecase.create_tracking(tracking)