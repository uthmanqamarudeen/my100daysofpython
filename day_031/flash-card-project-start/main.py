import pandas


BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random

current_card_word = {}

# ------------------------- CREATE FLASHCARDS -------------------------#
try:
    data_source = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data_source = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

def generate_card():
    global current_card_word, flip_timer, data_source
    window.after_cancel(flip_timer)
    current_card_word = random.choice(data_source)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card_word["French"], fill="black")
    flip_timer = window.after(3000, flip_flashcard)

def update_data():
    global current_card_word, data_source
    data_source.remove(current_card_word)
    words_to_learn_frame = pandas.DataFrame(data_source)
    words_to_learn_frame.to_csv("data/words_to_learn.csv")

def on_check_button():
    generate_card()
    update_data()

# ------------------------- FLIP FLASHCARDS -------------------------#
def flip_flashcard():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card_word["English"], fill="white")


# ------------------------- UI SETUP -------------------------#
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_flashcard)

canvas = Canvas(width=800, height=526, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)

mark_img = PhotoImage(file="images/right.png")
mark_button = Button(image=mark_img, highlightthickness=0, command=on_check_button)
mark_button.grid(column=0, row=1)

cancel_img = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_img, highlightthickness=0, command=generate_card)
cancel_button.grid(column=1, row=1)


generate_card()

window.mainloop()
