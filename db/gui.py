import tkinter as tk
from tkinter import messagebox
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

def on_button_click():
    user_input_pin = entry_pin.get()

    # Call the function to get user information from the database
    user_info = get_user_info_by_pin(user_input_pin)

    # Check if user_info is not None (i.e., data found in the database)
    if user_info:
        _, user_name, _, user_points = user_info

        # Award 5 points for signing in
        award_points(user_info[0], 5)  # user_info[0] is the user ID

        # Display welcome message and updated points information in the same window
        result_text = f"Welcome, {user_name}!\nCurrent Points: {user_points + 5}"
        messagebox.showinfo("Login Successful", result_text)

        # Reset text input after displaying information
        entry_pin.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid PIN", "Invalid PIN. User not found in the database.")

# Create the main window
window = tk.Tk()
window.title("User Login")

# Create and place widgets
label_instruction = tk.Label(window, text="Enter a 5-digit PIN:")
label_instruction.pack(pady=10)

entry_pin = tk.Entry(window)
entry_pin.pack(pady=10)

button_submit = tk.Button(window, text="Login", command=on_button_click)
button_submit.pack(pady=10)

# Bind the Enter key to the button click function
window.bind('<Return>', lambda event=None: on_button_click())

# Set focus to the PIN entry field when the GUI starts
entry_pin.focus_set()

# Start the GUI main loop
window.mainloop()
