import random
import re
import riddle

file_text = riddle.get_text('/Users/giovanniarigliani/Desktop/python_tools/esercitazioni/Lab01_traccia/domande.txt')

shullfed_raddles_list = riddle.shuffle_raddle(file_text)

flag = "true"
i = "0"
while flag == "true":
    for single in shullfed_raddles_list:
        print(single.question)
        print(single.answers)
        right_answer_index = riddle.get_index_answere(single.right_answer,single.answers)
        print(f"-----indice------{right_answer_index}")
        print("user input = ")
        user_input = int((input()))
        if user_input == right_answer_index+1:
            print("Risposta corretta!")
        else:
            print("hai perso!")
            flag = "false"
            break




