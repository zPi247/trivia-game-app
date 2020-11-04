#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
import random
import csv


def check_ans():
    global quest_num, score, play
    save_ans = e2.get()
    if e2.get() == trivia_answers[quest_num-1]:
        var.set('\nCorrect answer!\n')
        score = score + 1
        e2.delete(0, 'end')
    else:
        var.set('\nWrong answer!\nYour answer: '+save_ans+'\nCorrect answer: '+trivia_answers[quest_num-1]+'\n')
        e2.delete(0, 'end')
    if quest_num != 5:
        qu.set('\n\n'+trivia_questions[quest_num]+'\n\n')
        quest_num = quest_num + 1
    else:
        e2.delete(0, 'end')
        e2.config(state='disabled')
        e2.pack()
        if score == 5:
            tk.messagebox.showinfo(title='Well Done!', message='You got full score!')
        res = tk.messagebox.askquestion('Replay', 'Game end! Your score is '+str(score)+'.\nDo you want to replay?')
        if res == 'no':
            play = False
        else:
            tk.messagebox.showinfo(title='Notice', message='Please close this window.')


def num_gen():
    # generate random num
    sel = []
    sel.append(random.randint(1, count - 1))
    sel.append(random.randint(1, count - 1))
    while sel[1] == sel[0]:
        sel[1] = random.randint(1, count - 1)
    sel.append(random.randint(1, count - 1))
    while sel[2] == sel[1] or sel[2] == sel[0]:
        sel[2] = random.randint(1, count - 1)
    sel.append(random.randint(1, count - 1))
    while sel[3] == sel[2] or sel[3] == sel[1] or sel[3] == sel[0]:
        sel[3] = random.randint(1, count - 1)
    sel.append(random.randint(1, count - 1))
    while sel[4] == sel[3] or sel[4] == sel[2] or sel[4] == sel[1] or sel[4] == sel[0]:
        sel[4] = random.randint(1, count - 1)
    return sel


play = True
while play:
    # variables
    score = 0
    trivia_questions = []
    trivia_answers = []
    quest_num = 0

    # count CSV lines
    count = 0
    filename = 'questions.csv'
    with open(filename, 'r', encoding='utf-8')as f:
        read = f.readlines()
        for index, info in enumerate(read):
            count += 1

    selected = num_gen()

    # Read and print CSV
    with open('questions.csv', 'r') as f:
        reader = csv.reader(f)
        row = list(reader)
        for i in range(0, 5):
            trivia_questions.append(row[selected[i]][1])
            trivia_answers.append(row[selected[i]][2])

    # tkinter
    window = tk.Tk()
    window.title("Movie Trivia")
    window.geometry("1000x500")

    qu = tk.StringVar()
    qu.set('\n\n' + trivia_questions[quest_num] + '\n')
    quest_num += 1
    l1 = tk.Label(window, bg='white', width=40, textvariable=qu, font=('Palatino', 18), wraplength=250)
    l1.pack()

    e2 = tk.Entry(window, show=None, font=('Palatino', 15))
    e2.pack()

    var = tk.StringVar()
    l2 = tk.Label(window, textvariable=var, bg='white', fg='black', font=('Palatino', 15), width=50, wraplength=250)
    l2.pack()

    b = tk.Button(window, text='Check Answer', font=('Palatino', 14), width=20, height=2, command=check_ans)
    b.pack()

    window.mainloop()
