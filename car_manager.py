import random
from random import Random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, speed ):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.penup()
        self.color(random.choices(COLORS))
        self.seth(180)
        self.show_up()
        self.increment = speed
        self.x_move = STARTING_MOVE_DISTANCE + (self.increment * MOVE_INCREMENT)



    def show_up(self):
        rand_y = random.randint(-250, 250)
        self.goto(280, rand_y)

    def run(self):
        self.forward(self.x_move)

    def faster(self):
        self.x_move += MOVE_INCREMENT

