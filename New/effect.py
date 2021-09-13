import pygame as pg
from random import randint as r , choice as c
import math
def cos( x ) : return math.cos( x*math.pi/180 ) 
def sin( x ) : return math.sin( x*math.pi/180 ) 
Window_Width  =  800  
Window_Height =  300
Window = pg.display.set_mode((Window_Width, Window_Height))

pg.init()
class Particle :
    def __init__( self , x , y , dx , dy , size , color , dsize , theta ) :
        self.x  = x
        self.y  = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color
        self.dsize = dsize
        self.theta = theta
        self.r = 0 
    def Move( self ) :
        self.x += self.dx
        self.y += self.dy
    def DSize( self ) :
        self.size -= self.dsize 
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , int(self.size) )


X = Window_Width/2
Y = Window_Height/2 
Flow = []
Lemp = True 

def Boom() :
    global Lemp
    Lemp = False 
    Num = r(5,15) 
    for _ in range(Num) : 
        Flow.append( Particle ( X , Y ,
                                0 , 0 ,
                                5 ,
                                ( 255 , 255 , 255 ) ,
                                0.01 ,
                                _*( 360/Num) ) )


Radius = 100 
Gameover = False 
while not Gameover :
    Window.fill( ( 0 , 0 , 0 ) )
    for event in pg.event.get() :
        if event.type == pg.QUIT : Gameover = True
    
    if pg.key.get_pressed()[pg.K_SPACE] :
        if Lemp : Boom()
    else : Lemp = True
    if pg.key.get_pressed()[pg.K_ESCAPE] : break

    for _ in Flow :
        _.theta += 1/10
        _.r += 0.5
        Temp_x = _.x
        Temp_y = _.y
        _.x = X + cos(_.theta)*_.r  
        _.y = Y + sin(_.theta)*_.r
        _.DSize() 
    
        _.Display()
        if _.size <= 0 : Flow.remove(_) 
    pg.display.flip()
    
pg.quit()
quit()
    
