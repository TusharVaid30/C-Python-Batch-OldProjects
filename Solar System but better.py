from turtle import *
#--------------------------------
pi = 3.14159265358979323
sunsize = 3
earthsize= 1
moonsize = 0.5
#--------------------------------

#------------------------------------------------------------------
w=Screen();w.tracer(0);w.setup(800,600)
w.bgcolor("black")
#------------------------------------------------------------------

#----
def orbit(planet,base,dummy = 0):
    if dummy == 0 :
        planet.fd(2*pi*(planet.distance(base))/3600)
        planet.lt(0.11)
        planet.fd(2*pi*(planet.distance(sun))/3600)
        planet.lt(0.1)
    elif dummy == 1 :
        planet.fd(2*pi*275/1800)
        planet.lt(0.2)
    elif dummy == 2 :
        planet.fd(2*pi*375/3600)
        planet.lt(0.1)
    
    
#=======================
#SUN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sun=Turtle();sun.shape("circle");sun.speed(0)
sun.color("yellow");sun.shapesize(sunsize,sunsize)
sun.pu();sun.goto(0,0)
#EARTH~~~~~~~~~~~~~~~~~~~~~~~~~~~~
earth=Turtle();earth.shape("circle");earth.speed(0)
earth.color("blue");earth.shapesize(earthsize,earthsize)
earth.pu();earth.goto(175,0);earth.pd()
earth.setheading(90)
#MOON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
moon=Turtle();moon.shape("circle");moon.speed(0)
moon.color("white");moon.shapesize(moonsize,moonsize)
moon.pu();moon.goto(200,0);moon.pd()
moon.setheading(90)

mars = Turtle();mars.shape("circle");mars.speed(0)
mars.pu()
mars.setx(earth.xcor() + 100)
mars.color("red")
mars.pd()
mars.setheading(90)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#=======================
flag =0
while True :
    w.update()
    orbit(earth,sun,1)
    #orbit(moon,earth,0)
    orbit(mars,sun,2)
    




exitonclick()
