import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty")
        return

    is_ok_to_save = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                             f"\nPassword: {password}"f"\nIs it okay to save?")

    if is_ok_to_save:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)




# --------------------------- FIND PASSWORD --------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website_details = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Ouch", message="No details for the website exist")
    else:
        email = website_details["email"]
        password = website_details["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#Entries
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "uthmanqamarudeen@gmail.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)


#Buttons
password_button = Button(text="Generate password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)







window.mainloop()