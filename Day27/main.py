from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=50)

# Labels


km = 0
miles_label = Label(text=f" Miles", font=("Arial", 12))
miles_label.place(x=185, y=28)
main_label = Label(text=f"is equal to    {km}    km", font=("Arial", 12))
main_label.place(x=50, y=50)


# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# Button

def button_clicked():
    miles = input.get()
    km = int(miles) * 1.60934
    km = round(float(km) / 100, 2)
    km = int(km * 100)
    print(f"{miles} miles is equal to    {km}    km")
    main_label.config(text=f"is equal to    {km}    km", font=("Arial", 12))


# Entry (textbox)
input = Entry(width=10, justify="center")
input.place(x=120, y=30)
# input.pack()

button = Button(text="Calculate", command=button_clicked)
button.place(x=120, y=85)
# button.pack()



window.mainloop()
