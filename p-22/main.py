from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.up,"Up")

game_on = True

while game_on:
    time.sleep(0.2)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.finish_line():
        player.reset()
        car_manager.level_up()
        score.level_up()

screen.exitonclick()