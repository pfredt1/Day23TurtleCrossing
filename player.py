STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor()
        new_y += MOVE_DISTANCE
        if self.ycor() < 280:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor()
        new_y -= MOVE_DISTANCE
        if self.ycor() > -280:
            self.goto(self.xcor(), new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False

