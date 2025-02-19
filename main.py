import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []
car_spawn_chance = 6
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

turtle = Player()
scoreboard = Scoreboard()
current_level = scoreboard.level

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    if random.randint(1, car_spawn_chance) == 1:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.run()
    if turtle.position == (0,0):
        scoreboard.increase_level()
        for car in cars:
            car.faster()