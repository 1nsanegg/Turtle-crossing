from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280,280)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over, you score is {self.level}", False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_level()