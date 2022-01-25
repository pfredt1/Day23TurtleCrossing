import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randrange(1,7)
        if random_chance == 3:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(250, random.randrange(-280,280))

            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
