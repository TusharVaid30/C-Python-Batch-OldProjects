#         ||||||
#         ||||||
#         ||||||
#         /___/
#       C|"_" |D
#        \___/
#      ___) (__
#     | (.) (.) \
#    | | )   (\\ \
#   | | /     \ \ \
#  |_/  (  .  ) \_\
#      )       (                            C\=\======8
#     |   .V.  )
#     \  | ||  \
#      \  \|/  /
#       /#)|(#|
#      / / |\ \
#     |_|  ||_|
#     \_|  |\_|
#     ""'  |""'  V
#          \    /
#           \__/
#
#

#-___-^^-____

Trail_Wisps = []

import math , pygame as pg
from random import randint , choice
from time   import time
pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )

def sin( x ) : return math.sin( x*math.pi/180 )
def cos( x ) : return math.cos( x*math.pi/180 )
def Circle( x , y , color , size ) : pg.draw.circle( Window , color , ( int(x) , int(y) ) , int(size) )

#COLORS
Color_Black        = (  0  ,  0  ,  0  )
Color_White        = ( 255 , 255 , 255 )
Color_Red          = ( 128 ,  0  ,  0  )
Color_Green        = (  28  , 234 , 111  )
Color_Blue         = (  28  ,  111  , 234 )
Color_Orange       = ( 255 , 100 ,  0  )
Color_Yellow       = ( 255 , 255 ,  0  )
Color_Light_Red    = ( 255 ,  0  ,  0  )
Color_Light_Green  = (  0  , 255 ,  0  )
Color_Light_Blue   = (  0  ,  0  , 255 )

# KEYBINDS
Controls_Move_Up      = pg.K_w
Controls_Move_Down    = pg.K_s
Controls_Move_Left    = pg.K_a
Controls_Move_Right   = pg.K_d
Controls_Bullet_Fired = pg.K_e
Controls_Laser_Fired  = pg.K_r
Controls_Twinkle      = pg.K_f
Controls_Quit         = pg.K_ESCAPE


Gameover = False
FPS = 120


Spaceship_Start_x = Window_Width/2
Spaceship_Start_y = Window_Height/2
Spaceship_Start_Health = 100
Spaceship_Start_dx = Spaceship_Start_dy = 6
Spaceship_Thruster_Colors = [ Color_Blue , Color_Light_Blue , Color_Green , Color_Light_Green ]
Spaceship_Image = pg.image.load("Ship.png")

Stars_Count = 0
Stars_Max_dx = 10
Stars_Max_dy = 20

Temp_Twinkle = True

Enemies_Number = 10
Enemy_Image = pg.image.load("Enemy.png")
Enemy_Start_Health = 100
