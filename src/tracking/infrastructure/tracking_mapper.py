from tracking.domain.tracking_entity import Tracking

def map_to_tracking(row):
    """
    Maps a database row to a Tracking entity.
    """
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
    
    return Tracking(**tracking_dict)
