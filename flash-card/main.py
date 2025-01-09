from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd
import random



current_class ={}
to_learn={}


#read data from csv
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()



# Background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize the window
window = Tk()
window.title("Flash Card")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)


# Create canvas with adjusted size
canvas = Canvas(width=600, height=395)

# Use pre-rounded image
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)  # Centered on canvas
card_title = canvas.create_text(300, 100, text="Title", font=("Ariel", 24, "italic"))
card_word = canvas.create_text(300, 150, text="word", font=("Ariel", 32, "bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2,pady=(0,15))

# Cross button
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0,command=next_card)
cross_button.grid(column=0, row=1,padx=15)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0,command=is_known)
check_button.grid(row=1,column=1,padx=15)

next_card()

window.mainloop()
