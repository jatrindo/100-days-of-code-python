import tkinter as tk
import pandas
import random

# ----- Word Retrieval
database_path = "data/spanish_words.csv"
database_data = pandas.read_csv(database_path)
database_words = database_data.to_dict(orient='records')

foreign_language = database_data.columns[0]
native_language = database_data.columns[1]


def get_new_card():
    return random.sample(database_words, 1)[0]


def display_new_card():
    entry = get_new_card()
    foreign_word = entry.get(foreign_language)
    native_word = entry.get(native_language)

    card_canvas.itemconfig(language_name_text, text=foreign_language)
    card_canvas.itemconfig(word_text, text=foreign_word)


def wrong_button_pressed():
    display_new_card()


def right_button_pressed():
    display_new_card()

# ----- UI Stuff -----
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
language_name_text = card_canvas.create_text(400, 150, text="", font=(FONT_NAME, 25, "italic"))
word_text = card_canvas.create_text(400, 263, text="", font=(FONT_NAME, 55, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)


# Buttons
wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=wrong_button_pressed)
wrong_button.grid(row=1, column=0)

right_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, command=right_button_pressed)
right_button.grid(row=1, column=1)

# Start off with an initial word
display_new_card()

window.mainloop()
