import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager

from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
sleep_time = 0.1
level = 0
game_is_on = True
scoreboard.update_scoreboard()
while game_is_on:

    car_manager.create_car()
    car_manager.move_car()

    # detect Crash with car

    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()
    # detect if turtle made it to the other side.

    if player.is_at_finish_line() == True:
        print("you made it")
        scoreboard.level_up()
        car_manager.level_up()
        scoreboard.update_scoreboard()
        player.reset_player()
    time.sleep(sleep_time)
    screen.update()
    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")
screen.exitonclick()