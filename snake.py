from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def add_square(self, position):
        tim = Turtle("square")
        tim.color("#FFD82C")
        tim.penup()
        tim.goto(position)
        self.squares.append(tim)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def reset(self):
        for seg in self.squares:
            seg.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def move(self):
        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


