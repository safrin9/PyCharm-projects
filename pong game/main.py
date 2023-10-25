from turtle import Turtle,Screen
from paddle import Paddle
from circle import  Circle
import time
from score_board import Score
score=Score()
paddle_r=Paddle((350,0))
paddle_l=Paddle((-350,0))
ball=Circle()
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")

screen.tracer(0)

screen.listen()
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")


screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")


is_on=True
while is_on:
    time.sleep(ball.m_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(paddle_r)<50 and ball.xcor()>340 or ball.distance(paddle_l)<50 and ball.xcor()-340340:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_p()
        score.l_score_point()
    if ball.xcor()< -380:
        ball.reset_p()
        score.r_score_point()

screen.exitonclick()