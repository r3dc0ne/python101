import tkinter as tk
from datetime import date
from tkinter import messagebox


def show_date():
    global click_counter
    click_counter += 1
    date_today = str(date.today())
    messagebox.showinfo("The date today", date_today)
    label.config(text="Button was clicked " + str(click_counter) + " times")
    # window.destroy()


window = tk.Tk()

click_counter = 0

label = tk.Label(window)
label.pack()

button = tk.Button(window, text="Ok", command=show_date)
button.pack()

window.mainloop()


