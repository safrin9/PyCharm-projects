from turtle import Turtle
class Circle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pos=10
        self.y_pos = 10
        self.m_speed=0.1

    def move(self):
        x=self.xcor()+self.x_pos
        y=self.ycor()+self.y_pos
        self.goto(x,y)
    def bounce_y(self):
        self.y_pos*=-1
        self.m_speed*=0.9

    def bounce_x(self):
        self.x_pos *= -1
        self.m_speed *= 0.9
    def reset_p(self):
        self.goto(0,0)
        self.m_speed=0.1
        self.bounce_x()