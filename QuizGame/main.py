from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qdata in question_data:
    text = qdata.get('question')
    answer = qdata.get('correct_answer')
    question_bank.append(Question(text, answer))

qbrain = QuizBrain(question_bank)

while qbrain.still_has_questions():
    qbrain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {qbrain.score}/{qbrain.question_number}")
