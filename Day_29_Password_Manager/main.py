import json
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
password_file = "data.json"


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if not website:
        messagebox.showerror(title="Oops", message="Please provide a website!")
        return

    if not email:
        messagebox.showerror(title="Oops", message="Please provide an email!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"Okay to save password for the following?:\n"
                                                          f"Website: {website}\n"
                                                          f"Email: {email}")

    if not is_ok:
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        # Read JSON from database
        with open(password_file, 'r') as f:
            password_data = json.load(f)
    except FileNotFoundError:
        password_data = {}

    # Update database with new entry
    password_data.update(new_data)
    with open(password_file, 'w') as f:
        json.dump(password_data, f, indent=4)

    # Reset the website, password fields
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()

    if not website:
        messagebox.showerror(title="Oops", message="Please provide a website!")
        return

    try:
        with open(password_file, 'r') as f:
            password_data = json.load(f)

        entry = password_data.get(website)
        if not entry:
            messagebox.showerror(title=f"No Details", message=f"No details for {website} exist")
            return

        email = entry.get('email')
        password = entry.get('password')

        # Display Password
        messagebox.showinfo(title=f"{website}", message=f"Website: {email}\n"
                                                        f"Password: {password}")
        # Copy to Clipboard
        pyperclip.copy(password)
    except FileNotFoundError:
        messagebox.showerror(title="No Data File Found", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
WHITE = "#FFFFFF"

# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

# Lock Image
canvas = tk.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lockImg = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lockImg)
canvas.grid(row=0, column=1)


# Labels
website_label = tk.Label(text="Website:", bg=WHITE)
website_label.grid(row=1, column=0)

email_username_label = tk.Label(text="Email/Username:", bg=WHITE)
email_username_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:", bg=WHITE)
password_label.grid(row=3, column=0)


# Entries
website_entry = tk.Entry(width=25)
website_entry.grid(row=1, column=1, columnspan=1)

email_username_entry = tk.Entry(width=45)
email_username_entry.insert(0, "example@mail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=25)
password_entry.grid(row=3, column=1)


# Buttons
search_button = tk.Button(text="Search", command=search_password, width=16)
search_button.grid(row=1, column=2)

gen_password_button = tk.Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
