import sqlite3

def get_user_info_by_pin(pin):
    # Connect to SQLite database (change the database name if needed)
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example: Select data from the users table based on the PIN
    cursor.execute('''
        SELECT id, name, pin, points FROM users WHERE pin = ?
    ''', (pin,))

    # Fetch the results
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    return result

def award_points(user_id, points):
    # Connect to SQLite database (change the database name if needed)
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example: Update points for the user
    cursor.execute('''
        UPDATE users SET points = points + ? WHERE id = ?
    ''', (points, user_id))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # User input for a valid 5-digit PIN
    input_pin = input("Enter a 5-digit PIN: ")

    # Call the function to get user information from the database
    user_info = get_user_info_by_pin(input_pin)

    # Check if user_info is not None (i.e., data found in the database)
    if user_info:
        _, user_name, _, user_points = user_info
        print(f"Welcome, {user_name}!")

        # Award 5 points for signing in
        award_points(user_info[0], 5)  # user_info[0] is the user ID
        
        # Display updated user information
        updated_user_info = get_user_info_by_pin(input_pin)
        _, updated_user_name, _, updated_user_points = updated_user_info
        print(f"Current Points: {updated_user_points}")
    else:
        print("User not found in the database.")
