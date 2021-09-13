import turtle
from turtle import Turtle
from turtle import Screen

pi = 3.14159265

w= Screen();w.tracer()
w.bgcolor("black")
 
aspeed = 0
def cir(x):
    return 2*pi*x
def orbit(x,y):
    x.fd(y.m + (y.xcor()**2+y.ycor()**2)**0.5)
    x.rt(y.a + x.a)
    x.fd(1)

sun = Turtle()
sunsize = 3
sun.shape("circle")
sun.color("gold")
sun.shapesize(sunsize,sunsize)
sun.pu()
sun.speed(aspeed)
sun.goto(0,0)
sun.a = 1
sun.m = 0

earth = Turtle()
earthsize = 1
earth.shape("circle")
earth.color("blue")
earth.shapesize(earthsize,earthsize)
earth.pu()
earth.speed(aspeed)
earth.goto(175,0)
earth.setheading(90) ; earth.pu()
earth.a = 1
earth.m = 1

moon = Turtle()
moonsize = 0.5
moon.shape("circle")
moon.color("white")
moon.shapesize(moonsize,moonsize)
moon.pu()
moon.speed(aspeed)
moon.goto(200,0)
moon.setheading(90) ; moon.pu()


disearth = 175
cirearth = cir(disearth)
fdearth  = cirearth/360
rotearth = 1

dismoon = 200
cirmoon = cir(dismoon)
fdmoon  = cirmoon/360
rotmoon = 1
while True :
    #earth.undo()
    #moon.undo()
    w.update()
    orbit(earth,sun)
    #earth.write("Earth")
    #moon.write("Moon")	
	
