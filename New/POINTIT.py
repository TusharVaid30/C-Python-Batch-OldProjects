import pygame as pg
import math 
from random import randint as R , choice as C 
class Point :
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , abs(int(self.radius)) , abs(int(self.width)) )

    def Move( self ) :
        self.x += self.dx
        self.y += self.dy 
pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )


Radius = 10
Dis = Radius*2
Tol = 250

Number_X = int(Window_Width/(2*Dis))
Number_Y = int(Window_Height/(2*Dis))
Pixels = []
for _ in range( Number_Y ) : Pixels.append( [] )
for _ in Pixels :
    for __ in range( Number_X ) : _.append( Point() )

Color_Back = ( 128 , 128 , 128 ) 
Temp_y = Dis
for Y in Pixels :
    Temp_x = Dis
    for X in Y :
        X.x = Temp_x
        X.y = Temp_y
        X.color = Color_Back 
        X.width = X.radius = Radius
        Temp_x += 2*Dis
        X.changed = True
        X.dx = R(3,10)*C( (-1,1) )/2
        X.dy = R(3,10)*C( (-1,1) )/5
        X.ddy = 0.1 

    Temp_y += 2*Dis
def Mouse() :
    Mouse_x , Mouse_y = pg.mouse.get_pos()
    for Y in Pixels :
        for X in Y :
            c1 = c2 = False
            if Mouse_x > X.x - Tol and Mouse_x < X.x + Tol  :
                TOL = Tol*math.sin( math.acos( (Mouse_x - X.x)/Tol) )
                if Mouse_y > X.y - TOL :
                    c1 = True
                if Mouse_y < X.y + TOL :
                    c2 = True 
            if c1 and c2 :
                R = (( Mouse_x - X.x )**2 + ( Mouse_y - X.y )**2 )**0.5
                X.changed = True 
                X.color = ( abs(255*(math.cos(R/Tol)**2)) , abs(0*(math.cos(R/Tol)**4))  , abs(0*math.cos(R/Tol)) )

            else :
                if X.color != Color_Back :
                    X.changed = True 
                    X.color = Color_Back
                X.width = X.radius

def Teleport( X ) :
    if X.x > Window_Width : X.x = 0
    if X.x < 0 : Window_Width
    if X.y > Window_Height : X.y = 0
    if X.y < 0 : Window_Height

    
Gameover = False 
while not Gameover :
    Window.fill( ( 0 , 0 , 0 ) )
    #pg.time.Clock().tick(60)
    for Y in Pixels :
        for X in Y :
            X.Move()
            X.dy += X.ddy 
            if X.x >= Window_Width or X.x <= 0 : X.dx *= -0.98
            if X.y >= Window_Height or X.y <= 0 : X.dy *= -0.98
            #if X.changed :
            X.Display()
            X.changed = False 
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            Gameover = True
    Mouse() 
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
pg.quit() 
