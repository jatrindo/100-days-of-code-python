import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvases
card_img = tk.PhotoImage(file="images/card_front.png")
card_canvas_width = card_img.width()
card_canvas_height = card_img.height()

card_canvas = tk.Canvas(width=card_canvas_width, height=card_canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(card_canvas_width/2, card_canvas_height/2, image=card_img)
card_canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 25, "italic"))
card_canvas.create_text(400, 263, text="word", font=(FONT_NAME, 55, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
