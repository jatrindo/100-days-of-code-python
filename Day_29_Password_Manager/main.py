import tkinter as tk
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
password_file = "data.txt"


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

    if is_ok:
        with open(password_file, 'a') as f:
            f.write(f"{website} | {email} | {password}\n")

        # Reset the website, password fields
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

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
website_entry = tk.Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)

email_username_entry = tk.Entry(width=45)
email_username_entry.insert(0, "example@mail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=25)
password_entry.grid(row=3, column=1)


# Buttons
gen_password_button = tk.Button(text="Generate Password")
gen_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
