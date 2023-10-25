import time
from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from score_board import Score
snake=Snake()
food=Food()
score=Score()

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_on=True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<17:

        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        is_on=False
        score.game_over()
    for seg in snake.segment:
        if seg==snake.head:
            pass
        elif snake.head.distance(seg)<10:
            is_on=False
            score.game_over()



#
# tim=Turtle("square")
# tim.goto(x=-40,y=0)
# tim.color("white")
#
#
# tim_2=Turtle("square")
# tim_2.goto(x=-20,y=0)
# tim_2.color("white")
#
#
# tim_3=Turtle("square")
# tim_3.goto(x=0,y=0)
# tim_3.color("white")

screen.exitonclick()