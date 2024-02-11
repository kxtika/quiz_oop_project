"""Ask a random question. Check if the answer is right. Keep score.
Finish the game after 10 questions."""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(text=question["question"], answer=question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while not quiz.no_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")