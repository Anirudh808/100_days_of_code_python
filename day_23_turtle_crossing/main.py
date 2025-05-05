import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 4:
        car_manager.create_car()
    car_manager.move_cars()

    # Detect when player hits car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if the player finishes the race
    if player.ycor() >= FINISH_LINE_Y:
        print("player finished the race")
        player.restart()
        scoreboard.increase_level()
        car_manager.level_up()


screen.exitonclick()
