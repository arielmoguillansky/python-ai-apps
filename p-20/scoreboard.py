from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.high_score= self.read_high_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def read_high_score(self):
        with open("data.txt", "r") as file:
            return int(file.read())

    def write_high_score(self):
        with open("data.txt", "w") as file:
            return file.write(str(self.high_score))

    def sum_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", False, align="center", font=("Arial", 18, "normal"))


    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", False, align="center", font=("Arial", 18, "normal"))