from turtle import Turtle
ALIGN="center"
FONT=("courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"score:{self.score}", align=ALIGN, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", align=ALIGN, font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
