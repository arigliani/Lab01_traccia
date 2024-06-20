import random
import re
import riddle

file_text = riddle.get_text('/Users/giovanniarigliani/Desktop/python_tools/esercitazioni/Lab01_traccia/domande.txt')

shullfed_raddles_list = riddle.shuffle_raddle(file_text)

for single in shullfed_raddles_list:
    print(single.answers)