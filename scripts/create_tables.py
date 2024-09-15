def create_tables():
    return [
        """
        CREATE TYPE priority_level AS ENUM ('Low', 'Medium', 'High', 'Critical');
        """,
        """
        CREATE TYPE status_type AS ENUM ('Open', 'In Progress', 'Closed', 'Resolved');
        """,
        """
        CREATE TABLE IF NOT EXISTS support_cases (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            number TEXT NOT NULL CHECK (char_length(number) <= 15),
            description TEXT NOT NULL,
            status status_type NOT NULL DEFAULT 'Open',
            priority priority_level NOT NULL DEFAULT 'Medium'
            database_name TEXT NOT NULL CHECK (char_length(database_name) <= 63),
            schema_name TEXT NOT NULL CHECK (char_length(schema_name) <= 63),
            query_executed TEXT NOT NULL,
            executed_by TEXT NOT NULL CHECK (char_length(executed_by) <= 50),
            requester TEXT NOT NULL CHECK (char_length(requester) <= 50),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS tracking (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            support_case_id BIGINT REFERENCES support_cases(id),
            description TEXT NOT NULL,
            affected_table TEXT CHECK (char_length(affected_table) <= 63),
            affected_column TEXT CHECK (char_length(affected_column) <= 63),
            old_value TEXT,
            new_value TEXT,
            affected_row_id BIGINT
            updated_by TEXT NOT NULL CHECK (char_length(updated_by) <= 50),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        )
        """
    ]
