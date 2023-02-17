class QuizBrain:

    #Initialize question number to 0, print the question list
    def __init__(self,  question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0


    #Ask user for input. Print question number: text (True/False): answer
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        questions_list = self.questions_list
        if self.question_number < len(questions_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
