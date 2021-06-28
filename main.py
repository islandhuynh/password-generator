from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(): 
  password_input.delete(0, END)

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(0, nr_letters-1)]
  password_symbols = [random.choice(symbols) for _ in range(0, nr_symbols-1)]
  password_numbers = [random.choice(numbers) for _ in range(0, nr_numbers-1)]
  password_list = password_letters + password_symbols + password_numbers

  random.shuffle(password_list)

  password = "".join(password_list)

  password_input.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_credentials():
  website = website_input.get()
  username = username_input.get()
  password = password_input.get()
  new_data = {
    website.title(): {
      "email": username,
      "password": password
    }
  }

  if len(username) == 0 or len(password) == 0 or len(website) == 0:
    messagebox.showwarning(title="Oops", message="Please do not leave any fields empty!")
    return

  confirm_credentials = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail/Username: {username}\nPassword: {password}\nIs it okay to save?")

  if confirm_credentials:
    try: 
      with open("data.json", 'r') as data_file:
        # Reading old data
        data = json.load(data_file)
        # Updating old data with new data
        data.update(new_data)

    except FileNotFoundError:
        with open("data.json", 'w') as data_file: 
          # Add new data
          json.dump(new_data, data_file, indent=4)    

    else: 
      with open("data.json", 'w') as data_file: 
        # Saving updated data
        json.dump(data, data_file, indent=4)    
    
    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()

# ---------------------------- GET CREDENTIALS ------------------------------- #

def get_credentials():
  website = website_input.get().title()
  if len(website) == 0:
    messagebox.showwarning(title="Missing Website Name", message="Please enter a valid website")
    return
  
  try:
    with open("data.json", "r") as data_file:
      data = json.load(data_file)
      credentials = data[website]
  except FileNotFoundError:
    messagebox.showwarning(title="Missing Data", message="You have yet to save any credentials")
  except KeyError:
    messagebox.showwarning(title="Missing Data", message=f"There are data saved for {website}")
  else:
    messagebox.showinfo(title="Credentials", message=f"Email: {credentials['email']} \nPassword: {credentials['password']}\nPassword has been saved onto clipboard.")
    pyperclip.copy(credentials['password'])

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager by Island Huynh")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=60)
username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=32)
password_input.grid(column=1, row=3)

website_search_button = Button(text="Search", width=22, command=get_credentials)
website_search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", width=22, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_cred_button = Button(text="Add", width=42, command=save_credentials)
add_cred_button.grid(column=1, row=4, columnspan=2)

window.mainloop()