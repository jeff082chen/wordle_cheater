import json
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from test.sort import sort

with open('answers.json', 'r') as r:
    answers = json.load(r)

pa = answers['possible_answers']
ta = answers['total_answers']

not_duplicate = [ans for ans in pa if len(set(ans)) == 5]
duplicate = [ans for ans in pa if len(set(ans)) < 5]
assert len(not_duplicate) + len(duplicate) == len(pa), 'error'

guess = ''
result = [0, 0, 0, 0, 0]

def get_result(guess, answer):
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

def transform(ss):
    if ss == '🟩':
        return 2
    elif ss == '🟨':
        return 1
    elif ss == '⬜':
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
    global pa
    global ta
    global duplicate
    global not_duplicate
    global result

    pa = [answer for answer in pa if get_result(guess, answer) == result]
    ta = [answer for answer in ta if get_result(guess, answer) == result]
    not_duplicate = [answer for answer in not_duplicate if get_result(guess, answer) == result]
    duplicate = [answer for answer in duplicate if get_result(guess, answer) == result]

    not_duplicate = sort(not_duplicate)
    duplicate = sort(duplicate)

def generate():
    global duplicate
    global not_duplicate

    myGuess.set(not_duplicate[0] if not_duplicate else duplicate[0])
    guessLabel.config(text = 'Try this: ' + myGuess.get())

def check():
    global pa
    global ta
    global duplicate
    global not_duplicate
    global guess

    guess = myGuess.get()
    if guess == '':
        tkinter.messagebox.showwarning('warning', 'guess a number!')
        return
    if guess not in ta:
        tkinter.messagebox.showwarning('warning', 'answer is wrong!')
        myGuess.set('')
        return

    getResult()
    select()
    myGuess.set('')
    guessLabel.config(text = 'Try this: ')
    remainLabel.config(text = f'There\'s {len(ta)} possible answers remain')
    print(len(pa))
    print(len(not_duplicate))
    print(len(duplicate))

def reset():
    global pa
    global ta
    global duplicate
    global not_duplicate
    global guess
    global result

    with open('answers.json', 'r') as r:
        answers = json.load(r)

    pa = answers['possible_answers']
    ta = answers['total_answers']
    not_duplicate = [ans for ans in pa if len(set(ans)) == 5]
    duplicate = [ans for ans in pa if len(set(ans)) < 5]

    guess = ''
    result = [0, 0, 0, 0, 0]

    remainLabel.config(text = f'There\'s {len(ta)} possible answers remain')

    var1.set(optionList[2])
    var2.set(optionList[2])
    var3.set(optionList[2])
    var4.set(optionList[2])
    var5.set(optionList[2])

def show():
    global ta

    newWindow = tk.Toplevel(main)
    newWindow.title('answers')

    scrollbar = tk.Scrollbar(newWindow)
    scrollbar.pack(side = "right", fill = "y")

    listbox = tk.Listbox(newWindow, yscrollcommand = scrollbar.set, font = tkFont.Font(size = 25))
    for answer in ta:
        listbox.insert(tk.END, answer)
    listbox.place(x = 0, y = 0, width = 450, height = 120)

    scrollbar.config(command = listbox.yview)





main = tk.Tk()
main.title('Wordle Cheater')
main.geometry('450x120')

guessLabel = tk.Label(main, text = 'Try this: ')
resultLabel = tk.Label(main, text = 'How\'s the result?')
remainLabel = tk.Label(main, text = f'There\'s {len(ta)} possible answers remain')
myGuessLabel = tk.Label(main, text = 'My Guess: ')
guessButton = tk.Button(main, text = "help", command = generate)
checkButton = tk.Button(main, text = "check", command = check)
resetButton = tk.Button(main, text = "reset", command = reset)

myGuess = tk.StringVar()
myGuessEntry = tk.Entry(main, textvariable = myGuess)

buttonExample = tk.Button(main, text = "show", command = show)

optionList = ['🟩', '🟨', '⬜']

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
buttonExample.place(x = 80, y = 100, width = 55, height = 20)

main.mainloop()
