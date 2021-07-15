from turtle import Turtle

MOVE_FORWARDS = 20


class Snake:
    def __init__(self):
        self.snake = []

        for i in range(3):
            new_body = Turtle(shape="square")
            new_body.color("white")
            new_body.penup()
            new_body.goto(-i * 20, 0)
            self.snake.append(new_body)
            
        self.head = self.snake[0]

    def add_segment(self):
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(self.snake[len(self.snake) - 1].xcor(), self.snake[len(self.snake) - 1].ycor())
        self.snake.append(new_body)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()

            self.snake[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_FORWARDS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
