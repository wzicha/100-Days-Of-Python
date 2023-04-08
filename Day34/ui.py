from tkinter import *
import os

THEME_COLOR = "#375362"
image_dir = os.path.join(os.path.dirname(__file__), "images")


class QuizInterface:

    def __init__(self, question_text, question):
        self.question_text = question_text
        self.question = question
        self.window = Tk()
        self.window.geometry("340x400")
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", font=("Arial", "20", "italic"), justify="center", bg=THEME_COLOR)
        self.score.grid(column=1, row=0, sticky=E)

        self.question_text_label = Label(text=self.question_text, font=("Arial", "20", "italic"), justify="center",
                                         bg=THEME_COLOR)
        self.question_text_label.grid(column=0, row=1, columnspan=2, padx=10, pady=20)

        self.correct_image = PhotoImage(file=os.path.join(image_dir, "true.png"))
        self.correct_button = Button(image=self.correct_image)
        self.correct_button.grid(column=0, row=2, padx=20, pady=20, sticky="E")

        self.wrong_image = PhotoImage(file=os.path.join(image_dir, "false.png"))
        self.wrong_button = Button(image=self.wrong_image)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20, sticky="W")

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        self.window.mainloop()
