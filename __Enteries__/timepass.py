from turtle import *

w = Screen()
w.bgcolor("black")
#w.tracer(0)

t = Turtle()
t.color("white")
t.speed(0)

for _ in range(1,360) :
    t.fd(2*_)
    t.rt(2*_)
    #w.update()
