from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Create attribute to store questions
question_bank = []
#Pass each question from the question bank into the Question constructor
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"The quiz is over. Your final score: {quiz.score}/{len(quiz.questions_list)}")

