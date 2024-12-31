from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip





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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't leaved any field empty")
    else:

        is_ok = messagebox.askokcancel(title=website,message=f"These are the details you have entered :\nEmail:{username} \nPassword:{password},\n Is it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)











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
web_entry = Entry(width=52)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()
email_user_entry= Entry(width=52)
email_user_entry.grid(column=1,row=2,columnspan=2)
email_user_entry.insert(0,"ibrahim05@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)

#BUTTONS
generate_button =Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,sticky="EW")
add_button = Button(text="Add",width=44,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()