from turtle import * 
w = Screen()
w.tracer(0,0)



w.bgcolor("black")
t = Turtle()
t.ht()
t.pu()
t.color("white")
t.lt(90)
t.bk(250)
t.pd()

POS_X = -200
POS_Y = 100

DIS_X = 50
DIS_Y = 70
class Designer(Turtle):

    def design(self, homePos, scale):
        self.begin_poly() 
        self.up()
        for i in range(5):
            self.forward(64.65 * scale)
            self.down()
            self.wheel(self.position(), scale)
            #A.addcomponent("A" , self.get_poly()) 
            self.up()
            self.backward(64.65 * scale)
            self.right(72)
        self.up()
        self.goto(homePos)
        self.right(36)
        self.forward(24.5 * scale)
        self.right(198)
        self.down()
        A.addcomponent(self.get_poly() , "white")
        self.centerpiece(46 * scale, 143.4, scale)

    def wheel(self, initpos, scale):
        self.right(54)
        for i in range(4):
            self.pentpiece(initpos, scale)
        self.down()
        self.left(36)
        for i in range(5):
            self.tripiece(initpos, scale)
        self.left(36)
        for i in range(5):
            self.down()
            self.right(72)
            self.forward(28 * scale)
            self.up()
            self.backward(28 * scale)
        self.left(54)

    def tripiece(self, initpos, scale):
        oldh = self.heading()
        self.down()
        self.backward(2.5 * scale)
        self.tripolyr(31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.down()
        self.backward(2.5 * scale)
        self.tripolyl(31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)

    def pentpiece(self, initpos, scale):
        oldh = self.heading()
        self.up()
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pentr(18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pentl(18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)

    def pentl(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.left(ang)
        self.pentl(side - (.38 * scale), ang, scale)

    def pentr(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.right(ang)
        self.pentr(side - (.38 * scale), ang, scale)

    def tripolyr(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.right(111)
        self.forward(side / 1.78)
        self.right(111)
        self.forward(side / 1.3)
        self.right(146)
        self.tripolyr(side * .75, scale)

    def tripolyl(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.left(111)
        self.forward(side / 1.78)
        self.left(111)
        self.forward(side / 1.3)
        self.left(146)
        self.tripolyl(side * .75, scale)

    def centerpiece(self, s, a, scale):
        self.forward(s); self.left(a)
        if s < (7.5 * scale):
            return
        self.centerpiece(s - (1.2 * scale), a, scale)


class Slider(Turtle):
    def __init__(self, x, y , st ):
        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5,1)
        
        self.color("white")

        self.pu()
        self.goto(POS_X + x,POS_Y)
        self.pd()
        self.sety(y*2 + POS_Y)
        self.write(st , align = "center" )
        self.pu()
        self.sety(y + POS_Y)
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(POS_Y,min(y,2*DIS_Y + POS_Y)))
        updoot()
        w.update()
def updoot():
    AAAA = A_mod.ycor()
    BBBB = B_mod.ycor() 
    T = [ AAAA , BBBB ]
    print(T)
    t.design(0,1)
    t.clear()
    w.update()
t = Designer() 
A_mod = Slider(-2*DIS_X , DIS_Y , "Angle" )
B_mod = Slider(-  DIS_X , DIS_Y , "Scale"   )
while True : updoot() 
