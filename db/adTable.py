import sqlite3

def create_users_table():
    # Connect to SQLite database (change the database name if needed)
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example: Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            pin TEXT NOT NULL,
            name TEXT NOT NULL,
            points INTEGER DEFAULT 0
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Call the function to create the users table
    create_users_table()

    print("Users table created successfully.")
