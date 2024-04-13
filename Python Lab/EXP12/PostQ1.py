"""Create a GUI with frame and widgets: First name and Last name (Text), Gender (Radiobutton), Subject (dropdown menu) """
import tkinter as tk
from tkinter import ttk

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

# Run the main loop
root.mainloop()