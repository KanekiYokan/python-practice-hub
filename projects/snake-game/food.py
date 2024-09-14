from random import randint
from turtle import Turtle

WIDTH = 1920
HEIGHT = 1080
HALF_WIDTH = int(1920/2) - 70
HALF_HEIGHT = int(1080/2) -70


class Food(Turtle):
    def __init__(self):
            super().__init__()
            self.shape("circle")
            self.penup()
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.color("red")
            self.speed(0)
            self.refresh()

    def refresh(self):
        x_random = randint(-HALF_WIDTH, HALF_WIDTH)
        y_random = randint(-HALF_HEIGHT, HALF_HEIGHT)
        self.goto(x_random, y_random)