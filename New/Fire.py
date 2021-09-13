import pygame as pg
from random import randint as r , choice as c
def mod( x ) :
    if x < 0 : x*= -1
    return x 
pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )

class Particle :
    def __init__( self , x , y , dx , dy , size , color , dsize = 0 ) :
        self.x  = x
        self.y  = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color
        self.dsize = 0 # dsize
        self.ddy = 0.7
    def Move( self ) :
        self.x += self.dx
        self.y += self.dy
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , mod(int(self.size)) )

X = Window_Width*1/2
Y = Window_Height 
Fire = []
def Make() :
    x = r(1,500)
    Fire.append( Particle( X + r(0,x)*c((-1,1)) ,
                           Y  ,
                           r(1,10)*c((1,-1))/50 ,
                           -r(1,10)/60 ,
                           r(3,10) + 10/mod((X - x)) ,
                           ( r(55 , 255)  , r(0,30) , r(0,30) , 255 ) ,
                           r(1,10) ) )

Gameover = False

while not Gameover :
    Window.fill( ( 0 , 0 , 0 ) )
    for event in pg.event.get() :
        if event.type == pg.QUIT : Gameover = True
    #if len(Fire) < 200 :
    for _ in range(50) : Make() 
    for Flame in Fire :
        Flame.Move()
        Flame.dy -= Flame.ddy
        Flame.ddy += 0.0005 
        Flame.dx += r(1,10)*0.09*c((-1,1))
        #if Flame.x >  X - x and Flame.x < X + x  :
        Flame.dsize -= 0.015/(1+mod(X-Flame.x))
        Flame.size -= Flame.dsize
        Flame.dsize += 0.01
        __ = r(0,5) 
        for _ in range(__) :  
            Flame.x += r( - 10 , 10 )/20
            Flame.y += r( - 10 , 10 )/20
            Flame.dsize += r( -6 , 7 )/2000
        if Flame.x < 0 or Flame.x > Window_Width or Flame.y < 0 or Flame.y > Window_Height or Flame.size <= 0 : Fire.remove(Flame) 
        Flame.Display()
    
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
    
pg.quit()

    
