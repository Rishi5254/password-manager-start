import json
from tkinter import *
import random
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


CAPITALS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?", "/", "|", "+"]
all_letters = CAPITALS + small_letters + numbers + symbols


def generate_pass():
    RANDOM_PASS = " "
    chars = random.randint(11, 15)
    generated_random_pass = [random.choice(all_letters) for i in range(chars)]
    for n in generated_random_pass:
        RANDOM_PASS += str(n)
    password_entry.insert(END, RANDOM_PASS)
    pyperclip.copy(RANDOM_PASS)

# ----------------------------- SEARCH ---------------------------------- #

def search():
    site = website_entry.get()
    try:
        with open(file="file.json", mode="r") as file2:
            data = json.load(file2)
    except:
        messagebox.showinfo(site, f"The {site} is not present in data base\nYour Database is empty")
    finally:
        try:
            data[site]
        except KeyError as key:
            print(f"{key} website is not present in the database try again")
            messagebox.showinfo(key, f"The {key} website is not present in the database try another one ")
        else:
            email = (data[site]["email"])
            password = (data[site]["password"])
            messagebox.showinfo(site, f"Email : {email}\nPaswoord :{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_into_database():
    email = email_username_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    disc = {
         website: {
           "email": email,
           "password": password
      }
    }
    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Important", message="Please dont leave any feields empty")
    else:
        is_ok = messagebox.askyesnocancel(title=website, message=(f"You have Entered\nwebsite: {website}\npassword: {password}"))
        if is_ok:
            try:
                with open(file="file.json", mode="r") as file:
                    data = json.load(file)
            except :
                with open(file="file.json", mode="w", ) as file:
                    json.dump(disc, file, indent=4)

            else:
                data.update(disc)
                with open(file="file.json",mode="w",) as file:
                    json.dump(data, file, indent=4)
            finally:
                password_entry.delete(0, END)
                website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=30)

# IMAGE
canvas = Canvas(width=200, height=200)
image_1 = PhotoImage(file="logo.png")
canvas.create_image(60, 90, image=image_1)
canvas.grid(column=1, row=0, pady=10)


# LABELS

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(padx=15, pady=5)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_label.config(padx=15, pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=15, pady=5)

# ENTRIES

website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(column=1, row= 1, sticky="w")

email_username_entry = Entry(width=50)
email_username_entry.insert(0, "rishirishik18@gmail.com")
email_username_entry.grid(column=1, row=2)


password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky="w")

# BUTTONS
search_button = Button(text="Search", width=20, command=search)
search_button.grid(column=1, row=1, sticky="e")

generate_button = Button(text="Generate Password", width=20, command=generate_pass)
generate_button.grid(column=1, row=3, sticky="e")

add_button = Button(text="Add", width=45, command=save_into_database)
add_button.grid(column=1, row=4)

window.mainloop()