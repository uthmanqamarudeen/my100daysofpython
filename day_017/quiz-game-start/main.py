from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question_set in question_data:
    q_text = question_set["question"]
    q_answer = question_set["correct_answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

print(question_bank)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")