FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level {self.level}", align="center", font=(FONT))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=(FONT))




    def level_up(self):
        self.level += 1
        self.update_scoreboard()

