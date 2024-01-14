import tkinter as tk
from tkinter import messagebox, StringVar, Entry, Label, Button, Tk, Toplevel
import sqlite3
import subprocess


isProcessOn = False

def award_points(user_id, points):
    # Connect to SQLite database (change the database name if needed)
    conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Example: Update points for the user
    cursor.execute('''
        UPDATE users SET points = points + ? WHERE id = ?
    ''', (points, user_id))

    # Commit changes and close the connection:
    conn.commit()
    conn.close()

def on_button_click():
    user_input_pin = entry_pin.get()

    # Call the function to get user information from the database
    user_info = get_user_info_by_pin(user_input_pin)

    # Check if user_info is not None (i.e., data found in the database)
    if user_info:
        print("what is user_info? : ", user_info)
        print("currentStateValue is: ",currentUserId.get()) 
        currentUserId = user_info[2]
        _, user_name, _, user_points = user_info
        
        # Award 5 points for signing in
        # award_points(user_info[0], 5)  # user_info[0] is the user ID
        # Display welcome message and updated points information in the same window
        result_text = f"Welcome, {user_name}!\nCurrent Points: {user_points + 5}"
        messagebox.showinfo("Login Successful", result_text)

        # Reset text input after displaying information
        entry_pin.delete(0, tk.END)
        open_success_window()
    else:
        messagebox.showerror("Invalid PIN", "Invalid PIN. User not found in the database.")

def open_success_window():
    print("what is current user id? ", currentUserId)
    process = subprocess.run(["python", "/home/ant/ideaHacks/python_scripts/communicate.py", currentUserId])

    success_window = tk.Toplevel(window)

    success_window.title("Login Successful")
    
    label_success = tk.Label(success_window, text="You may now start using the application.")
    label_success.pack(pady=20)

    button_close = tk.Button(success_window, text="Finish", command=success_window.destroy)
    button_close.pack(pady=10)
    try:
        stdout, stderr = process.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
    


# Create the main window
# Bind the Enter key to the button click function
# window.bind('<Return>', lambda event=None: on_button_click())

# Set focus to the PIN entry field when the GUI starts
# entry_pin.focus_set()


# Start the GUI main loop

class TrashBrain:
    def __init__(self, root):
        self.root = root
        self.root.title("Trash Interface")
        self.root.config(bg="skyblue")
        
        self.input_value = StringVar()
        self.user = None;

        # Entry widget for input
        self.input_entry = Entry(root, textvariable=self.input_value)
        self.input_entry.pack()

        self.submitEntry = Button(root, text="Login",command=self.login_success)
        self.submitEntry.pack()

    def get_user_info_by_pin(self):
    # Connect to SQLite database (change the database name if needed)
        conn = sqlite3.connect('database.db')

    # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

    # Example: Select data from the users table based on the PIN
        cursor.execute('''
         SELECT id, name, pin, points FROM users WHERE pin = ?
        ''', (self.input_value.get(),))

    # Fetch the results
        result = cursor.fetchone()

    # Close the connection
        conn.close()

        return result


    def login_success(self):
        print("do I have state value?: ", self.input_value.get())
        user = self.get_user_info_by_pin()
        self.userId = user[2]
        print("do I have self. userId?", self.userId)
        new_window = Toplevel(self.root)
        new_window.title("Access Granted")
        new_window.config(bg="skyblue")

        # Display the message
        access_granted_label = tk.Label(new_window, text="You may now use this application.", bg="skyblue")
        access_granted_label.pack()
        process = subprocess.run(["python","/home/ant/ideaHacks/python_scripts/communicate.py", self.userId])

        # Add a 'Finish' button
        finish_button = Button(new_window, text="Finish", command=new_window.destroy)
        finish_button.pack()

    def finish_action(self):
        # Action to perform on clicking 'Finish' button
        print("Finish_action");
        process.terminate()
        pass

root = Tk()
app = TrashBrain(root)
root.mainloop()
