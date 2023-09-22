import tkinter as tk
from tkinter import messagebox


def window_design():
    first_window = tk.Tk()
    label = tk.Label(first_window)
    label.pack()
    label.config(text="I have a question")

    button = tk.Button(first_window, text="Ok", command=question_window)
    button.pack()

    first_window.mainloop()


def question_window():
    second_window = tk.Tk()
    question = tk.Label(second_window)
    question.pack()
    question.config(text="Will you visit me in Tromso?")

    buttons_yes_no(second_window)


def buttons_yes_no(window):
    button_yes = tk.Button(window, text="Yes")
    button_yes.pack()

    button_no = tk.Button(window, text="No", command=please)
    button_no.pack()


def please():
    second_window = tk.Tk()
    question = tk.Label(second_window)
    question.pack()
    question.config(text="Please?")

    buttons_yes_no(second_window)


class StartWindow(tk.Tk):

    def __init__(self):
        super().__init__()

    window_design()


run = StartWindow()
run.mainloop()
