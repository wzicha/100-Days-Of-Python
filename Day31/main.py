import tkinter
from tkinter import *
import pandas
import random

french_words_file = pandas.read_csv('data/french_words.csv')
french_words = pandas.DataFrame(french_words_file)
french_word_test = french_words.loc[random.randint(1, 102), 'French']


def generate_word():
    global french_word_test
    french_words_file = pandas.read_csv('data/french_words.csv')
    french_words = pandas.DataFrame(french_words_file)
    new_word = french_words.loc[random.randint(1, 102), 'French']
    french_word_test = new_word
    word_presented.config(text=f"{french_word_test}")
    window.update()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashcard Application')
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, highlightthickness=0)
window.grid_columnconfigure(index=1)
window.grid_rowconfigure(index=1)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

front_label = Label(image=card_front, borderwidth=0, highlightthickness=0, background=BACKGROUND_COLOR)
front_label.grid(column=0, row=0, columnspan=2, rowspan=1)
front_label.lift()

language = Label(text="French", font=("Ariel", 40, "italic"), compound='center', anchor="center", highlightthickness=0,
                 background='white')
language.place(x=400, y=150, anchor="center")

word_presented = Label(text=f"{french_word_test}", font=("Ariel", 60, "bold"), compound='center', anchor="center",
                       highlightthickness=0, background='white')
word_presented.place(x=400, y=263, anchor="center")

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=generate_word)
right_button.grid(column=1, row=1)

window.mainloop()
