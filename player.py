from turtle import Turtle

from constants import STARTING_POSITION, MOVE_DISTANCE, FINISH_LINE_Y, STARTING_ANGLE


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.set_properties()

    def set_properties(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(STARTING_ANGLE)
        self.go_to_start()

    def move(self):
        if self.has_crossed_finish_line():
            self.go_to_start()
        else:
            self.forward(MOVE_DISTANCE)

    def has_crossed_finish_line(self):
        return self.ycor() == FINISH_LINE_Y

    def go_to_start(self):
        self.setpos(STARTING_POSITION)
