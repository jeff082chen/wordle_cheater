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

def game(pa, ta, not_duplicate, duplicate):
    answer = random.choice(pa)
    print(f'ans: {answer}\n')

    bingo = False
    n = 0

    while not bingo:
        guess = not_duplicate[0] if not_duplicate else duplicate[0]
        print(f'guess: {guess}')
        
        if len(guess) != 5 or guess not in ta:
            print('invalid word!')
            continue
        
        result = check(guess, answer)
        print(f'result: {result}\n')

        if result == [2, 2, 2, 2, 2]:
            bingo = True
            break

        not_duplicate = [answer for answer in not_duplicate if check(guess, answer) == result]
        duplicate = [answer for answer in duplicate if check(guess, answer) == result]
        ta = [answer for answer in ta if check(guess, answer) == result]
        print(len(ta))
        print(len(pa))

        n += 1
    
    return n


if __name__ == '__main__':
    total = 0
    n = [0] * 16
    for _ in range(100):
        num = game(pa, ta, not_duplicate, duplicate) + 1
        total += num
        n[num] += 1
        print(num)

    print()

    print(total / 100)

    for i in range(1, 16):
        print(f'{i}: {n[i]}')
