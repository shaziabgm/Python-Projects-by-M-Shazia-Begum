import tkinter as tk
import random

# Character pool for password
pool_characters = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*(_+|<>?;'/{["

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Length must be >3 and <17")
            return
        if length <= 3:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Length is too short!")
            return
        if length >= 17:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Length is too long!")
            return
        password = "".join(random.sample(pool_characters, length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Please enter a valid number.")

# Tkinter window setup
root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg="#E6E6FA") 
root.geometry('500x300')
# Widgets
tk.Label(root, text="Enter password length:", font =15).pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

result_entry = tk.Entry(root, fg="blue", font=8, width=20)
result_entry.pack(pady=15)

root.mainloop()