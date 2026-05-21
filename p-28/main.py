from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BG_RED = "#f05b56"
LIGHT_RED = "#f26c67"
GREEN = "#9bdeac"
LIGHT_YELLOW = "#f7f5dd"
YELLOW = "#FFDB58"
FONT_NAME = "Modern"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        active_label.config(text="LONG BREAK!", background=GREEN)
        window.configure(background=GREEN)
        canvas.config(background=GREEN)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        active_label.config(text="SHORT BREAK!", background=YELLOW)
        window.configure(background=YELLOW)
        canvas.config(background=YELLOW)
        canvas.itemconfig(my_rectangle, fill=LIGHT_YELLOW)
        countdown(short_break_sec)
    else:
        window.configure(background=BG_RED)
        active_label.config(text="FOCUS!")
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, countdown, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

window = Tk()
window.title("Pomodoro App")
window.configure(background=BG_RED, padx=15, pady=15)

canvas = Canvas(window, width=800, height=600, bg=BG_RED, highlightthickness=0)

my_rectangle = round_rectangle(150, 150, 650, 450, radius=10, fill=LIGHT_RED, outline="")
timer_text = canvas.create_text(400,300, tex="00:00", fill="white", font=(FONT_NAME, 100, "bold"))

active_label = Label(text="", background=BG_RED, font=(FONT_NAME, 14), width=20, fg="white")
short_break_label = Label(text="Short Break", background=BG_RED, font=(FONT_NAME, 14), width=20, fg="white")
long_break_label = Label(text="Long Break", background=BG_RED, font=(FONT_NAME, 14), width=20, fg="white")

start_button = Button(text="START", highlightthickness=0, background="white", fg=BG_RED, font=(FONT_NAME, 14, "bold"),  width=10, borderwidth=0, cursor="hand2", relief="flat", command=start_timer)
reset_button = Button(text="RESET", highlightthickness=0, background="white", fg=BG_RED, font=(FONT_NAME, 14, "bold"), width=10, borderwidth=0, cursor="hand2", relief="flat")

start_button.grid(row=2, column=1, pady=10)
reset_button.grid(row=3, column=1)
active_label.grid(row=0, column=1)

canvas.grid(row=1, column=1)

















window.mainloop()