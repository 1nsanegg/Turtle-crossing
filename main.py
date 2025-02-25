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
level = 0

screen.listen()
screen.onkey(turtle.move, "Up")
game_loop = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if game_loop == 6:
        new_car = CarManager(level)
        cars.append(new_car)
        game_loop = 0
    for car in cars:
        if turtle.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()
        car.run()
    if level < turtle.refresh_time:
        level += 1
        scoreboard.increase_level()
        for car in cars:
            car.faster()
    game_loop +=1


screen.exitonclick()
