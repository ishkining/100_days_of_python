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

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    mark_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text='Work', fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text='Break', fg=RED)
        mark_label.config(text=reps // 2 * '✔')
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break', fg=PINK)
        mark_label.config(text=reps // 2 * '✔')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    canvas.itemconfig(timer_text, text=f'{count // 60 if count // 60 >= 10 else "0" + str(count // 60)}:'
                                       f'{count % 60 if count % 60 >= 10 else "0" + str(count % 60)}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 35, 'bold'), bg=YELLOW)
title_label.grid(column=1, row=0)

mark_label = Label(text='', fg=GREEN, font=(FONT_NAME, 15, 'bold'), bg=YELLOW)
mark_label.grid(column=1, row=3)

button_start = Button(text='Start', width=8, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', width=8, command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()