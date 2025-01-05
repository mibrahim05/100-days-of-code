from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
from typing import final

import pyperclip
import json

from django.template.defaultfilters import title


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10)) ]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = web_entry.get()
    username = email_user_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email": username,
            "password":password,

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't leaved any field empty")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)

            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0,END)
            password_entry.delete(0,END)


def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #





window = Tk()
window.title("Password Manger")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100 ,image=logo_img)
canvas.grid(column = 1,row=0)


#LABELS
web_label = Label(text="Website:")
web_label.grid(column = 0,row=1)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#ENTRIES
web_entry = Entry(width=33)
web_entry.grid(column=1,row=1)
web_entry.focus()
email_user_entry= Entry(width=52)
email_user_entry.grid(column=1,row=2,columnspan=2)
email_user_entry.insert(0,"ibrahim05@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)

#BUTTONS
search_button = Button(text="Search",command=find_password)
search_button.grid(column = 2,row = 1,sticky="EW")
generate_button =Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,sticky="EW")
add_button = Button(text="Add",width=44,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()