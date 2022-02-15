import tkinter
from tkinter import *
from tkinter import messagebox
import random
import json
FONT_NAME = 'Arial'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    site_cautat = website_entry.get()
    try:
        with open('passwords.json', 'r') as fisier:
            date = json.load(fisier)
            messagebox.showinfo(title=f"{site_cautat}", message=f"mail: {date[site_cautat]['email']}\n"
                                                                f"parola: {date[site_cautat]['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Eroare", message="Nu exista fisierul")
    except KeyError:
        messagebox.showerror(title="Eroare", message="Nu exista detalii despre site")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def parola_random():
    copy_letters = letters
    copy_numbers = numbers
    copy_symbols = symbols

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password = ""

    while nr_letters != 0:
        letter = copy_letters[random.randint(0, len(copy_letters) - 1)]
        password += letter
        nr_letters -= 1

    while nr_numbers != 0:
        number = copy_numbers[random.randint(0, len(copy_numbers) - 1)]
        password += number
        nr_numbers -= 1

    while nr_symbols != 0:
        symbol = copy_symbols[random.randint(0, len(copy_symbols) - 1)]
        password += symbol
        nr_symbols -= 1

    password_v2 = []
    for i in password:
        password_v2.append(i)

    password_randomised = ""
    number_of_characters = len(password_v2)

    while number_of_characters != 0:
        character = password_v2[random.randint(0, number_of_characters - 1)]
        password_randomised += character
        password_v2.remove(character)
        number_of_characters -= 1

    password_entry.insert(END, string=password_randomised)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_click():
    #luam datele din fiecare casuta
    nou_site = website_entry.get()
    nou_mail = email_username_entry.get()
    noua_parola = password_entry.get()
    new_data = {
        nou_site:{
            'email': nou_mail,
            'password': noua_parola
        }
    }

    if nou_site == "" or nou_mail == "" or noua_parola == "":
        messagebox.showerror(title="Eroare", message="Verificati din nou datele introduse")
    else:
        try:
            # le scriem in fisier
            with open('passwords.json', 'r') as fisier:
                # scrierea intr-un fisier de tip json:
                # json.dump(new_data, fisier, indent=5)

                # citirea datelor dintr-un fisier json
                # date = json.load(fisier)

                # actualizarea datelor intr-un fisier json
                date = json.load(fisier)
                date.update(new_data)
            with open('passwords.json', 'w') as fisier:
                json.dump(date, fisier, indent=5)
                # stergem continutul care probabil va trebui schimbat
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        except FileNotFoundError:
            with open('passwords.json', 'w') as fisier:
                json.dump(new_data, fisier, indent=5)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Managerul de parole")
window.config(padx=20, pady=20)



canvas = Canvas(width=200, height=190, highlightthickness=0)
poza_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=poza_logo)
canvas.grid(row=0, column=1)

website = Label(text='Website:', font=(FONT_NAME, 15, 'normal'))
website.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1, sticky=tkinter.W)
website_entry.focus()

email_username = Label(text='Email/Username:', font=(FONT_NAME, 15, 'normal'))
email_username.grid(row=2, column=0)
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky=tkinter.W)
email_username_entry.insert(END, string="marinescumatei99@gmail.com")

password = Label(text='Password:', font=(FONT_NAME, 15, 'normal'))
password.grid(row=3, column=0)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2, sticky=tkinter.W)


generate_password = Button(text='Generate Password', font=(FONT_NAME, 15, 'normal'), width=16, command=parola_random)
generate_password.grid(row=3, column=2, sticky=tkinter.W, columnspan=2)

add = Button(text='Add', font=(FONT_NAME, 15, 'normal'), width=36, command=add_click)
add.grid(row=4, column=1,  sticky=tkinter.E, columnspan=2)

search = Button(text='Search', font=(FONT_NAME, 15, 'normal'), width=16, command=search_password)
search.grid(row=1, column=2, sticky=tkinter.W, columnspan=2)

window.mainloop()