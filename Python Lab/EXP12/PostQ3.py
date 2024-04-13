import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Create the main window
root = tk.Tk()
root.title("Form")

# Create a frame
frame = ttk.Frame(root, padding="10")
frame.pack()

# Create 'First name' and 'Last name' labels and text entry boxes
first_name_label = ttk.Label(frame, text="First Name:", font=('Helvetica', 10))
first_name_label.grid(row=0, column=0, sticky=tk.W, pady=2)
first_name_entry = ttk.Entry(frame)
first_name_entry.grid(row=0, column=1, pady=2)

last_name_label = ttk.Label(frame, text="Last Name:", font=('Helvetica', 10))
last_name_label.grid(row=1, column=0, sticky=tk.W, pady=2)
last_name_entry = ttk.Entry(frame)
last_name_entry.grid(row=1, column=1, pady=2)

# Create 'Gender' radio buttons
gender_label = ttk.Label(frame, text="Gender:", font=('Helvetica', 10))
gender_label.grid(row=2, column=0, sticky=tk.W, pady=2)
gender = tk.StringVar()
male_radio = ttk.Radiobutton(frame, text="Male", variable=gender, value="Male")
male_radio.grid(row=2, column=1, sticky=tk.W, pady=2)
female_radio = ttk.Radiobutton(frame, text="Female", variable=gender, value="Female")
female_radio.grid(row=3, column=1, sticky=tk.W, pady=2)

# Create 'Subject' dropdown menu
subject_label = ttk.Label(frame, text="Subject:", font=('Helvetica', 10))
subject_label.grid(row=4, column=0, sticky=tk.W, pady=2)
subject = ttk.Combobox(frame, values=["Automata Theory", "EM-4", "COA","UNIX"])
subject.grid(row=4, column=1, pady=2)

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('form_data.db')
c = conn.cursor()

# Create a new table (if it doesn't exist)
c.execute('''
    CREATE TABLE IF NOT EXISTS form_data (
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        subject TEXT
    )
''')

# Function to submit the form
def submit_form():
    # Insert the form data into the database
    c.execute('''
        INSERT INTO form_data VALUES (?, ?, ?, ?)
    ''', (first_name_entry.get(), last_name_entry.get(), gender.get(), subject.get()))
    
    # Commit the changes and close the connection
    conn.commit()
    
    # Display the input
    display_input()

# Function to display the input
def display_input():
    messagebox.showinfo("Input", f"First Name: {first_name_entry.get()}\nLast Name: {last_name_entry.get()}\nGender: {gender.get()}\nSubject: {subject.get()}")

# Function to reset the form
def reset_form():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    gender.set('')
    subject.set('')

# Create 'Submit', 'Reset', and 'Exit' buttons
submit_button = ttk.Button(frame, text="Submit/Display", command=submit_form)
submit_button.grid(row=5, column=0, pady=1)

reset_button = ttk.Button(frame, text="Reset", command=reset_form)
reset_button.grid(row=5, column=1, pady=1)

exit_button = ttk.Button(frame, text="Exit", command=root.destroy)
exit_button.grid(row=5, column=2, pady=1)

# Run the main loop
root.mainloop()