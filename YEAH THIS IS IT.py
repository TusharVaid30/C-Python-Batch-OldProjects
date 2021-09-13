from turtle import * 
w = Screen()
w.tracer(0,0)    #screen.delay(0)
#w.delay(0)
#w.setworldcoordinates(-1, -0.3, 3, 1.3)
w.bgcolor("black")
t = Turtle()

A = 1
B = 1
C = 1

POS_Y = -100
POS_X = 100

DIS_X = 70
LOC_Y = -100

class ColorTurtle(Turtle):
    def __init__(self, x, y , st ):
        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5,1)
        
        self.color("white")

        self.pu()
        self.goto(x,LOC_Y)
        self.pd()
        self.sety(y*2 + LOC_Y)
        self.write(st)
        self.pu()
        self.sety(y + LOC_Y)
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(LOC_Y,min(y,2*POS_Y + LOC_Y)))
        updoot()
        w.update()

def updoot():
    global A , B , C
    A = A_mod.ycor()
    B = B_mod.ycor()
    C = C_mod.ycor()
    T = [ A , B , C ]
    print(T)
    w.update()
def main():
    
    global A_mod , B_mod , C_mod
    A_mod = ColorTurtle(POS_X - DIS_X , POS_Y , "A" )
    B_mod = ColorTurtle(POS_X         , POS_Y , "B" )
    C_mod = ColorTurtle(POS_X + DIS_X , POS_Y , "C" )
    updoot()


main()
