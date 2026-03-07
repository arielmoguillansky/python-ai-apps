from turtle import Turtle, Screen
import random
from tkinter import messagebox

screen_width = 1.0
screen_height = 600
scuderias = ["rb", "mer", "fer", "mc", "am", "al", "wi", "rb2", "ks", "ha"]
screen = Screen()
screen.setup(screen_width, screen_height)
is_race_on = False
turtles = {}
line_pos = (screen.window_width() / 2) - 50
x_pos = -(screen.window_width() / 2) + 25
y_pos = -180
screen.register_shape("rb","sprites/1.png")
screen.register_shape("mer","sprites/2.png")
screen.register_shape("fer","sprites/3.png")
screen.register_shape("mc","sprites/4.png")
screen.register_shape("am","sprites/5.png")
screen.register_shape("al","sprites/6.png")
screen.register_shape("wi","sprites/7.png")
screen.register_shape("rb2","sprites/8.png")
screen.register_shape("ks","sprites/9.png")
screen.register_shape("ha","sprites/10.png")

scuderias_code = {
    "rb": "redbull",
    "mer": "mercedes",
    "fer": "ferrari",
    "mc": "mclaren",
    "am": "astonmartin",
    "al": "alpine",
    "wi": "willams",
    "rb2": "racingbulls",
    "ks": "kicksauber",
    "ha": "haas",
}


referee = Turtle()
referee.hideturtle()
referee.speed(10)
referee.penup()

referee.goto(line_pos, 240)
referee.setheading(270) # Point Down
referee.pensize(5)
referee.pencolor("black")

referee.pendown()
for _ in range(12):
    referee.forward(20)
    referee.penup()
    referee.forward(20)
    referee.pendown()

for scuderia in scuderias:
    turtles[f"turtle_{scuderia}"] = Turtle(shape=scuderia)
    turtles[f"turtle_{scuderia}"].speed(10)
    turtles[f"turtle_{scuderia}"].penup()
    turtles[f"turtle_{scuderia}"].goto(x_pos, y_pos)
    y_pos = y_pos + 40

def get_speed_number():
    return random.randint(10,25)



user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower().replace(" ", "")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtles[turtle].forward(get_speed_number())
        if turtles[turtle].xcor() >= line_pos:
            is_race_on = False
            winner_code = turtles[turtle].shape()
            winner =scuderias_code[winner_code]
            if winner == user_bet:
                messagebox.showinfo("showinfo", f"YOU WIN! Winner is team {winner}!")
                break
            else:
                messagebox.showinfo("showinfo", f'YOU LOOSE! Winner is team {winner}! You chose {user_bet}.')
                break

screen.exitonclick()
