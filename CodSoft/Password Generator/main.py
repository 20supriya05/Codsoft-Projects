import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")
        return
    
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display the password
    result_label.config(text=password)
    copy_button.config(state=tk.NORMAL)

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")  # Set window size to 300x250 pixels

# Create and place the widgets
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=10, font=('Helvetica', 14))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Helvetica', 14), wraplength=300)
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

# Start the main loop
root.mainloop()
