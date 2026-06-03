import psycopg2

def get_table_schema(db_config, table_name):
    """
    Connects to the database and fetches the true columns 
    and data types for a specific table.
    """
    # 1. Open the connection to the database
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    # 2. Ask the database's internal registry for the column names
    query = """
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = %s;
    """
    
    # 3. Execute the question and grab the results
    cursor.execute(query, (table_name,))
    columns = cursor.fetchall()
    
    # 4. Clean up and close our database connection
    cursor.close()
    conn.close()
    
    # 5. Convert the results into a clean dictionary format:
    # Example output: {'id': 'integer', 'username': 'character varying'}
    return {row[0]: row[1] for row in columns}
