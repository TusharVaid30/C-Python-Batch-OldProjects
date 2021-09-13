from turtle import *
from turtle import Vec2D as Vec
w = Screen()
w.bgcolor("black")
w.tracer(0)
w.screensize(10000,10000)
t = Turtle() ; t.ht() ; t.pu()
fps = 0 ; refrate = 2
G = 20
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
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        global fps
        fps += 1
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a
        if fps%refrate == 0 : w.update()

## create compound yellow/blue turtleshape for planets

def main():
    gs = GravSys()    

    Sun = Star(1250000, Vec(0,0), Vec(0,-2.5), gs, "circle")
    Sun.color("gold")
    Sun.shapesize(1.6)
    Sun.pd()



    make_planet_shape("Mercury" , "chocolate" , "brown")
    Mercury = Star(1250000, Vec(-70,0), Vec(0,-195), gs, "Mercury")
    Mercury.pencolor("brown") 
    Mercury.shapesize(0.3)


    make_planet_shape("Venus" , "crimson" , "red")
    Venus = Star(1250000, Vec(-140,0), Vec(0,-195), gs, "Venus")
    Venus.pencolor("yellow") 
    Venus.shapesize(0.5)


    make_planet_shape("Earth" , "blue" , "darkblue")
    Earth = Star(1250000, Vec(160,0), Vec(0,195), gs, "Earth")
    Earth.pencolor("blue")
    Earth.shapesize(0.8)

    make_planet_shape("Moon" , "grey" , "black")
    Moon = Star(1250000, Vec(170,0), Vec(0,295), gs, "Moon")
    Moon.pencolor("white")
    Moon.shapesize(0.5)

    make_planet_shape("Mars" , "red" , "darkred")
    Mars = Star(1250000, Vec(-210,0), Vec(0,-195), gs, "Mars")
    Mars.pencolor("red")
    Mars.shapesize(0.7)



    PLANETS   = [ Mercury , Venus , Earth , Mars ]
    SATALITES = [ Moon ]
    #for PLANET   in PLANETS   : PLANET.pu()
    for SATALITE in SATALITES : SATALITE.pd()
    gs.init()
    gs.start()
    return "Done!"

main()
##if __name__ == '__main__':
##    main()
##    mainloop()
