from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = -10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.one_car()
        self.move_speed = 0.1

    def one_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        new_y = random.randint(-300, 300)
        self.goto(300, new_y)

    def moving_car(self):
        self.forward(MOVE_INCREMENT)

