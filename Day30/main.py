from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project from Day 5. Add list comprehension to improve password generation.
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    # Clear previous password
    Password_Entry.delete(0, END)
    Password_Entry.insert(0, password)
    # Add password to clipboard
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # Triggered when search button is pressed
    web_name = Website_Entry.get()
    user_email = Email_User_Entry.get()
    user_password = Password_Entry.get()
    # Check if user's text entry matches an item in data.json
    try:
        with open("data.json", "r") as data_file:
            # Read data
            data = json.load(data_file)
            # If yes, show a messagebox with website's name and password
            if web_name in data:
                contains_password = messagebox.askokcancel(title=f"{web_name}",
                                                    message=f"These are the details: \nEmail: {data[web_name]['email']}"
                                                    f"\nPassword: {data[web_name]['password']}")

    # Catch an exception that might occur trying to access the data.json
    except FileNotFoundError:
        print("File not found")
        no_file = messagebox.showwarning(title="Warning!", message="No Data File Found")

    # If the user's website does not exist inside data.json show message
    with open("data.json", "r") as data_file:
        # Read data
        data = json.load(data_file)
        if web_name not in data:
            no_details = messagebox.showwarning(title="Warning!", message="No details for the website exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get Website
    web_name = Website_Entry.get()
    # Get Email & Username
    user_email = Email_User_Entry.get()
    # Get Password
    user_password = Password_Entry.get()

    new_data = {
        web_name: {
            "email": user_email,
            "password": user_password,
        }
    }

    # Check to ensure that all fields are populated
    if len(web_name) > 0 and len(user_email) > 0 and len(user_password) > 0:
        is_acceptable = messagebox.askokcancel(title=f"{web_name}",
                                               message=f"These are the details entered: \nEmail: {user_email} "
                                                       f"\nPassword: {user_password} \nIs it okay to save?")

        if is_acceptable:
            try:
                with open("data.json", "r") as data_file:
                    # Read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "x") as data_file:
                    json.dump(new_data, data_file, indent=4)
                # Update old data with new data
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                Website_Entry.delete(0, END)
                Password_Entry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20)
window.grid_columnconfigure(index=3)
window.grid_rowconfigure(index=5)

logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

Website = Label(text="Website:", font=("Times New Roman", 12))
Website.grid(column=0, row=1)
Website_Entry = Entry(width=21)
Website_Entry.grid(column=1, row=1, sticky="EW")
# Set cursor in website entry by default
Website_Entry.focus()

Email_Username = Label(text="Email/Username:", font=("Times New Roman", 12))
Email_Username.grid(column=0, row=2)
Email_User_Entry = Entry(width=35)
Email_User_Entry.grid(column=1, row=2, columnspan=2, sticky="EW")
# Set email to populate the email_username field by default
Email_User_Entry.insert(0, "test@example.com")

Password = Label(text="Password:", font=("Times New Roman", 12))
Password.grid(column=0, row=3)
Password_Entry = Entry(width=21)
Password_Entry.grid(column=1, row=3, sticky="EW")

# Buttons
Generate_Password = Button(text="Generate Password", command=generate_password)
Generate_Password.grid(column=2, row=3, sticky="EW")
Add_Button = Button(text="Add", width=35, command=save)
Add_Button.grid(column=1, row=4, columnspan=2, sticky="EW")
Search_Button = Button(text="Search", command=find_password)
Search_Button.grid(column=2, row=1, sticky="EW")

window.mainloop()
