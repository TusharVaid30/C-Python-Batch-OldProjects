from turtle import *
from random import *
w = Screen()
w.tracer(0)
w.bgcolor("black")
xwall = 500
ywall = xwall
safe = xwall/10
parti = []
def make_parti(max_parti = 50) :
    for _ in range(max_parti) :
        parti.append(Turtle())
    for _ in parti :
        _.color("white")
        _.shape("circle")
        _.shapesize(randint(10,500)/1000)
        _.pu()
        _.goto(randint(-xwall,xwall),randint(-ywall,ywall))
        _.seth(90)
        _.angl = 0
        _.shhh = 0
def move_parti() :
    for _ in parti :
        hid = randint(1,2000)
        if _.heading() not in range(-45,225) : _.seth(90)
        if hid == 1  or (_.shhh > 5 and not _.isvisible()):
            if _.isvisible() : _.ht() ; _.shhh = 0
            else : _.st() ;
        mv = randint(1,5)/10
        if (not _.isvisible()) : _.shhh += mv
        _.angl = randint(-10,10)
        _.fd(mv)
        _.rt(_.angl)
        if _.xcor() >  xwall + safe : _.setx(-xwall - safe)
        if _.xcor() < -xwall - safe : _.setx( xwall + safe)
        if _.ycor() >  xwall + safe : _.sety(-ywall - safe)
        if _.ycor() < -ywall - safe : _.sety( ywall + safe)

#while True :
#$    move_parti()
