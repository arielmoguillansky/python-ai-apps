from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    segments=[]
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def get_tail_position(self):
        return self.segments[len(self.segments) -1].position()

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        last_position = self.get_tail_position()
        new_segment.goto(last_position)
        self.segments.append(new_segment)

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(FORWARD)

    def up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(90)

    def down(self):
        if int(self.head.heading()) != UP:
            self.head.setheading(270)

    def left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.setheading(180)

    def right(self):
        if int(self.head.heading()) != LEFT:
             self.head.setheading(0)

