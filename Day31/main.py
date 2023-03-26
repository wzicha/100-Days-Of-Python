from tkinter import *
import pandas
import random

french_words_file = pandas.read_csv('data/french_words.csv')
french_words = pandas.DataFrame(french_words_file)
# random_value = random.choice(range(len(french_words)))
# french_word_test = french_words.loc[random_value, 'French']
# english_word_test = french_words.loc[random_value, 'English']
cards_to_learn = french_words.to_dict(orient="records")
current_card = {}
learn_cards = {}
flip_card_timer = None

# Try to open words_to_learn
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If words_to_learn does not exist, create it
    original_data = french_words_file
    learn_cards = original_data.to_dict(orient="records")
else:
    learn_cards = data.to_dict(orient="records")


def generate_word():
    global current_card, french_word_test, english_word_test, flip_card_timer, random_value
    back_label.grid_forget()
    front_label = Label(image=card_front, borderwidth=0, highlightthickness=0, background=BACKGROUND_COLOR)
    front_label.grid(column=0, row=0, columnspan=2, rowspan=1)
    language.config(text="French", bg="#FFFFFF")
    current_card = random.choice(learn_cards)
    french_word_test = current_card['French']
    english_word_test = current_card['English']
    word_presented.config(text=f"{french_word_test}", bg="#FFFFFF")
    word_presented.lift()
    language.lift()
    window.update()
    # Cancel previous timer
    if flip_card_timer:
        window.after_cancel(flip_card_timer)
    flip_card_timer = window.after(3000, flip_card)
    window.update()


def flip_card():
    global back_label
    front_label.grid_forget()
    back_label = Label(image=card_back, borderwidth=0, highlightthickness=0, background='GREY')
    back_label.grid(column=0, row=0, columnspan=2, rowspan=1)
    language.config(text="English", bg="#B1DDC6", highlightthickness=0)
    word_presented.config(text=f"{english_word_test}", bg="#B1DDC6", highlightthickness=0)
    language.lift()
    word_presented.lift()
    window.update()


def known_card():
    global current_card, learn_cards
    if current_card in learn_cards:
        learn_cards.remove(current_card)
    if len(learn_cards) == 0:
        window.after_cancel(flip_card_timer)
        word_presented.config(text="Congratulations! You have completed all flashcards.", bg="#FFFFFF",
                              font=("Ariel", 18, "italic"))
        language.config(text="", bg="#FFFFFF")
        word_presented.lift()
        language.lift()
    else:
        data = pandas.DataFrame(learn_cards)
        data.to_csv("data/words_to_learn.csv", index=False)
        generate_word()
    print(len(learn_cards))


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

back_label = Label(image=card_back, borderwidth=0, highlightthickness=0, background='GREY')

language = Label(text="French", font=("Ariel", 40, "italic"), compound='center', anchor="center", highlightthickness=0,
                 background='white')
language.place(x=400, y=150, anchor="center")

word_presented = Label(text=f"", font=("Ariel", 60, "bold"), compound='center', anchor="center",
                       highlightthickness=0, background='white')
word_presented.place(x=400, y=263, anchor="center")

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1)

window.mainloop()
