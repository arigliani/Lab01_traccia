import re
import random
class Riddle_class:
    def __init__(self, question, level, right_answer, answers):
        self.question = question
        self.level = level
        self.right_answer = right_answer
        self.answers = answers

    def check_answer(self, answer):
        return answer == self.right_answer

    def get_string(self):
        return f"domanda {self.question} -- livello {self.level} -- corretta {self.right_answer} - lista: {self.answers}"


def get_text(file_path):
        with open(file_path, 'r') as c:
            file_text = c.read()
        riddle_list = []

        for rid in re.split('\n\n', file_text):
            riddle_elements = re.split('\n', rid)
            if len(riddle_elements) == 6:
                question = riddle_elements[0]
                level = riddle_elements[1]
                right_answer = riddle_elements[2]
                answers = [riddle_elements[2], riddle_elements[3], riddle_elements[4], riddle_elements[5]]
                new_riddle = Riddle_class(question, level, right_answer, answers)
                riddle_list.append(new_riddle)

            else:
                print("error: the text format is not correct")
        return riddle_list

def shuffle_raddle(txt):
    for i in txt:
        random.shuffle(i.answers)
    return txt

def get_index_answere(right_answer, answers):
        for i in range(len(answers)):
            if right_answer == answers[i]:
                return i