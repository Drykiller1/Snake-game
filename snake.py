from turtle import *
import time
import random

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.allow_key_press = 1
        self.x_list = []
        x_start = 20
        for n in range(3):
            x = Turtle(shape="square")
            x.shapesize(stretch_wid=0.9, stretch_len=0.9, outline=0)
            x.penup()
            x_start -= 20
            x.setx(x_start)
            x.color("white")
            self.x_list.append(x)

    def add_seg(self):
        x = Turtle(shape="square")
        x.penup()
        x.color("white")
        x.shapesize(stretch_wid=0.9, stretch_len=0.9, outline=0)
        last_seg = self.x_list[-1]
        if last_seg.heading() == RIGHT:
            x.setheading(RIGHT)
        elif last_seg.heading() == UP:
            x.setheading(UP)
        elif last_seg.heading() == LEFT:
            x.setheading(LEFT)
        else:
            x.setheading(DOWN)
        self.x_list.append(x)

    def move(self):
        for seg in range(len(self.x_list) - 1, 0, -1):
            new_x = self.x_list[seg - 1].xcor()
            new_y = self.x_list[seg - 1].ycor()
            self.x_list[seg].goto(new_x, new_y)
        self.x_list[0].forward(MOVE_DISTANCE)


    def right(self):
        if self.x_list[0].heading() != LEFT and self.x_list[0].heading() != RIGHT and self.allow_key_press == 1:
            self.x_list[0].setheading(RIGHT)
            self.allow_key_press = 0
    def up(self):
        if self.x_list[0].heading() != DOWN and self.x_list[0].heading() != UP and self.allow_key_press == 1:
            self.x_list[0].setheading(UP)
            self.allow_key_press = 0
    def left(self):
        if self.x_list[0].heading() != RIGHT and self.x_list[0].heading() != LEFT and self.allow_key_press == 1:
            self.x_list[0].setheading(LEFT)
            self.allow_key_press = 0
    def down(self):
        if self.x_list[0].heading() != UP and self.x_list[0].heading() != DOWN and self.allow_key_press == 1:
            self.x_list[0].setheading(DOWN)
            self.allow_key_press = 0
