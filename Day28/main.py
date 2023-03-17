from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

# Grid setup, to properly format the elements in the UI

window.grid_columnconfigure(index=3)
window.grid_rowconfigure(index=5)
window.config(padx=100, pady=50, bg=YELLOW)

# Labels and placement (Timer text, Image + countdown text and checkmark)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
timer_label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

checkmark = Label(text="✓", fg=GREEN, highlightthickness=0)
checkmark.grid(row=4, column=2)

# Create Start & Reset Buttons

start_button = Button(text="Start", font=("Times New Roman", 12, "bold"), command=start_timer)
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", font=("Times New Roman", 12, "bold"))
reset_button.grid(row=3, column=3)

window.mainloop()
