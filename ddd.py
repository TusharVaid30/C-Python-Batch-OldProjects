from turtle import *
from turtle import Vec2D as Vec
from random import *
w = Screen()
w.bgcolor("black")
w.tracer(0)
w.screensize(10000,10000)
t = Turtle() ; t.ht() ; t.pu()
fps = 0 ; refrate = 50
f = 0 
#G = 80
def make_planet_shape(Name , LightColor , DarkColor) :
    
    t.reset() ; t.fd(6) ; t.lt(90)

    t.begin_poly() ; t.circle(6, 180) ; t.end_poly()
    m1 = t.get_poly()

    t.begin_poly() ; t.circle(6, 180) ; t.end_poly()
    m2 = t.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,LightColor)
    planetshape.addcomponent(m2,DarkColor)
    w.register_shape(Name, planetshape)
class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        while True:
            self.t += self.dt
            for p in self.planets:
                p.step()



class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        self.f = f
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                self.f += randint(-100,100)/100
                v = planet.pos()-self.pos()
                G = self.f 
                a += (G*planet.m/abs(v)**3)*v
                
        return a
    def step(self):
        global fps
        fps += 1
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        #5self.color(0,1,2) ;self.xcor() , self.ycor() , 122) 
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a
    
        if fps%refrate == 0 : w.update()

## create compound yellow/blue turtleshape for planets

def main():
    gs = GravSys()    
    COLORS = ( "red" , "magenta" , "white" , "green", "blue" , "chocolate" ,
               "purple" , "orange" , "yellow" , "violet" , "lightblue"  )
    Sun = Star(12500, Vec(0,0), Vec(0,0), gs, "circle")
    Sun.color("gold")
    Sun.shapesize(1.6)
    Sun.pd()
    

    ___ = 0
    PLANETS   = [ ]
    for _ in range(250) :
        PLANETS.append(Turtle())
    for __ in PLANETS :
        col1 = choice(COLORS)
        col2 = choice(COLORS)
        ___ += 1
        make_planet_shape("Planet"+str(___), col1 , col2)
        x = randint(-500 , 500)
        y = randint(-500 , 500)
        vx = randint(-100 , 100)
        vy = randint(-100 , 100)
        m = randint(10000 , 50000)
        __ = Star(m, Vec(x,y), Vec(vx,vy), gs, "Planet"+str(___))
        __.pencolor(col1)
        __.shapesize(randint(5,15)/10)

##    make_planet_shape("mer" , "red" , "orange")
##    mer = Star(50000, Vec(-100,0), Vec(0,20), gs, "mer")
##    mer.pencolor("red")
##    mer.shapesize(0.8)
##    make_planet_shape("mer1" , "red" , "orange")
##    mer1 = Star(50000, Vec(100,0), Vec(0,-20), gs, "mer1")
##    mer1.pencolor("red")
##    mer1.shapesize(0.8)

    
    #for PLANET   in PLANETS   : PLANET.pu()
    #for SATALITE in SATALITES : SATALITE.pd()
    gs.init()
    gs.start()
    return "Done!"

main()
##if __name__ == '__main__':
##    main()
##    mainloop()
