from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip

def insert_generated_password():
    password_entry.delete(0, END)
    pwd = generate_password()
    password_entry.insert(0, pwd)
    pyperclip.copy(pwd)

def check_entries(*args):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        add_btn.config(state="normal")
    else:
        add_btn.config(state="disabled")


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    confirm_save = messagebox.askokcancel(title=website,
                                          message=f"Your password has been saved: \n Email: {email} | Password:{password} \n Is this correct?")

    if confirm_save:
        with open("data.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

        add_btn.config(state="disabled")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except Exception:
    pass
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website: ")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

web_text = StringVar()
email_text = StringVar()
pass_text = StringVar()

web_text.trace_add("write", check_entries)
email_text.trace_add("write", check_entries)
pass_text.trace_add("write", check_entries)

website_entry = Entry(width=35, textvariable=web_text)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35, textvariable=email_text)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21, textvariable=pass_text)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate Password", command=insert_generated_password)
generate_btn.grid(row=3, column=2)

# Starts disabled by default
add_btn = Button(text="Add", width=36, command=save, state="disabled")
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()