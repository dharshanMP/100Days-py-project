from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#---------------------------------------------FLASH CARDS------------------------------#
try:
    data = pandas.read_csv("words.csv", encoding="latin-1")

except FileNotFoundError:
    orginal_data = pandas.read_csv("words_data", encoding="latin-1")   
    to_learn = orginal_data.to_dict(orient="records")

else:     
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["german"], fill="black")
    canvas.itemconfig(bg_img, image=card_f_img)
    flip_timer = window.after(3000, func=flip_card)
    



def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["english"], fill="white")
    canvas.itemconfig(bg_img, image=card_b_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words.csv", index=False)
    next_card()    

#---------------------------------------------WINDOW-----------------------------------#

window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) 

canvas = Canvas(width=800, height=526)
card_f_img = PhotoImage(file="images/card_front.png")
card_b_img = PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image = card_f_img)
card_title = canvas.create_text(400, 150,text="", font=("arial", 40))
card_word = canvas.create_text(400, 263, text="", font=("arial, 40"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)





cross_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unkown_button.grid(row=1, column=0)


tick_image = PhotoImage(file="images/right.png")
known_button = Button(image=tick_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)



next_card()

window.mainloop()