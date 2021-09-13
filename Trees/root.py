import time
from turtle import *
from random import *
dis    = 100      ; dismod = (2/3,3/4,3/5,7/8)       ; c = 2      ; d = 5
ang    = 45       ; a = 15   ; b = 45  ; minpix = 10 ; siz = 10   ; wmod = 3/5
w = Screen()      ; w.bgcolor("white") ; w.tracer(0) ; w.setup(800, 1000, 600, 0)
t = Turtle()      ; t.color  ("black") ; t.lt(90)    ; t.speed(0) ; 
t.pu()            ; t.bk(305)          ; t.pd()      ; t.ht()     ;
def root(x,y,w)   :
    t.width(w)
    s = w*wmod
    i = int(x)
    z = x*choice(dismod)
    zz = choice((z,z/4))
    aaa = choice((1,2))
    if aaa == 1 : zzz = z ; zzzz = zz
    else : zzz = zz ; zzzz = z
    yy = y - 0.1
    angs = []
    for _ in range(i) : angs.append(randint(-1,1))
    for _ in range(i) : t.fd(1) ; t.lt(angs[_]) 
    t.lt(y)
    #t.fd(z)
    #t.bk(z)
    if x > minpix : root(zzz,yy,s)
    t.rt(2*y)
    if x > minpix : root(zzzz,yy,s)
    t.lt(y)
    for _ in range(i) : t.rt(angs[i - _ - 1]) ; t.bk(1)
    
while True :
    root(200 , 30 , 20) 
    
    w.update()
    t.clear()
