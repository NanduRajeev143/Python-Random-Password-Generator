import random
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar, messagebox

def generate_password():
    try:
        nr_letters = int(entry_letters.get())
        nr_symbols = int(entry_symbols.get())
        nr_numbers = int(entry_numbers.get())

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []

        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))

        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)
        password = ''.join(password_list)
        password_var.set(f"Your password is: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for letters, symbols, and numbers.")

def copy_to_clipboard():
    password = password_var.get().split(": ")[1]
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")


window = tk.Tk()
window.title("PyPassword Generator")
window.geometry("400x350")  # Set window size
window.configure(bg="#e6e6e6")  # Set background color


label_letters = Label(window, text="How many letters?", bg="#e6e6e6")
label_letters.pack(pady=10)

entry_letters = Entry(window)
entry_letters.pack(pady=5)

label_symbols = Label(window, text="How many symbols?", bg="#e6e6e6")
label_symbols.pack(pady=10)


entry_symbols = Entry(window)
entry_symbols.pack(pady=5)

label_numbers = Label(window, text="How many numbers?", bg="#e6e6e6")
label_numbers.pack(pady=10)

entry_numbers = Entry(window)
entry_numbers.pack(pady=5)


generate_button = Button(window, text="Generate Password", command=generate_password, bg="#4caf50", fg="white")
generate_button.pack(pady=15)

password_var = StringVar()
password_label = Label(window, textvariable=password_var, font=("Helvetica", 12), bg="#e6e6e6")
password_label.pack()


copy_button = Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white")
copy_button.pack(pady=10)

window.mainloop()
