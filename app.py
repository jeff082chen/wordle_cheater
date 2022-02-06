import json
import tkinter as tk
import tkinter.messagebox
import random

with open('answers.json', 'r') as r:
    answers = json.load(r)

guess = ''
result = [0, 0, 0, 0, 0]

def get_result(guess, answer):
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

def transform(ss):
    if ss == 'Green':
        return 2
    elif ss == 'Yellow':
        return 1
    elif ss == 'Gray':
        return 0
    else:
        return -1

def getResult():
    global result

    result[0] = transform(var1.get())
    result[1] = transform(var2.get())
    result[2] = transform(var3.get())
    result[3] = transform(var4.get())
    result[4] = transform(var5.get())

def select():
    global answers
    global result

    for i, n in enumerate(result):
        if n == 0:
            answers = [answer for answer in answers if guess[i] not in answer]

    answers = [answer for answer in answers if get_result(guess, answer) == result]

def generate():
    myGuess.set(random.choice(answers))
    guessLabel.config(text = 'Try this: ' + myGuess.get())

def check():
    global guess

    guess = myGuess.get()
    if guess == '':
        tkinter.messagebox.showwarning('warning', 'guess a number!')
        return
    if guess not in answers:
        tkinter.messagebox.showwarning('warning', 'answer is wrong!')
        myGuess.set('')
        return

    getResult()
    select()
    myGuess.set('')
    guessLabel.config(text = 'Try this: ')
    remainLabel.config(text = f'There\'s {len(answers)} possible answers remain')

def reset():
    global answers
    global guess
    global result

    with open('answers.json', 'r') as r:
        answers = json.load(r)

    guess = ''
    result = [0, 0, 0, 0, 0]

    remainLabel.config(text = f'There\'s {len(answers)} possible answers remain')

    var1.set(optionList[2])
    var2.set(optionList[2])
    var3.set(optionList[2])
    var4.set(optionList[2])
    var5.set(optionList[2])





main = tk.Tk()
main.title('Wordle Cheater')
main.geometry('450x120')

guessLabel = tk.Label(main, text = 'Try this: ')
resultLabel = tk.Label(main, text = 'How\'s the result?')
remainLabel = tk.Label(main, text = f'There\'s {len(answers)} possible answers remain')
myGuessLabel = tk.Label(main, text = 'My Guess: ')
guessButton = tk.Button(main, text = "random", command = generate)
checkButton = tk.Button(main, text = "check", command = check)
resetButton = tk.Button(main, text = "reset", command = reset)

myGuess = tk.StringVar()
myGuessEntry = tk.Entry(main, textvariable = myGuess)

optionList = ['Green', 'Yellow', 'Gray']

var1 = tk.StringVar()
var1.set(optionList[2])
result1 = tk.OptionMenu(main, var1, *optionList)

var2 = tk.StringVar()
var2.set(optionList[2])
result2 = tk.OptionMenu(main, var2, *optionList)

var3 = tk.StringVar()
var3.set(optionList[2])
result3 = tk.OptionMenu(main, var3, *optionList)

var4 = tk.StringVar()
var4.set(optionList[2])
result4 = tk.OptionMenu(main, var4, *optionList)

var5 = tk.StringVar()
var5.set(optionList[2])
result5 = tk.OptionMenu(main, var5, *optionList)



guessLabel.place(x = 0, y = 0, width = 120, height = 20)
guessButton.place(x = 120, y = 0, width = 55, height = 20)

myGuessLabel.place(x = 0, y = 25, width = 120, height = 20)
myGuessEntry.place(x = 120, y = 25, width = 120, height = 20)

resultLabel.place(x = 0, y = 50, width = 120, height = 20)
result1.place(x = 120, y = 50, width = 55, height = 20)
result2.place(x = 175, y = 50, width = 55, height = 20)
result3.place(x = 230, y = 50, width = 55, height = 20)
result4.place(x = 285, y = 50, width = 55, height = 20)
result5.place(x = 340, y = 50, width = 55, height = 20)

checkButton.place(x = 20, y = 75, width = 55, height = 20)
remainLabel.place(x = 95, y = 75, width = 250, height = 20)

resetButton.place(x = 20, y = 100, width = 55, height = 20)

main.mainloop()
