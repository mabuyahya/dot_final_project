"""
turtle
"""
"""turtle is a standard Python library for drawing shapes and patterns using a turtle graphics system.
It provides a simple way to create graphics and is often used for educational purposes."""
"""The turtle module allows you to control a turtle that moves around the screen, drawing as it goes."""
"""You can control the turtle's movement, color, and speed to create various shapes and designs."""

import turtle

t = turtle.Turtle()

t.speed(0.1)
t.color('blue')
t.pensize(1.4)

t.color('green')
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.forward(300)
    else:
        t.forward(100)
    t.right(90)
t.end_fill()
t.left(90)
t.color('white')
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.forward(100)
    else:
        t.forward(300)
    t.right(90)
t.forward(200)
t.end_fill()
t.right(90)
t.color('black')
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.forward(300)
    else:
        t.forward(100)
    t.right(90)

t.end_fill()
t.color('red')
t.begin_fill()
t.left(180 + 45)
t.forward(235)
t.left(96)
t.forward(215)
t.end_fill()
turtle.done()
