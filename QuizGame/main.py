from question_model import Question
from data import question_data

question_bank = []
for qdata in question_data:
    text = qdata.get('text')
    answer = qdata.get('answer')
    question_bank.append(Question(text, answer))
