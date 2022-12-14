# an attribute for the quiz
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # checking for more questions
    def more_questions(self):
        cur_ques = (self.question_number + 1)
        total_quest = len(self.question_list)

        #print statement at the end of the quiz
        if cur_ques == total_quest:
            print("You've completed the quiz")
            print(f"Your final score is {self.score}")
        return cur_ques < total_quest

    # moving to the next question
    def next_question(self):
        quest = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q {self.question_number}: {quest.text} (True / False): ")

        # checking answer and printing score
        self.check_answer(answer, quest.answer)
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")

    # checking for correct answer and adding score
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
            print(f"The answer is {correct_answer}")

