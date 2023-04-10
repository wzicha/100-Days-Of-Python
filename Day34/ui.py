from tkinter import *
import os
import html
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
image_dir = os.path.join(os.path.dirname(__file__), "images")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # self.question_text = question_text
        # self.question = question
        self.window = Tk()
        self.window.geometry("360x550")
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.columnconfigure(index=1)
        self.window.rowconfigure(index=2)

        self.score = Label(text="Score: 0", font=("Arial", "14",), justify="center", bg=THEME_COLOR, fg="White")
        self.score.grid(column=1, row=0, sticky=E, padx=40, pady=20)

        self.question_text_label = Label(
            text=html.unescape(self.quiz.current_question.text) if self.quiz.current_question else "",
            font=("Arial", "14", "italic"), width=300, height=250,
                                         wraplength=260, bg='White')

        self.question_text_label.grid(column=0, row=1, columnspan=2, pady=50)

        self.correct_image = PhotoImage(file=os.path.join(image_dir, "true.png"))
        self.correct_button = Button(image=self.correct_image, command=self.get_next_question)
        self.correct_button.grid(column=0, row=2, padx=30, sticky="E")

        self.wrong_image = PhotoImage(file=os.path.join(image_dir, "false.png"))
        self.wrong_button = Button(image=self.wrong_image, command=self.get_next_question)
        self.wrong_button.grid(column=1, row=2, padx=30, sticky="W")

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        # self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_text_label.config(self.question_text, text=q_text)

