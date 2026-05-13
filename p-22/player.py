from turtle import Turtle
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
FORWARD = 10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.reset()

    def up(self):
        self.forward(FORWARD)

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)