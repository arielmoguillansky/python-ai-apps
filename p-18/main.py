from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def rot_clockwise():
    turtle.right(45)

def rot_counter_clockwise():
    turtle.left(45)

def clear_draw():
    turtle.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rot_clockwise)
screen.onkey(key="a", fun=rot_counter_clockwise)
screen.onkey(key="c", fun=clear_draw)

screen.exitonclick()