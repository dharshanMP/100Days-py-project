# basics of tkinter

from tkinter import *


window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# label

label = Label(text = "Hi!")
label.pack()

# button

def button_clicked():

    new_text = input.get()
    label.config(text=new_text)
    

button = Button(text="click me", command = button_clicked)
button.pack()

# Entry 

input = Entry()
input.pack()

window.mainloop()


# *args

'''def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum    

print(add(1, 2, 4, 5))'''


# **kwargs

'''def calculate(n, **kwargs):
    n += kwargs["add"]
    n += kwargs["subtract"]
    print(n)


calculate(3, add = 10, subtract = 4)'''
