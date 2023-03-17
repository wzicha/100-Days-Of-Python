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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    # timer text set to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label set to "timer"
    timer_label.config(text="Timer")
    # reset check marks
    checkmark.config(text="")
    # reset reps
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep:
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    # If it's the 8th rep:
    elif reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    # if it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks = int(reps / 2)
            for num in range(checkmarks):
                checkmark.config(text=checkmark["text"] + "✓")


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

checkmark = Label(fg=GREEN, highlightthickness=0)
checkmark.grid(row=4, column=2)

# Create Start & Reset Buttons

start_button = Button(text="Start", font=("Times New Roman", 12, "bold"), command=start_timer)
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", font=("Times New Roman", 12, "bold"), command=reset_timer)
reset_button.grid(row=3, column=3)

window.mainloop()
