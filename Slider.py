from turtle import * 
w = Screen()
#w.tracer(0,0)
w.bgcolor("black")
w.delay(0)

POS_X = 0
POS_Y = 10

DIS_Y = 70
s = 1
class Slider(Turtle):
    def __init__(self, x, y , dis , st = f"Slider {s}" ):
        global s
        s+=1
        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5,1)
        
        self.color("white")

        self.pu()
        self.goto(x , y )
        self.pd()
        self.sety(dis + POS_Y)
        self.write(st , align = "center" )
        self.pu()
        self.sety(y + POS_Y)
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(POS_Y,min(y,2*DIS_Y + POS_Y)))
        updoot()
        #w.update()
Slider( POS_X , DIS_Y , 100)
