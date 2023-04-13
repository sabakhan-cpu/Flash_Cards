from tkinter import *
import pandas
import random
import time

mainwindow = Tk()

current_word = ""

"""reading from csv and usinf orient=records to create separate dictionary records"""
try:
 data = pandas.read_csv("./words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("french_words.csv")

    to_learn = original_data.to_dict(orient='records')
else:
    to_learn=data.to_dict(orient="records")
# print(type(to_learn))
# print(to_learn)


# print(current_word)


def next_word():
    global flip_timer
    global current_word
    mainwindow.after_cancel(flip_timer)  # to cancel the after function
    current_word = random.choice(to_learn)
    print(current_word)
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=current_word['French'], fill='black')
    canvas.itemconfig(canvas_image, image=card_front)

    flip_timer = mainwindow.after(3000, func=flip_card)  # creating a newafter fucntion


def flip_card():
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=current_word['English'], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


"""removing the data from csv file"""

"""remove the item from the to_learn list"""


def word_remove():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_word()

    # print()


"""creating window"""

mainwindow.title("Flashy")
mainwindow.config(bg="#ADD8E6", width=600, height=500)
flip_timer = mainwindow.after(3000, func=flip_card)  # the first after method
# # get the window at the center
# mainwindow.eval("tk::PlaceWindow . center")

"""sleep"""

"""creating a canvas"""
canvas = Canvas(width=800, height=526, bg="#ADD8E6", highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(800, 526, anchor='se', image=card_front)
title = canvas.create_text(400, 150, text="title", font=("Arial", 50, 'italic'))
# canvas.itemconfig(title,fill="red")
word = canvas.create_text(400, 263, text="", font=("Arial", 40, 'bold'))
canvas.place(x=210, y=20)

"""getting the buttons"""
image_right = PhotoImage(file="./images/right.png")
yes_button = Button(mainwindow, image=image_right, highlightthickness=0, command=word_remove)
yes_button.place(x=860, y=530)

image_wrong = PhotoImage(file="./images/wrong.png")
no_button = Button(mainwindow, image=image_wrong, highlightthickness=0, command=next_word)

no_button.place(x=230, y=530)
next_word()

# next_word()
mainwindow.mainloop()
