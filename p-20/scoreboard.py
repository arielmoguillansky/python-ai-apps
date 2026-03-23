from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.hideturtle()
        self.color("white")
        self.write_score()

    def sum_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("Arial", 18, "normal"))


    def write_score(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.write(f"score: {self.score}", False, align="center", font=("Arial", 18, "normal"))