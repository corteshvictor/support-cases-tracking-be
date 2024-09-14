def insert_sample_data():
    """Define los comandos SQL para insertar datos de ejemplo."""
    return [
        """
        INSERT INTO support_cases (
            number, description, status, database_name, schema_name, query_executed, executed_by, requester, priority
        ) VALUES
        ('SC-001', 'Create a Cargo Agent', 'Open', 'transactional_db', 'public', 'INSERT INTO cargo_agents ...', 'admin', 'user1', 'Medium'),
        ('SC-002', 'Change status of an Operation', 'Closed', 'transactional_db', 'operations', 'UPDATE operations SET status = ...', 'admin', 'user2', 'High'),
        ('SC-003', 'Delete obsolete records', 'In Progress', 'transactional_db', 'archive', 'DELETE FROM archive WHERE ...', 'admin', 'user3', 'Low')
        """,
        """
        INSERT INTO tracking (
            support_case_id, description, updated_by, affected_table, affected_column, old_value, new_value
        ) VALUES
        (1, 'Initial creation of cargo agent', 'admin', 'cargo_agents', 'status', NULL, 'Active'),
        (2, 'Status changed to Closed', 'admin', 'operations', 'status', 'Open', 'Closed'),
        (3, 'Obsolete records marked for deletion', 'admin', 'archive', 'status', 'Active', 'Deleted')
        """
    ]
