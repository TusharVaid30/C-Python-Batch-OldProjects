from turtle import *
from random import randint as r , choice as c 

w = Screen()
w.tracer(0) 
w.bgcolor("black")
w.setup(1200 , 600) 
t = Turtle()
t.ht()
t.speed(0)
t.color("white")
def Building(x , y) :
    t.lt(90)
    t.fd(x)
    t.rt(90)
    t.fd(y)
    t.rt(90)
    t.fd(x)
    t.lt(90)
Start_L = -800
Start_D = -100
Ground  = 300
leng = 10000
t.pu()
t.goto(Start_L , Start_D)
t.pd()
t.begin_poly()
t.begin_fill()
dy = 0
for _ in range(leng) :
    t.fd(1)
    if _ == 0 :
        dis = r(0 , 100)
    if _ == dis :
        dis += r(30 , 130)
        x = r(100 , 450)
        y = r(30 , 120) + x/2.5
        dy += y
        Building(x , y)
    #w.update()
t.rt(90)
t.fd(Ground)
t.rt(90)
t.fd(dy + leng)
t.rt(90)
t.fd(Ground)

t.end_fill() 
w.register_shape( "Buildings" , t.get_poly() )

##
##
t.clear()
Builds = Turtle()

Builds.shape("Buildings")
Builds.color("white")
Builds.pu() 
Builds.setheading(90)
Builds.bk(Ground/4) 
Builds.dx = 50 
Objs = [] 
Objs.append(Builds)  

dx = 50 
def Left() :
    for _ in Objs : _.setx(_.xcor() + _.dx )
def Right() :
    for _ in Objs : _.setx(_.xcor() - _.dx )
listen() 
w.onkeypress(Left  , "a")
w.onkeypress(Right , "d")
###t.color("white")
##w.color("white")
for _ in range(5000) : w.update() 
