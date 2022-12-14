from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    q_1 = Question(q["text"], q["answer"])
    question_bank.append(q_1)
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.more_questions():
    quiz.next_question()