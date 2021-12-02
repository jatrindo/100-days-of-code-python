import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

# Website Row
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username Row
email_username_label = tk.Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = tk.Entry(width=45)
email_username_entry.grid(row=2, column=1, columnspan=2)

# Password Row
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=25)
password_entry.grid(row=3, column=1)

gen_password_button = tk.Button(text="Generate Password")
gen_password_button.grid(row=3, column=2)

# Add Row
add_button = tk.Button(text="Add", width=43)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
