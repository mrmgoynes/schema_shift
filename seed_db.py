import psycopg2

# Connection details matching our docker-compose blueprint
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "sdet_admin",
    "password": "SecretPassword123",
    "database": "user_directory"
}

def seed_database():
    print("Connecting to the local Docker database...")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Create a fresh users table matching our OpenAPI spec columns
    print("Creating the 'users' table...")
    cursor.execute("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL
        );
    """)
    
    # Insert a dummy record for test data coverage
    print("Inserting sample profile data...")
    cursor.execute("""
        INSERT INTO users (username, email) 
        VALUES ('test_user', 'sdet_explorer@example.com');
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
