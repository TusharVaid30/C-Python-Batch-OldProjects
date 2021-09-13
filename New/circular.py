import pygame as pg
import math 
from random import randint as R , choice as C

def cos( x ) : x %= 360 ; return math.cos( x*math.pi/180 ) 
def sin( x ) : x %= 360 ; return math.sin( x*math.pi/180 )

pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )

class Point() :
    def __init__( self, x , y , radius , color ) :
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color 
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , abs(int(self.radius)) )

Father = Point( Window_Width/2 , Window_Height/2 , 10 , ( 255 , 255 , 255 ) )

Max_Points = 50
Theta  = 0
Points = []
Distance = 100
 
for _ in range(Max_Points) :
    Points.append( Point( Father.x + Distance*cos(Theta) , Father.y + Distance*sin(Theta) , 1 , ( 255 , 0 , 0 ) ) )
    Theta += 360/Max_Points 

Theta = 0

for _ in Points :
    _.Theta = Theta
    _.dTheta = 0.4
    _.Distance = Distance
    _.iDistance = Distance
    _.dDistance = 0.4
    _.ddDistance = -0.002
    _.Distance_Max = 1.5*Distance
    _.dradius = -0.01
    
    Theta += 360/Max_Points
    _.Inside = True
    
    
ZTHETA = 0 
def Logic() :

    for _ in Points :
        if _.Inside and (_.Distance >= _.iDistance + _.Distance_Max or _.Distance <= _.iDistance - _.Distance_Max):
            _.dDistance *= -1
            _.dradius *= -1.1
        if _.Inside and (_.Distance < 0 ) :
            _.Inside  = False
            _.color = ( 255 , 0 , 255 ) 
        if not _.Inside :
            _.radius -= _.dradius 
            _.dradius += 0.0005
            ZTHETA = 180
        else :
            _.radius -= _.dradius 
            ZTHETA = _.Distance - 90

        Temp_x = ( 16*( sin(_.Theta)**3) )/10 
        Temp_y = ( 13*cos(_.Theta) - 5*cos(2*_.Theta) - 2*cos(3*_.Theta) - cos(4*_.Theta) )/10 
        _.x = Father.x - _.Distance*( Temp_x*cos(ZTHETA) + Temp_y*sin(ZTHETA) )
        _.y = Father.y - _.Distance*( Temp_y*cos(ZTHETA) - Temp_x*sin(ZTHETA) )
        
        
        _.Theta += _.dTheta 
        _.Distance += _.dDistance
        _.dDistance += _.ddDistance
        if _.radius < 0 : Points.remove(_)

        
while True :
    Window.fill( ( 0 , 0 , 0 ) )
    pg.time.Clock().tick(240)
    Father.Display()
    Logic()
    ZTHETA += 0.1
    for _ in Points : _.Display() 
    for event in pg.event.get() :
        if event.type == pg.QUIT : break 
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
pg.quit() 
