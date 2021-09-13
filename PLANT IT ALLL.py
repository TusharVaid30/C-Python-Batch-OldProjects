from random import *
from turtle import *
from tkinter import *
#from multiprocessing import Process
#processes = []
SEE = False
dismod = (2/3,3/4,3/5,7/8)       ; c = 2      ; d = 5
a = 15   ; b = 40  ; minpix = 10 ; wmod = 3/5
ground = - 225
seeds = 0
rightmost = 0
leftmost = 0
listen()
w = Screen()
w.tracer(0,0)
w.bgcolor("black")
zulu = 0
gnd = Turtle() ; seee = Turtle() ; seee.color("white") ; seee.ht()
gnd.pu()
gnd.ht()
gnd.color("white")
gnd.begin_fill()
gnd.goto(-1000 , ground)
gnd.towards( 0 , ground )
gnd.pd()
for _ in range(2000) :
    gnd.fd(1) ; gnd.lt(randint(-20,21)/3)
    if _%5 == 0 : gnd.setheading(0)

gnd.goto(1000  , ground - 200 ) 
gnd.goto(-1000 , ground - 200 )
gnd.goto(-1000 , ground )
gnd.end_fill()
seee.pu()
seee.goto( 0 , 100)
seee.write("PLANT")
T = []
for _ in range (100) : T.append(Turtle()) ; seeds += 1 

def see() :
    seee.clear()
    seee.write(f"Seeds : {seeds}\nDistance : {int(rightmost - leftmost)}") 
def make_t(t) :
    t.ht()
    t.color("white")
    t.pu()
    t.dy = 0
    t.setheading(randint(85,95))
    
for t in T :
    make_t(t)
    t.shape("circle")
    t.shapesize(0.5)
    t.g  = 0.05
    t.setundobuffer(0)
    t.taken = False
    t.used = False
    t.tree = False
    t.once = False 


def multitask() :
    global seeds , leftmost , rightmost
    for t in T : 
        if t.used :
            if t.taken and not t.tree :
                t.fd(1)
                if t.ycor() >= ground  :
                    t.sety(t.ycor() - t.dy)
                    t.dy += t.g
                if not t.ycor() >= ground :
                    t.tree = True
                    if t.xcor() > rightmost : rightmost = t.xcor()
                    if t.xcor() < leftmost : leftmost = t.xcor()
                    t.pd()
                    t.ht()
                    PLANT(t , 2*randint(15,40)/2 , randint(20,35) , randint(40,65)/10 )
                    
                    
                    #make_t(t)

                    t.tree = False
                    t.taken = False
                    t.once = True
                    if not t.once : seeds += 1 ; see()
                
                    

                    #process = Process(target = tree , args = ( t , 40 , 30 , 4 ) )
                    #processes.append( process )
                    #process.start() 

                
            
            
    w.update()


def dot(x , y) :
    global seeds
    for t in T :
        if not t.taken and not t.once :
            if not t.used : t.used = True ; t.st()
            t.taken = True 
            t.ht()
            seeds -= 1
            see()
            t.goto(x , y)
            t.st()
            break
    
    
def fresh() :
    global leftmost , rightmost
    leftmost = rightmost = 0 
    for t in T : t.clear()

def tree(t,x,y,s) :
    if x < minpix :
        if SEE : multitask()
        return
    else :
        zzz = s*wmod  ; zz = y*0.98 ; z  = choice(dismod)*x
        t.width(s)    ; t.fd(x) 
        tree(t,z*1.01,zz,zzz)
        lll = choice((1,-1))
        t.lt(lll*y)
        tree(t,z,zz,zzz) 
        t.rt(lll*2*y)
        tree(t,z,zz,zzz) 
        #if z < minpix : multitask()
        t.lt(lll*y) ; t.bk(x)     

def root(t,x,y,w)   :
    t.width(w)
    s = w*wmod
    i = int(x)
    z = x*choice(dismod)
    zz = choice((z,z/10))
    aaa = choice((1,2))
    if aaa == 1 : zzz = z ; zzzz = zz
    else : zzz = zz ; zzzz = z
    yy = y - 0.1
    angs = []
    diss = []
    for _ in range(i) : angs.append(randint(-10,10)) ; diss.append(randint(9,10)/10)
    for _ in range(i) : t.fd(diss[_]) ; t.lt(angs[_]) 
    t.lt(y)
    #t.fd(z)
    #t.bk(z)
    if x > minpix : root(t , zzz,yy,s)
    t.rt(2*y)
    if x > minpix : root(t , zzzz,yy,s)
    t.lt(y)
    for _ in range(i) : t.rt(angs[i - _ - 1]) ; t.bk(diss[i - _ - 1])

def PLANT(p1 , p2 , p3 , p4 ) :
    global zulu
    Temp_x = p1.xcor()
    Temp_y = p1.ycor() 
    p1.begin_poly()
    tree(p1 , p2 , p3 , p4)
    Treah = p1.get_poly()
    p1.setheading(-90)
    p1.color("black")
    p1.begin_poly()
    root(p1 , p2 , p3 , p4)
    Treag = p1.get_poly()
    Treaa = Shape("compound")
    Treaa.addcomponent(Treah , "white")
    Treaa.addcomponent(Treag , "red")
    w.register_shape("Tree" + str(zulu) , Treaa)
    p1.shape("Tree" + str(zulu))
    p1.setheading(90)
    p1.goto(0,-110)
    #p1.setx(Temp_x)
    #p1.sety(p1.ycor() + Temp_y)
    p1.clear()
    p1.st()
    zulu += 1 
#x = -250
#y = 100
#for _ in range(10) : dot(x , y) ; x+= 2*randint(25,50)
x = 0
while True :
    x += 1
    onscreenclick(dot)
    if x%randint(1,100) == 0 : x = 0 ; dot(randint(-500,500) , 300 )
    #if x%5000 == 0 : fresh()
    onkey(fresh , "w" )
    #see()
    multitask() 
    
