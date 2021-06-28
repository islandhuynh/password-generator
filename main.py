from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_credentials():
  with open("data.txt", 'a') as data:
    credentials = f"{website_input.get()} | {username_input.get()} | {password_input.get()} \n"
    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()
    data.write(credentials)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=60)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=60)
username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=22)
generate_password_button.grid(column=2, row=3)

add_cred_button = Button(text="Add", width=42, command=save_credentials)
add_cred_button.grid(column=1, row=4, columnspan=2)

window.mainloop()