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
cars = []
count = 0
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1

    # turtle crosses finish line
    if player.ycor() > 280:
        player.starting_position()
        scoreboard.increase_score()

    # Every 6th loop make a new car
    if count == 6:
        car = CarManager()
        cars.append(car)
        count = 0

    # Move forward cars in list
    for c in cars:
        c.moving_car()
        if c.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
