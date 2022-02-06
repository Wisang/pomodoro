from itertools import count
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
checked = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_button_clicked():
    window.after_cancel(timer)
    global reps
    global checked
    reps = 0
    head_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checked = ""
    check_label.config(text=checked)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        head_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        head_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        head_label.config(text="Working", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    global  checked
    min = int(count/60)
    sec = int(count%60)
    if sec < 10:
        sec = f"0{sec}"
    formatted_count = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=formatted_count)
    if count > 0:
        global timer
        timer = window.after(20, count_down, count-1)
    else:
        if reps % 2 != 0:
            checked += "v"
        check_label.config(text=checked)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

head_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
head_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.config(pady=20)
check_label.grid(column=1, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=reset_button_clicked)
reset_button.grid(column=2, row=2)


window.mainloop()