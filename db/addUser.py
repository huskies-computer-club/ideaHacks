import sqlite3

def add_user(pin, name):
    # Connect to SQLite database (change the database name if needed)
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example: Insert new user into the users table
    cursor.execute('''
        INSERT INTO users (pin, name) VALUES (?, ?)
    ''', (pin, name))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def input_valid_pin():
    while True:
        pin_input = input("Enter a 5-digit PIN: ")
        if pin_input.isdigit() and len(pin_input) == 5:
            return pin_input
        else:
            print("Invalid input. Please enter a 5-digit number.")

def input_valid_name():
    while True:
        name_input = input("Enter the user's name: ")
        if name_input.strip():  # Check if the input is not empty
            return name_input
        else:
            print("Invalid input. Please enter a non-empty name.")

if __name__ == "__main__":
    # User input for a valid 5-digit PIN
    input_pin = input_valid_pin()

    # User input for the user's name
    input_name = input_valid_name()

    # Call the function to add a new user to the database
    add_user(input_pin, input_name)

    print(f"User '{input_name}' with PIN '{input_pin}' added to the database.")
