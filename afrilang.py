import json
import random

with open("data/twi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def translate(a):
    if a in data:
        print(data[a])
    else:
        print("Word not in dictionary.")


def list_words():
    for a in data:
        print(a, ":", data[a])

def quiz():
    q_word = random.choice(list(data.keys()))
    ans = input(f"What is the meaning of {q_word}").lower()
    if ans == data[q_word]:
        print("Correct✅\n")
    else:
        print("Sorry thats not correct😭")
        print(f"The correct answer was: {data[q_word]}")

def contribute():
    new_word = input("Enter the English Word you want to contribute: ")
    if new_word in data:
        print("Word already exists in the dictionary.")
        return
    trans_nw = input(f"Enter the translation of the {new_word} in Akan")
    data[new_word] = trans_nw
    print(f"'{new_word}' has been added. Thank you for contributing!")
    with open("data/twi.json", "w", encoding="utf-8") as f:
        json.dump(data, f)


running = True
while running == True:
    try:
        cont = int(input("Do you want to translate(1) or print all(2) or test yourself(3) contribute(4) quit(5): "))
    except:
        print("Invalid Input\n")
        continue
    
    if cont == 1:
        word = input("Enter a word: \n").lower()
        translate(word)
    elif cont == 2:
        list_words()
    elif cont == 3:
        quiz()
    elif cont == 4:
        contribute()
    elif cont == 5:
        running = False
    else:
        print("Invalid input\n")