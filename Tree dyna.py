from turtle import * 
w = Screen()
w.tracer(0,0)    #screen.delay(0)
#w.delay(0)
#w.setworldcoordinates(-1, -0.3, 3, 1.3)
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
    global min_mod , ang_mod , dis_mod , wid_mod , dis_srt , ang_srt , wid_srt
    min_mod = A_mod.ycor() * 0.1
    
    ang_mod = (170 - B_mod.ycor())*0.03 
    dis_mod = C_mod.ycor() * 0.003
    wid_mod = D_mod.ycor() * 0.003
    dis_srt = E_mod.ycor() 
    ang_srt = F_mod.ycor() * 0.2
    wid_srt = G_mod.ycor() * 0.09
    #T = [ wid_mod ] # min_mod , ang_mod , dis_mod ]
    #print(T)
    t.clear()
    tree( dis_srt , ang_srt , wid_srt ) 
    w.update()


def tree(x , y , w ) :
    t.width(w)
    t.fd(x)
    t.lt(y)
    if x > min_mod : tree(x*dis_mod , y + ang_mod , w*wid_mod) 
    t.rt(2*y)
    if x > min_mod : tree(x*dis_mod , y + ang_mod , w*wid_mod) #.fd(x*B) ; t.bk(x*B)
    t.lt(y)
    t.bk(x)
def Slider_Setup():
    
    global A_mod , B_mod , C_mod , D_mod , E_mod , F_mod , G_mod
    A_mod = Slider(-2*DIS_X , DIS_Y , "Min Pix" )
    B_mod = Slider(-  DIS_X , DIS_Y , "Split"   )
    C_mod = Slider(    0    , DIS_Y , "Length"  )
    D_mod = Slider(   DIS_X , DIS_Y , "Branch"  )
    E_mod = Slider( 2*DIS_X , DIS_Y , "Size"    )
    F_mod = Slider( 3*DIS_X , DIS_Y , "Angle"   )
    G_mod = Slider( 4*DIS_X , DIS_Y , "Width"   )



Slider_Setup()
while True : updoot()
