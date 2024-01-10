from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:
    def make_snake(self, screen):
        for pos in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(pos)
            self.segments.append(new_segment)
        screen.update()

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_index].goto(self.segments[seg_index - 1].pos())
        self.head.forward(MOVING_DISTANCE)

    def add(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def __init__(self, screen):
        self.segments = []
        self.make_snake(screen)
        self.head = self.segments[0]
