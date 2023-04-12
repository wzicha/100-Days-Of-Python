from tkinter import *
import os
import html
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
image_dir = os.path.join(os.path.dirname(__file__), "images")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.window.geometry("360x550")
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.columnconfigure(index=1)
        self.window.rowconfigure(index=2)

        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", "14",), justify="center", bg=THEME_COLOR, fg="White")
        self.score_label.grid(column=1, row=0, sticky=E, padx=40, pady=20)

        self.question_text_label = Label(
            text=html.unescape(self.quiz.current_question.text) if self.quiz.current_question else "",
            font=("Arial", "14", "italic"), width=300, height=250,
                                         wraplength=260, bg='White')

        self.question_text_label.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_image = PhotoImage(file=os.path.join(image_dir, "true.png"))
        self.true_button = Button(image=self.true_image, command=lambda: self.check_answer("True"))
        self.true_button.grid(column=0, row=2, padx=30, sticky="E")

        self.false_image = PhotoImage(file=os.path.join(image_dir, "false.png"))
        self.false_button = Button(image=self.false_image, command=lambda: self.check_answer("False"))
        self.false_button.grid(column=1, row=2, padx=30, sticky="W")

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_text_label.config(text=q_text)

    def check_answer(self, user_answer):
        correct_answer = self.quiz.current_question.answer
        if user_answer.lower() == correct_answer.lower():
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                print("You got it right!")
        else:
            print("That's wrong.")
            self.get_next_question()
        if self.quiz.next_question() is None:
                print("You've completed the quiz")
                print(f"Your final score was: {self.score}/{self.quiz.question_number}")



