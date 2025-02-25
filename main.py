import random
import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager(speed=0)
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create and move car
    car_manager.create_car()
    car_manager.move_car()

    # check the Player hit car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    # check if the player has reached the other side
    if player.has_reached_other_side():
        player.level_up()
        car_manager.speed += 1
        scoreboard.increase_level()

screen.exitonclick()
