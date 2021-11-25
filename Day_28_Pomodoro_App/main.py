import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        # Every 8 reps we take a long break
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # Every even (non-8) reps we take a short break
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # Every odd rep we work
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    time = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        window.after(10, count_down, count - 1)   # Call this function again after a second
    else:
        start_timer()

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
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
