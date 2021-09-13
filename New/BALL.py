import pygame as pg
import math 
from random import randint as R , choice as C
pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )
def Line( Start , End ) :
  pg.draw.line( Window , ( 255 , 255 , 255 ) , ( Start[0] , Start[1] ) , ( End[0] , End[1] ) , 1 ) 
def Write( x , y , Text ) :
  Window.blit( pg.font.SysFont( None , Text_Size ).render( str(Text) , True , ( 255 , 255 , 255 ) ) , ( x , y ) ) 
def Circle( x , y , Radius , Color ) :
  pg.draw.circle( Window, Color , (int(x) , int(y)) , abs(int(Radius)) )      
def Rectangle( x , y , Width , Height , Color ) :
  pg.draw.rect( Window , Color , ( x - Width/2 , y - Height/2 , Width , Height ) )

def r( A , B ) :
    return R( A*1000 , B*1000 )/1000

class Class_Ball :
    def __init__( self ) :
        self.Radius = 20# R(1,10) 
        self.x = 500#R( self.Radius , Window_Width  - self.Radius )
        self.y = 500#R( self.Radius , Window_Height - self.Radius )
        self.dx = 0#r( -1 , 1 )
        self.dy = 0#r( -1 , 1 )
        self.Color = ( 155 , 155 , 155 )
        
    def Recoil( self ) :
        if self.x >= Window_Width  - self.Radius or self.x <= self.Radius : self.dx *= -1
        if self.y >= Window_Height - self.Radius or self.y <= self.Radius : self.dy *= -1 
    def Wall_Teleport( self ) :
        if self.x > Window_Width : self.x = 0
        if self.x < 0 : Window_Width
        if self.y > Window_Height : self.y = 0
        if self.y < 0 : Window_Height
    def Display( self ) :
        Circle( self.x , self.y , self.Radius , self.Color )
    def Move( self ) :
        self.x += self.dx
        self.y += self.dy
        
    

Tol = 250
Max_Balls = 1
Pres = 100

Color_Back = ( 128 , 128 , 128 )
Color_Front = ( 255 , 0 , 0 )

Balls = []
for _ in range(Max_Balls) : Balls.append( Class_Ball() )

def Logic() :
    for Ball in Balls :
        Ball.Recoil() 
        Ball.Move()
        #Ball.dy += Gravity 
        Ball.Display()
         
while True :
    Window.fill( ( 0 , 0 , 0 ) )
    Logic()
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            break 
    if pg.key.get_pressed()[pg.K_ESCAPE]: break 
    pg.display.flip()
pg.quit() 
