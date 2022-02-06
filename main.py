from tkinter import *

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

head_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"))
head_label.grid(column=1, row=0)

check_label = Label(text="v", fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_label.config(pady=20)
check_label.grid(column=1, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"))
reset_button.grid(column=2, row=2)


window.mainloop()