from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 'o', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '\\', '|', '~']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)

    password = ''.join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    if website == '' or password == '':
        messagebox.showinfo(
            title="Oops!", message=f"Please don't leave field's empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email_username} "
            "\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            information = f'{website} | {email_username} | {password}\n'
            file_write(information)


def file_write(information):
    with open("data.txt", 'a') as data_file:
        data_file.write(information)
        entry_website.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(
    file='./logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
label_website = Label(text='Website:', font=('Arial', 10, 'bold'))
label_website.grid(row=1, column=0)

label_email_username = Label(
    text='Email/Username:', font=('Arial', 10, 'bold'))
label_email_username.grid(row=2, column=0)

label_password = Label(text='Password:', font=('Arial', 10, 'bold'))
label_password.grid(row=3, column=0)

# entry
entry_website = Entry(width=52)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email_username = Entry(width=52)
entry_email_username.grid(row=2, column=1, columnspan=2)
entry_email_username.focus()
entry_email_username.insert(0, 'your_email@example.com')

entry_password = Entry(width=33)
entry_password.grid(row=3, column=1)
entry_password.focus()

# button
button_generate_password = Button(
    text='Generate Password', command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text='Add', width=44, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
