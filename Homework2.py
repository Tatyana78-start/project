#--------------Задача-----------------#
'''
задача
написать программу для черепашки
'''

import turtle
star = turtle.Turtle()
star.hideturtle()
for i in range(8):
    star.forward(100)
    star.right(135)
turtle.exitonclick()


#--------------Задача-----------------#
'''
задача
написать программу для черепашки
'''
import turtle
turtle.title("Turtle Drawing")
circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("cyan")

circle.dot(20)
circle.penup()
circle.goto(0, -100)
circle.pendown()
circle.circle(100)
turtle.exitonclick()
