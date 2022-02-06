import json
import random

with open('answers.json', 'r') as r:
    answers = json.load(r)


def check(guess, answer):
    result = [0, 0, 0, 0, 0]

    for i in range(len(result)):
        if guess[i] == answer[i]:
            result[i] = 2

    for i in range(len(result)):
        if result[i] == 2:
            continue

        for j in range(len(result)):
            if guess[i] == answer[j] and result[j] != 2:
                result[i] = 1
    
    return result

if __name__ == '__main__':
    bingo = False

    while not bingo:
        guess = random.choice(answers)
        result = [int(n) for n in input('hows the result? ').split(', ')]

        if result == [2, 2, 2, 2, 2]:
            bingo = True
            continue

        for i, n in enumerate(result):
            if n == 0:
                answers = [answer for answer in answers if guess[i] not in answer]

        answers = [answer for answer in answers if check(guess, answer) == result]