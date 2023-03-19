from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20)
window.grid_columnconfigure(index=3)
window.grid_rowconfigure(index=5)

logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, background='gray75')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)


Website = Label(bg="red", text="Website:", font=("Times New Roman", 12))
Website.grid(column=1, row=2)
Website_Entry = Entry(width=35)
Website_Entry.grid(column=2, row=2)


Email_Username = Label(bg="red", text="Email/Username:", font=("Times New Roman", 12))
Email_Username.grid(column=1, row=3)
Email_User_Entry = Entry(width=35)
Email_User_Entry.grid(column=2, row=3)

Password = Label(bg="red", text="Password:", font=("Times New Roman", 12))
Password.grid(column=1, row=4)
Password_Entry = Entry(width=21)
Password_Entry.grid(column=2, row=4)

Generate_Password = Button(text="Generate Password", width=14)
Generate_Password.grid(column=3, row=4)
# Create Add button
Add_Button = Button(text="Add", width=36)
Add_Button.grid(column=2, row=5)

window.mainloop()
