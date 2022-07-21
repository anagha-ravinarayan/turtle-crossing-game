import time
from turtle import Screen

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_SLEEP, PLAYER_CAR_DISTANCE
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(GAME_SLEEP)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect if player has crossed finish line
    if player.has_crossed_finish_line():
        scoreboard.increment_level()
        player.go_to_start()
        car_manager.increase_car_speed()

    # Detect collision with any car
    cars = car_manager.get_cars()
    for car in cars:
        if player.distance(car) < PLAYER_CAR_DISTANCE:
            scoreboard.show_game_over()
            game_is_on = False

screen.exitonclick()
