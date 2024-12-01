import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength():
  global password, result
  password = password_entry.get()
  if len(password) < 6:
    result.set("Weak: Too short")
  elif not any(char.isdigit() for char in password):
    result.set("Weak: No numbers")
  elif not any(char.isupper() for char in password):
    result.set("Weak: No uppercase letters")
  elif not any(char.islower() for char in password):
    result.set("Weak: No lowercase letters")
  elif not any(char in "!@#$%^&*()" for char in password):
    result.set("Weak: No special characters")
  else:
    result.set("Strong")
    
# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")

# Create password label and entry
password_label = tk.Label(window, text="Enter password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create check button
check_button = tk.Button(window, text="Check Strength", command=check_password_strength)
check_button.pack()

# Create result label
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()
window.mainloop()



