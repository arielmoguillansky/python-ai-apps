from turtle import Screen, Turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import scoreboard

DIFFICULTY = {
    "easy": 0.3,
    "medium": 0.1,
    "hard": 0.05,
}

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
score = Scoreboard()
snake = Snake()
food = Food()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(DIFFICULTY["medium"])
    snake.move()

    if snake.head.distance(food) < 15:
        food.set_position()
        snake.add_segment()
        score.sum_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False






screen.exitonclick()
