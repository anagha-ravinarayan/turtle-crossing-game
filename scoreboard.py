from turtle import Turtle

from constants import FONT, SCOREBOARD_POSITION, LEVEL_ALIGNMENT, GAME_OVER_ALIGNMENT, GAME_OVER_FONT, GAME_OVER_POSITION


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.set_properties()
        self.show_level()

    def set_properties(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setpos(SCOREBOARD_POSITION)

    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=LEVEL_ALIGNMENT, font=FONT)

    def increment_level(self):
        self.level += 1
        self.show_level()

    def show_game_over(self):
        self.setpos(GAME_OVER_POSITION)
        self.write(arg="GAME OVER", align=GAME_OVER_ALIGNMENT, font=GAME_OVER_FONT)
