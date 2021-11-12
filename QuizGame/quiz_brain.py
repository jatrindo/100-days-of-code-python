class QuizBrain(object):

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
