from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" :email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) ==0 or len(email) ==0:
        messagebox.showinfo(title="sorry!",message= "Please enter thr necessary details without leaving empty..." )

    else :
        try:
            with open("data.json", "r") as data:
                # reading data
                data_file = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        else:        
            # updating the new_data
            data_file.update(new_data)

            with open("data.json", "w") as data:
                # saving updated data
                json.dump(data_file, data, indent=4) 

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)


#-------------------------------------FIND PASSWORD------------------------------#

def find_password():
    website = website_entry.get()
    
    try:
        with open("data.json")as data:
            data_file = json.load(data)
    
    except FileNotFoundError:  
        messagebox.showinfo(title="Error", message="Data does not exist")    
    
    else:    
        if website in data_file:
            email = data_file[website]["email"]
            password = data_file[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Details does not exist for {website}.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#Image

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 93,image=logo_img)
canvas.grid(row=0,column=1)

# labels

website_label = Label(text="Website:")
website_label.grid(row=1)

mail_label = Label(text="Email/Username:")
mail_label.grid(row=2)

password_label = Label(text="Password:")
password_label.grid(row=3)

#Entries

website_entry = Entry(width=45)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "dharshan22@gmail.com")

password_entry = Entry(width=45)
password_entry.grid(row=3, column=1)


#Button
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width= 15, command=find_password)
search_button.grid(row=1, column=3,columnspan=1)

window.mainloop()