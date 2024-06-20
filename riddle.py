import re
class Riddle:
    def __init__(self, question, level, right_answer, answers):
        self.question = question
        self.level = level
        self.right_answer = right_answer
        self.answers = answers

    def check_answer(self, answer):
        return answer == self.right_answer

