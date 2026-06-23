import tkinter as tk
import random

# Character pool for password
pool_characters = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*(_+|<>?;'/{["

def generate_password():
    try:
        length = int(entry.get())
        if length <=0:
            result_label.config(text="Length must be >3 and <17")
            return
        if length <= 3:
            result_label.config(text="Length is too short for the Password!")
            return
        if length >= 17:
            result_label.config(text="Length is too long for the Password!")
            return
        password = "".join(random.sample(pool_characters, length))
        result_label.config(text=f"Generated Password:   {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Tkinter window setup
root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg="#E6E6FA") 
root.geometry('500x300')
# Widgets
tk.Label(root, text="Enter password length:", font =("red",15)).pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

result_label = tk.Label(root, text="", fg="blue",font = 8)
result_label.pack(pady=30)

root.mainloop()