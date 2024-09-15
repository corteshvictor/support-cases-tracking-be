def insert_sample_data():
    return [
        """
        INSERT INTO support_cases (
            number, description, status, priority, database_name, schema_name, query_executed, executed_by, requester
        ) VALUES
            ('SC001', 'Initial setup of the database schema.', 'Open', 'Medium', 'main_db', 'public', 'CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT);', 'admin', 'user1'),
            ('SC002', 'Update user table to add email column.', 'In Progress', 'High', 'main_db', 'public', 'ALTER TABLE users ADD COLUMN email TEXT;', 'admin', 'user2'),
            ('SC003', 'Optimize the performance of the orders table.', 'Closed', 'Critical', 'orders_db', 'sales', 'CREATE INDEX idx_orders_date ON orders (order_date);', 'admin', 'user3'),
            ('SC004', 'Fix foreign key constraint in the products table.', 'Resolved', 'High', 'inventory_db', 'inventory', 'ALTER TABLE products ADD CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES categories(id);', 'admin', 'user4'),
            ('SC005', 'Add new column to the employees table.', 'Open', 'Medium', 'hr_db', 'hr', 'ALTER TABLE employees ADD COLUMN date_of_birth DATE;', 'admin', 'user5'),
            ('SC006', 'Remove deprecated column from the sales table.', 'In Progress', 'Low', 'sales_db', 'public', 'ALTER TABLE sales DROP COLUMN old_field;', 'admin', 'user6'),
            ('SC007', 'Add new index to the logs table.', 'Open', 'Medium', 'logs_db', 'public', 'CREATE INDEX idx_logs_timestamp ON logs (timestamp);', 'admin', 'user7'),
            ('SC008', 'Update stored procedure for customer data.', 'Closed', 'Critical', 'crm_db', 'public', 'CREATE OR REPLACE PROCEDURE update_customer_data() LANGUAGE plpgsql AS $$ BEGIN ... END; $$;', 'admin', 'user8'),
            ('SC009', 'Change default value for the status column in orders.', 'Resolved', 'High', 'orders_db', 'public', 'ALTER TABLE orders ALTER COLUMN status SET DEFAULT ''Pending'';', 'admin', 'user9'),
            ('SC010', 'Create new view for sales report.', 'Open', 'Medium', 'sales_db', 'reports', 'CREATE VIEW sales_report AS SELECT * FROM sales WHERE status = ''Completed'';', 'admin', 'user10'),
            ('SC011', 'Archive old data from the transactions table.', 'In Progress', 'Medium', 'transactions_db', 'archived', 'CREATE TABLE transactions_archive AS SELECT * FROM transactions WHERE transaction_date < CURRENT_DATE - INTERVAL ''1 year'';', 'admin', 'user11'),
            ('SC012', 'Modify the trigger for auditing changes.', 'Closed', 'High', 'audit_db', 'public', 'CREATE OR REPLACE FUNCTION audit_trigger() RETURNS TRIGGER AS $$ BEGIN ... END; $$ LANGUAGE plpgsql;', 'admin', 'user12'),
            ('SC013', 'Add foreign key constraint to the orders table.', 'Open', 'Medium', 'orders_db', 'sales', 'ALTER TABLE orders ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(id);', 'admin', 'user13'),
            ('SC014', 'Update schema for the payments table.', 'Resolved', 'High', 'payments_db', 'public', 'ALTER TABLE payments ADD COLUMN payment_method TEXT;', 'admin', 'user14'),
            ('SC015', 'Remove obsolete data from the inventory table.', 'Closed', 'Low', 'inventory_db', 'public', 'DELETE FROM inventory WHERE last_update < CURRENT_DATE - INTERVAL ''6 months'';', 'admin', 'user15');
        """,
        """
        INSERT INTO tracking (
            support_case_id, description, affected_table, affected_column, old_value, new_value, affected_row_id, updated_by
        ) VALUES
            (1, 'Initial schema setup', 'users', NULL, NULL, NULL, NULL, 'admin'),
            (2, 'Added email column', 'users', 'email', NULL, NULL, NULL, 'admin'),
            (3, 'Indexed order_date', 'orders', 'order_date', NULL, NULL, NULL, 'admin'),
            (4, 'Foreign key constraint added', 'products', 'category_id', NULL, NULL, NULL, 'admin'),
            (5, 'Date of birth column added', 'employees', 'date_of_birth', NULL, NULL, NULL, 'admin'),
            (6, 'Removed old_field', 'sales', 'old_field', 'old_value', NULL, NULL, 'admin'),
            (7, 'Index added to logs table', 'logs', 'timestamp', NULL, NULL, NULL, 'admin'),
            (8, 'Updated customer data procedure', 'customer_data', NULL, NULL, NULL, NULL, 'admin'),
            (9, 'Default value for status changed', 'orders', 'status', 'Shipped', 'Pending', NULL, 'admin'),
            (10, 'Created sales report view', 'sales', NULL, NULL, NULL, NULL, 'admin'),
            (11, 'Archived old transactions', 'transactions', NULL, NULL, NULL, NULL, 'admin'),
            (12, 'Modified audit trigger function', 'audit', NULL, NULL, NULL, NULL, 'admin'),
            (13, 'Added foreign key to orders table', 'orders', 'customer_id', NULL, NULL, NULL, 'admin'),
            (14, 'Added payment_method column', 'payments', 'payment_method', NULL, NULL, NULL, 'admin'),
            (15, 'Removed obsolete inventory data', 'inventory', NULL, 'old_value', NULL, NULL, 'admin');
        """
    ]
