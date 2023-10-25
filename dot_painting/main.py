import random
from turtle import Turtle,Screen
import turtle as t

import colorgram
turtle=Turtle()
t.colormode(255)
screen=Screen()
colors=colorgram.extract('image.jpg', 30)
rgb_color=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new=(r,g,b)
    rgb_color.append(new)
colorss=[(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
dots=100

for dot in range(1,dots+1):
    turtle.dot(20,random.choice(colorss))
    turtle.forward(50)



    if dot%10==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)






screen.exitonclick()