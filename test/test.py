import json
import random

with open('answers.json', 'r') as r:
    answers = json.load(r)

pa = answers['possible_answers']
ta = answers['total_answers']

def check(guess, answer):
    result = [0, 0, 0, 0, 0]
    temp = [0, 0, 0, 0, 0]

    for i in range(len(result)):
        if guess[i] == answer[i]:
            result[i] = 2

    for i in range(len(result)):
        if result[i] == 2:
            continue

        for j in range(len(result)):
            if guess[i] == answer[j] and result[j] != 2 and temp[j] != 1:
                result[i] = 1
                temp[j] = 1
    
    return result

def get_random(answers):
    n = 0
    while n < 10:
        guess = random.choice(answers)
        if len(guess) == len(set(guess)):
            return guess
        n += 1

if __name__ == '__main__':
    bingo = False

    while not bingo:
        guess = input()
        guess = get_random(pa) if guess == '' else guess
        print(guess)
        result = [int(n) for n in input('hows the result? ').split(', ')]

        if result == [2, 2, 2, 2, 2]:
            bingo = True
            continue

        pa = [answer for answer in pa if check(guess, answer) == result]
        ta = [answer for answer in ta if check(guess, answer) == result]

        print(f'there\'s {len(ta)} possible answers remain')