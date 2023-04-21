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
s = 60
rep = 0
tim = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(tim)
    timer.config(text='Timer',foreground=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_time, text="00:00")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    working = WORK_MIN * s
    short = SHORT_BREAK_MIN * s
    lon = LONG_BREAK_MIN * s
    global rep
    rep += 1
    if rep % 8 == 0:
        countdown(lon)
        timer.config(text='REST', fg=RED)
    elif rep % 2 == 0:
        countdown(short)
        timer.config(text='BREAK', fg=PINK)
    else:
        countdown(working)
        timer.config(text='WORK', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    r_min = math.floor(count / 60)
    r_sec = count % 60
    if r_sec < 10:
        r_sec = "0" + str(r_sec)
    canvas.itemconfig(timer_time, text=f"{r_min}:{r_sec}")
    if count > 0:
        global tim
        tim = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(rep/2)):
            marks += '✔'
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Time Management')
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato)
timer_time = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)
start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)
reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=3)
timer = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), foreground=GREEN, background=YELLOW, padx=20, pady=10)
timer.grid(column=1, row=0)
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)
window.mainloop()
