import tkinter
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashcard Application')
canvas = Canvas(width=800, height=526)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, highlightthickness=0)
window.grid_columnconfigure(index=1)
window.grid_rowconfigure(index=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

front_label = Label(image=card_front, borderwidth=0, highlightthickness=0, background=BACKGROUND_COLOR)
front_label.grid(column=0, row=0, columnspan=2, rowspan=1)

window.mainloop()
