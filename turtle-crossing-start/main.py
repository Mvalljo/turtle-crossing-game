import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # turtle crosses finish line
    if player.ycor() > 280:
        player.starting_position()
        scoreboard.increase_score()

    # Every 6th loop make a new car

    # Move forward cars in list

screen.exitonclick()
