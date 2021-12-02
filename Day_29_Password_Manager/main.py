import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
WHITE = "#FFFFFF"

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = tk.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lockImg = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lockImg)
canvas.grid(row=0, column=0)

window.mainloop()
