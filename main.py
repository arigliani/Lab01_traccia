import random
import re
import riddle
import player

file_text = riddle.get_text('/Users/giovanniarigliani/Desktop/python_tools/esercitazioni/Lab01_traccia/domande.txt')

shullfed_raddles_list = riddle.shuffle_raddle(file_text)

flag = "true"
score = int(0)
ranking = []
while flag == "true":
    for single in shullfed_raddles_list:
        print(single.question)
        print(single.answers)
        right_answer_index = riddle.get_index_answere(single.right_answer, single.answers)
        print(f"-----indice------{right_answer_index}")
        user_input = int((input("inserisci il numero della risposta giusta")))
        if user_input == right_answer_index + 1:
            print("Risposta corretta!")
            score = score + 1
        else:
            print("hai perso!")
            print(f"Il punteggio totalizzato è: {score}")
            flag = "false"
            nickname = input("inserisci il tuo nickname: ")
            file_path = '/Users/giovanniarigliani/Desktop/python_tools/esercitazioni/Lab01_traccia/punti.txt'
            with open(file_path, 'a+') as c:
                c.write(f"{nickname} {score}\n")

            with open(file_path, 'r+') as c:
                players = c.read().split("\n")

            for p in players:
                    sub_p = p.split()
                    if (len(sub_p) == 2):
                        ranking.append(player.Player(sub_p[0],sub_p[1]))

            ranking_ordinato = sorted(ranking, key=lambda p: p.score, reverse=True)

            for p in (ranking_ordinato):
                print(f" {p.nickname} -- {p.score}")

            score = 0
            break
