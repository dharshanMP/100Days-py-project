from tkinter import *

def km_converting():
    miles = float(user_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=25, pady=25)

user_input = Entry(width=7)
user_input.grid(column=1 , row=0)

mile_lable = Label(text="miles")
mile_lable.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)


km_label = Label(text="km")
km_label.grid(column=2, row=1)

button = Button(text = "Calculate", command=km_converting)
button.grid(column=1, row=2)






window.mainloop()