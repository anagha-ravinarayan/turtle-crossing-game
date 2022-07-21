from turtle import Turtle
import random

from constants import COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT, SCREEN_WIDTH, CAR_Y_LIMIT, CAR_ANGLE


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            random_position = (SCREEN_WIDTH / 2, random.randint(-CAR_Y_LIMIT, CAR_Y_LIMIT))
            random_color = random.choice(COLORS)

            car = Turtle(shape="square")
            car.penup()
            car.setheading(CAR_ANGLE)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random_color)
            car.setpos(random_position)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT

    def get_cars(self):
        return self.cars
