from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz_ui = QuizInterface(question_text, question)
quiz_ui = QuizInterface()

while quiz_ui.still_has_questions():
    quiz_ui.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_ui.score}/{quiz_ui.question_number}")
