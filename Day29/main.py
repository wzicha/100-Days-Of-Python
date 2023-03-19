from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get Website
    web_name = Website_Entry.get()
    # Get Email & Username
    user_email = Email_User_Entry.get()
    # Get Password
    user_password = Password_Entry.get()
    # Merge user data into string, then save to a local file (same level as main.py)
    user_info = f"{web_name} | {user_email} : {user_password}"
    print(user_info)
    # Create file if it does not exist
    f = open("data.txt", "x")
    f = open("data.txt", "a")
    f.write(user_info)
    f.close()

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
Website_Entry = Entry(width=35)
Website_Entry.grid(column=1, row=1, columnspan=2, sticky="EW")
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
Generate_Password = Button(text="Generate Password")
Generate_Password.grid(column=2, row=3, sticky="EW")
Add_Button = Button(text="Add", width=35, command=save)
Add_Button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
