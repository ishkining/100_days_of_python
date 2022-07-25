from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_random_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, ''.join(password_list))
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if site_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        messagebox.showinfo(title='Empty fields', message='Please fill entries!')
    else:
        is_ok = messagebox.askokcancel(title=site_entry.get(), message=f'These are the details entered: '
                                                               f'\nEmail: {email_entry.get()}'
                                                               f'\nPassword: {password_entry.get()}'
                                                              f'\nIs it okay to save?')
        if is_ok:
            with open('password.txt', 'a') as file:
                file.write(site_entry.get() + ' | ' + email_entry.get() + ' | ' + password_entry.get() + '\n')
            site_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #



my_window = Tk()
my_window.title('Password manager')
my_window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='email/username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

site_entry = Entry(width=60)
site_entry.grid(column=1, row=1, columnspan=2)
site_entry.focus()

email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'ishkining@mail.ru')

password_entry = Entry(width=40)
password_entry.grid(column=1, row=3)

generate_button = Button(text='Generate password', command=generate_random_password)
generate_button.grid(column=2, row=3)

save_button = Button(text='Add', width=52, command=save_password)
save_button.grid(column=1, row=4, columnspan=2)

my_window.mainloop()