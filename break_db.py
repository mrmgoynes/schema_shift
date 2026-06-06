import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "user": "sdet_admin",
    "password": "SecretPassword123",
    "database": "user_directory"
}

def drop_required_column():
    print("⚠️ Simulating an unannounced backend database migration...")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # Intentionally drop the 'email' column which our API contract promises to provide
    cursor.execute("ALTER TABLE users DROP COLUMN email;")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("❌ MUTATION COMPLETE: The 'email' column has been dropped from the Docker database!")

if __name__ == "__main__":
    drop_required_column()
