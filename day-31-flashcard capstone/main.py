from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = []


def next_card():
    """basically chose random card configure new word and language"""
    # new_word = to_learn[random.randint(2, 102)]["French"]
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(language_label, text="French", fill="black")
    flip_timer = window.after(3000, func=card_swap)


def card_swap():
    """Swap languages"""
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    """remove card from dictionary, make new csv with remaining words"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------UI-----------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_swap)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_flashcard_image = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_flashcard_image)
language_label = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word_label = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas.grid(column=0, row=0, columnspan=2)

no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)

yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=1)

next_card()




window.mainloop()
