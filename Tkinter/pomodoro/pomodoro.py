import tkinter as tk
import playsound as play
import os

# ----------------------- CONSTANTS -------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None

# ---------------------- TIMER RESET ------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# -------------------PLAYING SOUND --------------------------- #
def funkymusic(songfile):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if name == songfile:
                play.playsound(os.path.abspath(os.path.join(root, name)))
    
# -------------------- TIMER MECHANISM ----------------------- #
def start_timer():
    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        title_label.config(text="Break",fg=RED)
        countdown(long_break_sec)
        funkymusic("notification.wav")
    elif reps % 2 == 0:
        title_label.config(text="Break",fg=RED)
        countdown(short_break_sec)
        funkymusic("notification.wav")
    else:
        title_label.config(text="Work",fg=RED)
        countdown(work_sec)
        funkymusic("notification.wav")

# ------------------ COUNTDOWN MECHANISM --------------------- #
def countdown(count=5):
    global timer_text
    count_seconds = count % 60
    count_min = count // 60
    if count%60 < 10:
        count_seconds = f"0{count_seconds}"
    elif count%60 >= 10:
        count_seconds = f"{count_seconds}"
    if count_min < 10:
        count_min = f"0{count_min}"
    elif count_min >= 10:
        count_min = f"{count_min}"

        
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_seconds}")
        
    if count > 0:
        global timer
        #1000 milliseconds delay, name of the function to run and then the arguments passed into the function
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for i in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ----------------------- UI SETUP --------------------------- #
#Window setup
window = tk.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW,padx=50,pady=100)

#Creating an image
canvas = tk.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,font=(FONT_NAME,35,'bold'),text='00:00',fill='white')
canvas.grid(column=1,row=1)

#Title text
title_label = tk.Label(text='Timer',fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)
check_marks = tk.Label(text='',fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=2)

#Creating buttons

start_button=tk.Button(text="Start",highlightthickness=0,command=start_timer)
reset_button=tk.Button(text="Reset",highlightthickness=0,command=reset_timer)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)

window.mainloop()
