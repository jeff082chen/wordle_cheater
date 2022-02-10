import json
import random

with open('answers.json', 'r') as r:
    answers = json.load(r)

pa = answers['possible_answers']
ta = answers['total_answers']

not_duplicate = [ans for ans in pa if len(set(ans)) == 5]
duplicate = [ans for ans in pa if len(set(ans)) < 5]
assert len(not_duplicate) + len(duplicate) == len(pa), 'error'

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

if __name__ == '__main__':
    bingo = False

    while not bingo:
        guess = input()
        guess = (not_duplicate[0] if not_duplicate else duplicate[0]) if guess == '' else guess
        print(guess)
        result = [int(n) for n in input('hows the result? ').split(', ')]

        if result == [2, 2, 2, 2, 2]:
            bingo = True
            continue

        not_duplicate = [answer for answer in not_duplicate if check(guess, answer) == result]
        duplicate = [answer for answer in duplicate if check(guess, answer) == result]
        ta = [answer for answer in ta if check(guess, answer) == result]

        print(f'there\'s {len(ta)} possible answers remain')