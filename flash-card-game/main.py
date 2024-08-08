import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# -------------------------- CARD GENERATOR --------------------------- #


def generate_next_card():
    global current_card, flip_timer
    window.after_cancel(str(flip_timer))
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_button_img = PhotoImage(file="./images/right.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=529, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
right_button = Button(image=right_button_img, command=generate_next_card, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_button_img, command=generate_next_card, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

generate_next_card()

window.mainloop()
