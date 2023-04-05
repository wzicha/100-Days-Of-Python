from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        canvas = Canvas(self.window, width=350, height=500, bg=THEME_COLOR)
        self.window.columnconfigure(index=2)
        self.window.rowconfigure(index=3)
        self.score = Label(text="Score: 0", padx=20, pady=20, font=("Arial", "12"), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.question = Label(text="qqq", font=("Arial", "20", "italic"), height=250, width=300, justify="center")
        self.question.grid(column=0, row=1)

        self.window.mainloop()
