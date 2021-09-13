import turtle
from random import randint as r
from random import choice as c

def mod(a):
    return a*4/5


t = turtle.Turtle()
p = turtle.Turtle()
p.color("white")
p.ht()
p.pu()
p.goto(0,-300)
w = turtle.Screen()
w.bgcolor("black")
t.speed(0)
t.lt(90)
t.pu()
t.goto(0,-300)
t.pd()
t.ht()
z = 15
b = 1
w.tracer(0)

def tree1(x,y=15):
    #if y >75 :
     #   y = 30

    w.update()
    a = mod(x)
    t.fd(x)
    t.rt(y)
    if x > z :
        tree1(a,y+b)
    t.lt(2*y)
    if x > z :
        tree1(a,y+b)
    t.rt(y)
    t.bk(x)
    if x<100 and x>50 :
        t.color(c1)
    elif x<50 and x>30 :
        t.color(c2)
    elif x<30  and x>10:
        t.color(c3)
    elif x<10  :
        t.color(c4)
def tree2(x,y=15):
    #if y >75 :
     #   y = 30

    w.update()
    a = mod(x)
    t.fd(x)
    t.lt(y)
    if x > z :
        tree2(a,y+b)
    t.rt(2*y)
    if x > z :
        tree2(a,y+b)
    t.lt(y)
    t.bk(x)
    if x<100 and x>50 :
        t.color(c5)
    elif x<50 and x>30 :
        t.color(c6)
    elif x<30  and x>10:
        t.color(c7)
    elif x<10  :
        t.color(c8)
colors = ("grey","pink","crimson","pink","lightblue","lightgreen","yellow")
iag = 0
p.write(0)
while True:
    #w.update()
    c1 = c(colors)
    c2 =c(colors)
    c3 = c(colors)
    c4 = c(colors)
    c5 = c(colors)
    c6 = c(colors)
    c7 = c(colors)
    c8 = c(colors)
    k = (tree1(r(50,100),r(10,30)),tree2(r(50,100),r(10,30)))
    c(k)
    p.undo()
    p.write(iag)
    if iag%3 == 0 :
        t.clear()
    iag += 1
w.update()
turtle.exitonclick()
