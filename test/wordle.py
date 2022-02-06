import json
import random

with open('answers.json', 'r') as r:
    answers = json.load(r)

pa = answers['possible_answers']
ta = answers['total_answers']

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
    answer = random.choice(pa)

    bingo = False

    while not bingo:
        guess = input('make a guess: ')
        if len(guess) != 5 or guess not in ta:
            print('invalid word!')
            continue
        
        result = check(guess, answer)

        if result == [2, 2, 2, 2, 2]:
            bingo = True
            break

        print(result)
        print('try again!')