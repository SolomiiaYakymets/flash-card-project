from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_button_img = PhotoImage(file="./images/right.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=529, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Buttons
right_button = Button(image=right_button_img, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_button_img, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

window.mainloop()