from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=20)
window.grid_columnconfigure(index=3)
window.grid_rowconfigure(index=5)
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=400, height=400, background='gray75')
canvas.create_image(200, 200, image=logo)
# canvas.pack(ipadx=20)
canvas.grid(column=2, row=1)

Website = Label(bg="red", text="horse", font=("Times New Roman" , 12))
Website.grid(column=0, row=2)


window.mainloop()
