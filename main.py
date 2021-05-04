from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in range(len(question_data)):
    question = Question(question_data[entry]["text"], question_data[entry]["answer"])
    question_bank.append(question)

Quiz = QuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print("\n\n\You have completed the quiz")
print(f"Your final score is: {Quiz.score}/{Quiz.question_number} ")