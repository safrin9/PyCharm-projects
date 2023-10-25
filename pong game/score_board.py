from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()

    def update(self):
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("courier", 24, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("courier", 24, "normal"))
    def l_score_point(self):
        self.clear()
        self.l_score+=1
        self.update()
    def r_score_point(self):
        self.clear()
        self.r_score+=1
        self.update()