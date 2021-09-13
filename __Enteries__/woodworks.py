from turtle import *

floor = -100


w = Screen() ; w.bgcolor("black") ; w.tracer(0)
t = Turtle() ; t.color("white")

t.shape("square")
t.shapesize(5,1)

f = Turtle()
f.pu() ; f.color("white") 
f.goto(-300,floor) ; f.pd()
f.towards(0,floor)
f.fd(600)

t.dx = 0
t.dy = -0.1
while True :
    if t.ycor() - 50 > floor : t.sety(t.ycor() + t.dy)
    w.update()
