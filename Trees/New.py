import time
from turtle import *
from random import *
dis    = 100      ; dismod = (2/3,3/4,3/5,7/8)       ; c = 2      ; d = 5
ang    = 45       ; a = 15   ; b = 45  ; minpix = 15 ; siz = 10   ; wmod = 3/5
w = Screen()      ; w.bgcolor("black") ; w.tracer(0) ; w.setup(800, 1000, 600, 0)
t = Turtle()      ; t.color  ("white") ; t.lt(90)    ; t.speed(0) ; 
t.pu()            ; t.bk(305)          ; t.pd()      ; t.ht()     ;
def tree(x,y,s)   :
    zzz = s*wmod  ; zz = randint(a,b)  ; z  = choice(dismod)*x  
    t.width(s)    ; t.fd(x) 
    if z > minpix : tree(z,zz,zzz) #LEFT   BRANCHING
    t.rt(y) 
    if z > minpix : tree(z,zz,zzz) #RIGHT  BRANCHING
    t.lt(2*y)
    if z > minpix : tree(z,zz,zzz) #CENTER BRANCHING
    t.rt(y)
    t.bk(x)       ;     #w.update()
t.begin_poly()
tree(100 , 30 , 10)
mmmm = t.get_poly()
TREE = Shape("compound")
TREE.addcomponent(mmmm , "white")
w.register_shape("TREE" , TREE)
w.update()
w.tracer(1)
t.st()
t.shape("TREE")
while True : t.fd(1)
    
