import re
import riddle


def get_text(file_path):
    with open(file_path, 'r') as c:
        pattern_question = c.read()
    return pattern_question


file_text = get_text('/Users/giovanniarigliani/Desktop/python_tools/prova flet/esempio_flat_rep/Lab01_traccia/domande.txt')

riddle_list = []

for rid in re.split('\n\n', file_text):
    riddle_elements = re.split('\n',rid)
    if len(riddle_elements) == 6:
        question = riddle_elements[0]
        level = riddle_elements[1]
        right_answer = riddle_elements[2]
        answers = [riddle_elements[2],riddle_elements[3],riddle_elements[4],riddle_elements[5]]
        new_riddle = riddle.Riddle(question, level, right_answer, answers)
        riddle_list.append(new_riddle)

    else:
        print("error: the text format is not correct")

