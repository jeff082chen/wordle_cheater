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

def game(pa, ta):
    answer = random.choice(pa)

    bingo = False
    n = 0

    while not bingo:
        guess = random.choice(pa)
        
        if len(guess) != 5 or guess not in ta:
            print('invalid word!')
            continue
        
        result = check(guess, answer)

        if result == [2, 2, 2, 2, 2]:
            bingo = True
            break

        pa = [answer for answer in pa if check(guess, answer) == result]
        ta = [answer for answer in ta if check(guess, answer) == result]

        n += 1
    
    return n

if __name__ == '__main__':
    total = 0
    for _ in range(1000):
        total += game(pa, ta) + 1
    print(total / 1000)