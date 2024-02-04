"""Ask a random question. Check if the answer is right. Keep score.
Finish the game after 10 questions."""

from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    new_question = Question(text=question["text"], answer=question["answer"])
    question_bank.append(new_question)

print(question_bank)