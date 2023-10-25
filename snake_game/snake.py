from turtle import Turtle
S_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE=20
UP=90
DOWN=270

LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):

        for pos in S_POSITION:

            self.add(pos)
    def add(self,pos):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(pos)
        self.segment.append((new))
    def extend(self):
        self.add(self.segment[-1].position())
    def move(self):
        for s_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[s_num - 1].xcor()
            new_y = self.segment[s_num - 1].ycor()
            self.segment[s_num].goto(new_x, new_y)
        self.head.forward(MOVE)
    def up(self):
        if self.head.heading()!=DOWN:
             self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
             self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)


