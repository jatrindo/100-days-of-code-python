import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
title_label.grid(row=0, column=1)

checkmark_label = tk.Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmark_label.grid(row=3, column=1)

# Tomato Image with Timer
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
