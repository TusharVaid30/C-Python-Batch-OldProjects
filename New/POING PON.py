import pygame as pg
from random import randint as R , choice as C
import math
def cos( x ) : return math.cos( x*math.pi/180 ) 
def sin( x ) : return math.sin( x*math.pi/180 )
def tan( x ) : return math.tan( x*math.pi/180 )

Text_Size = 40

pg.init()
Window_Width  = 500 # pg.display.Info().current_w
Window_Height = 500 # pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) ) #, pg.FULLSCREEN )

#pygame.draw.line(<surface>, (<rgb>), (start x, start y), (end x, end y), width)
#Window.blit(pg.font.SysFont(None, size).render(text, True, color), (x, y))

class Point :
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , abs(int(self.size)) )
Balls = []
for _ in range( 10 ) : Balls.append( Point() )
for Ball in Balls : 
    Ball.size = R(10,20)
    Ball.x = R(Ball.size , Window_Width  - Ball.size)
    Ball.y = R(Ball.size , Window_Height - Ball.size)
    Ball.color = ( 255 , 255 , 255 )
    



while True :
    Window.fill( ( 0 , 0 , 0 ) )

    Clicked = pg.mouse.get_pressed()[0]
    
    if not Clicked :
        Holding = False
    
    if Clicked and not Holding :
        Mouse_x , Mouse_y = pg.mouse.get_pos()
        for Ball in Balls :
            if Mouse_x > Ball.x - Ball.size and Mouse_x < Ball.x + Ball.size and Mouse_y > Ball.y - Ball.size and Mouse_y < Ball.y + Ball.size :
                Holding = True
                Current_Ball = Ball
                Buffer_x = Ball.x - Mouse_x  
                Buffer_y = Ball.y - Mouse_y  
                break 
    if Holding :
        Mouse_x , Mouse_y = pg.mouse.get_pos()
        Current_Ball.x = (Mouse_x + Buffer_x)
        Current_Ball.y = (Mouse_y + Buffer_y)
        
    for Ball in Balls : Ball.Display()
    for event in pg.event.get() :
        if event.type == pg.QUIT : break
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
    
pg.quit()
