import pygame as pg
import math 

class Point :
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , abs(int(self.radius)) )#, abs(int(self.width)) )


pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )


Radius = 4
Dis = Radius*2
Tol = 50

Number_X = int(Window_Width/(2*Dis))
Number_Y = int(Window_Height/(2*Dis))
Pixels = []
for _ in range( Number_Y ) : Pixels.append( [] )
for _ in Pixels :
    for __ in range( Number_X ) : _.append( Point() )

Color_Back = ( 32 , 32 , 32 ) 
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
                X.color = ( abs(255*(math.cos(R/Tol)**2)) , abs(128*(math.cos(R/Tol)**4))  , abs(255*math.cos(R/Tol)) )
                X.radius = abs(Dis*(math.cos(R/Tol)**2))

            else :
                if X.color != Color_Back :
                    X.changed = True 
                    X.color = Color_Back
                X.width = X.radius
                X.radius = Radius 
                
                
Gameover = False 
while not Gameover :
    #Window.fill( ( 0 , 0 , 0 ) )
    #pg.time.Clock().tick(60)
    for Y in Pixels :
        for X in Y :
            if X.changed : X.Display()
            X.changed = False 
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            Gameover = True
    Mouse() 
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
pg.quit() 
