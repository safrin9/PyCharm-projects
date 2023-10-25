import turtle
from turtle import Turtle,Screen
import random
screen=Screen()

is_won=False
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="who will win")
print(user_bet)
y_pos=[-100,-60,-20,20,60,100]
all_turtles=[]
colors=['purple','blue','cyan','green','yellow','orange']
for turtles in range(0,6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtles])
    tim.goto(x=-230,y=y_pos[turtles])
    all_turtles.append(tim)
if user_bet:
    is_won=True
while is_won:
    for turtles in all_turtles:
        if turtles.xcor()>230:
            is_won=False
            winning_color=turtles.pencolor()
            if user_bet==winning_color:
                print("congo! you won")
            else:
                print("you lost")
        distance=random.randint(0,10)
        turtles.forward(distance)

#
#
#
# def move():
#     turn_right():
#     tim.right(10)
#

# def clear():
#     tim.clear()
#     tim.home()
#
#
# screen.listen()
# screen.onkey(key="f", fun=move)
# screen.onkey(key="b", fun=move_back)
# screen.onkey(key="l", fun=turn_left)
# screen.onkey(key="r", fun=turn_right)
# screen.onkey(key="c", fun=clear)
# tim.forward(10)
# def move_back():
#     tim.back(10)
# def turn_left():
#     tim.left(10)
# def


screen.exitonclick()