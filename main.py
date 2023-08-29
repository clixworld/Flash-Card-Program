from tkinter import *
import pandas
from random import choice

# ----------------Constant Variables----------------------------
BACKGROUND_COLOR = "#B1DDC6"
timer = None
# -----------------Get CSV File---------------------------------
data = pandas.read_csv("data/french_words.csv")
data_list = data.to_dict(orient="records")


# -----------------Timer/Flip-----------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=back_front)
    canvas.itemconfig(french_text, text="English")
    canvas.itemconfig(current_word, text=word["English"])
    window.after_cancel(timer)


# -----------------Generate Word---------------------------------
remove = False


def generate_word():
    global remove
    global word
    word = choice(data_list)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(current_word, text=word["French"])
    canvas.itemconfig(french_text, text="French")
    global timer
    timer = window.after(3000, func=flip_card)
    if remove:
        data_list.remove(word)


# -----------------Button---------------------------------

def right_button():
    global remove
    remove = True
    generate_word()


def wrong_button():
    global remove
    remove = False
    generate_word()


# -----------------GUI------------------------------------------
window = Tk()
window.title("Flashcard Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
back_front = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
french_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
current_word = canvas.create_text(400, 263, text="FrenchWord", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=wrong_button)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=right_button)
right_button.grid(column=1, row=1)

window.mainloop()
