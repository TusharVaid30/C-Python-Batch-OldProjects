from turtle import *

w = Screen()
w.bgcolor("black")
w.tracer(0)
t = Turtle()
t.color("white")

t.begin_poly()
t.begin_fill()
t.fd(20)
t.lt(120)
t.fd(40)
t.lt(120)
t.fd(40)
t.lt(120)
t.fd(20)
t.end_fill()
Arrow = t.get_poly()
w.register_shape("ARR" , Arrow)
t.clear()
t.pu() 
t.shape("ARR")
t.lt(90)
#w.tracer(1)
for _ in range(90) : t.shapesize(t.shapesize()[0] - 0.01) ; t.bk(0.5) ; w.update() 
laft = - 150
dis = 75
Obj = []
while laft <= 150 :
    Obj.append(laft)
    laft += dis
Box = []
colors = [ "pink" , "yellow" , "black" , "red" , "purple" ] 
ono = 0 
for _ in range ( len(Obj)) : Box.append(Turtle()) 
for _ in Box :
    _.color(colors[ono])
    _.shape("square")
    _.shapesize(3)
    _.pu()
    _.goto( Obj[ono] , 50 )
    ono += 1 
ooo = 2
swift = False
dx = 0.1
t.dx = dx
t.aa = 0.01
def L() :
    global ooo , swift
    swift = True 
    if ooo > 0 : ooo -= 1 #; t.dx = dx 
def R() :
    global ooo , swift
    swift = True 
    if ooo < len(Obj) - 1 : ooo += 1 ;# t.dx = dx
def Moo() :
    global swift
    if t.dx > 2 : t.dx = dx
    if int(t.xcor()) > Obj[ooo] : t.setx(t.xcor() - t.dx)  ; t.dx += t.aa 
    elif int(t.xcor()) < Obj[ooo] : t.setx(t.xcor() + t.dx) ; t.dx += t.aa
    else : t.dx = 0 ; swift = False ; t.dx = dx
def Noo():
    if int(t.xcor()) == Obj[ooo] : w.bgcolor(colors[ooo]) 
listen()

onkey(L , "a")
onkey(R , "d")
onkey(Noo , " ")
while True :
    if swift : Moo()
    w.update() 




