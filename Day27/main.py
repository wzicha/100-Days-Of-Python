from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=200)

# Label

km = 0
my_label = Label(text=f"is equal to {km} km", font=("Arial", 12), compound="bottom")
my_label.pack()


# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# Button

def button_clicked():
    miles = input.get()
    km = int(miles) * 1.60934
    km = round(float(km) / 100, 2)
    km = int(km * 100)
    print(f"{miles} miles are equal to {km} km")
    my_label.config(text=f"is equal to {km} km", font=("Arial", 12), compound="bottom")


# Entry
input = Entry(width=10, justify="center")
input.pack()

button = Button(text="Calculate", command=button_clicked)
button.pack()

window.mainloop()
