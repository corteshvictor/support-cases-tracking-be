from support_cases.domain.support_cases_entity import SupportCases

def map_to_support_cases(row):
    """
    Maps a database row to a SupportCases entity.
    """
    case_dict = {
        "id": row[0],
        "number": row[1],
        "description": row[2],
        "status": row[3],
        "priority": row[4],
        "database_name": row[5],
        "schema_name": row[6],
        "query_executed": row[7],
        "executed_by": row[8],
        "requester": row[9],
        "created_at": row[10],
        "updated_at": row[11],
    }
    return SupportCases(**case_dict)
