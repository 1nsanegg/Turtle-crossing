import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    # carManager should not inherit from Turtle, this should be manage multiple Turtle object (car)
    def __init__(self, speed):
        self.cars = []
        self.speed = speed

    # create each car and add to cars
    def create_car(self):
        # add condition to create car to make sure that the frequency is not to high
        spawn_chance = random.randint(1,6)
        if spawn_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            random_y = random.randint(-250,250)
            new_car.goto(280, random_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            move_distance = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.speed)
            car.forward(move_distance)
        self.cars = [car for car in self.cars if car.xcor() > -320]