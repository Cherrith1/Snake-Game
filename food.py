from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        x_cor = randint(-250, 250)
        y_cor = randint(-250, 250)
        self.goto(x_cor, y_cor)