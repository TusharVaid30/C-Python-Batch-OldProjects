import turtle
from random import choice as c
t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)
t.lt(90)
t.pu()
t.goto(0,-300)
t.pd()
t.ht()
z = 200
l = 5
b = 30
w.tracer(0)
def tree(x,y=30):
    #if y >75 :
     #   y = 30
    w.update()
    h=(3*x/2,2*x/3)
    a = c(h)
    t.fd(x)
    t.rt(y)
    if x < z and x > l:
        tree(a)
    t.lt(2*y)
    if x < z and x > l:
        tree(a)
    t.rt(y)
    t.bk(x)
tree(10,45)
w.update()
