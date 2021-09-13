from turtle import *
from random import randint as r , choice as c
from math import cos , sin , e as E , pi as PI
def mod( x ) :
    if x < 0 : x*= -1
    return x 
Wall = 600
Floor = 300
w = Screen()
w.tracer(0)
w.setup( 2*Wall , 2*Floor ) 
w.bgcolor("black")
ITheta = PI
IDTheta = 0.25#E/10#0.25
DTheta = IDTheta
Theta = ITheta
Radius = 15
colormode(255)
r = 0
g = 0
b = 100
dr = Theta*40/255
dg = 0
db = 0




c = 0
d = 0
e = 0
z = -1
zz = 3
t = []
for _ in range(zz) : t.append( Turtle() )
for tt in t :
    z += 1 
    tt.ht()
    tt.pu() 
    tt.setx( Radius*16*( sin(ITheta)**3 ) )
    tt.sety( Radius*(13*cos(ITheta) - 5*cos(2*ITheta) - 2*cos(3*ITheta) - cos(4*ITheta)) )
    tt.pd()
while True :

    if c % int(ITheta/DTheta) == 0 :

        if d%2 == 1 :
            pass # print("Up")
        else :
            c = 0
            if e == z : e = 0 
            else : e += 1
            t[e].clear() 
        d += 1
    
    r += dr   
    g += dg
    b += db
    if r >= 255 or r <= 0 : dr *= -1
    if g >= 255 or g <= 0 : dg *= -1
    if b >= 255 or b <= 0 : db *= -1
    t[e].color( int(r) , int(g) , int(b) ) 
    t[e].setx( Radius*16*( sin(Theta)**3 ) )
    t[e].sety( Radius*(13*cos(Theta) - 5*cos(2*Theta) - 2*cos(3*Theta) - cos(4*Theta)) )
    Theta += DTheta
    c += 1 
    w.update()



















    
