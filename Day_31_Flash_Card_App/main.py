import tkinter as tk
import pandas
import random

# ----- Word Retrieval
database_path = "data/spanish_words.csv"
database_data = pandas.read_csv(database_path)
database_words = database_data.to_dict(orient='records')

foreign_language = database_data.columns[0]
native_language = database_data.columns[1]

flip_timer = None
flip_time_ms = 3000


def get_new_card():
    return random.sample(database_words, 1)[0]


def flip_card(language, word):
    card_canvas.itemconfig(card_canvas_img, image=back_card_img)
    card_canvas.itemconfig(language_name_text, text=language, fill=BACK_CARD_TEXT_COLOR)
    card_canvas.itemconfig(word_text, text=word, fill=BACK_CARD_TEXT_COLOR)


def display_new_card():
    global flip_timer

    # Cancel the previous flip timer if the user clicked a button fast
    if flip_timer:
        window.after_cancel(flip_timer)

    # Grab a card from the database
    entry = get_new_card()
    foreign_word = entry.get(foreign_language)
    native_word = entry.get(native_language)

    # Display Foreign word
    card_canvas.itemconfig(card_canvas_img, image=front_card_img)
    card_canvas.itemconfig(language_name_text, text=foreign_language, fill=FRONT_CARD_TEXT_COLOR)
    card_canvas.itemconfig(word_text, text=foreign_word, fill=FRONT_CARD_TEXT_COLOR)

    # After some time, flip and show the Native word
    flip_timer = window.after(flip_time_ms, flip_card, native_language, native_word)


def wrong_button_pressed():
    display_new_card()


def right_button_pressed():
    display_new_card()

# ----- UI Stuff -----
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
FRONT_CARD_TEXT_COLOR = "#000000"
BACK_CARD_TEXT_COLOR = "#FFFFFF"

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvases
front_card_img = tk.PhotoImage(file="images/card_front.png")
back_card_img = tk.PhotoImage(file="images/card_back.png")
card_canvas_width = front_card_img.width()
card_canvas_height = front_card_img.height()

card_canvas = tk.Canvas(width=card_canvas_width, height=card_canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas_img = card_canvas.create_image(card_canvas_width/2, card_canvas_height/2, image=front_card_img)
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
