import json

with open('answers.json', 'r') as f:
    answers = json.load(f)
    pa = answers['possible_answers']
    ta = answers['total_answers']

frequency = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
}

for word in pa:
    for ch in word:
        frequency[ch] += 1

def score(word, frequency):
    n = 0
    for ch in word:
        n += frequency[ch]
    return n

pa.sort(key = lambda ans: score(ans, frequency), reverse = True)
ta.sort(key = lambda ans: score(ans, frequency), reverse = True)

with open('answers.json', 'w') as f:
    answers['possible_answers'] = pa
    answers['total_answers'] = ta
    json.dump(answers, f, indent = 4)
