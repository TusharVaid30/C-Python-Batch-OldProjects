from Variables import *

def Teleport_Corner( Arg ) :
    if Arg.x < 0             : Arg.x = Window_Width
    if Arg.x > Window_Width  : Arg.x = 0
    if Arg.y < 0             : Arg.y = Window_Height
    if Arg.y > Window_Height : Arg.y = 0

zz = 1
Beautiful = False
def Nibble( x ) :
    global Beautiful
    if len( x.Particles ) == 0  : Beautiful = True
    if len( x.Particles ) > 600 : Beautiful = False
    if Beautiful : x.Twinkle()

def Stuff() :
    global zz

    if Spaceship.Thrusters[5].angle > 200 or Spaceship.Thrusters[5].angle < 160  : zz *= -1

    Spaceship.Thrusters[5].angle += zz
    Spaceship.Thrusters[6].angle -= zz

def Collide(ship, bullet):#Obj1 - Spaceship, Obj2 - Bullet
    if bullet.x > ship.x and bullet.x < ship.x + ship.Image_Bit:
        if bullet.y > ship.y and bullet.y < ship.y + ship.Image_Bit:
            return True
    return False
'''
    if bullet.y > ship.y  and bullet.y < ship.y + self.Image_Bit:
        if bullet.x > ship.x + Image_Bit*     ( 1  - math.cos( math.asin((ship.y + Image_Bit/2 - bullet.y)*2/self.Image_Bit)) )/2 :
            if bullet.x < ship.x + self.Image_Bit *(1  + math.cos( math.asin((ship.y + self.Image_Bit/2 - bullet.y)*2/self.Image_Bit)) )/2 :
                return True
    return False
'''



def Logic() :
    for Star in Stars :
        Star.Move()
    for Star in Stars : Teleport_Corner( Star )

    Teleport_Corner( Spaceship )
    for bullet in Spaceship.Bullets:
        bullet.Wispy = True
        bullet.Execute()
    Spaceship.Curl()
    Spaceship.Move_Wisp()
    for thruster_particle in Spaceship.Thruster_Particles :
        thruster_particle.Move()
        thruster_particle.size -= thruster_particle.dsize
        if (thruster_particle.x < 0 or thruster_particle.x > Window_Width) or (thruster_particle.y < 0 or thruster_particle.y > Window_Height) or  (thruster_particle.size <= 0) :
            Spaceship.Thruster_Particles.remove( thruster_particle )
    for bullet in Spaceship.Bullets :
        bullet.Move()
        if (bullet.x < 0 or bullet.x > Window_Width) or (bullet.y < 0 or bullet.y > Window_Height) :
            bullet.Wisps.clear()
            Spaceship.Bullets.remove( bullet )
    for Bullet in Spaceship.Bullets:
        for Enemy in Enemies:
            if Collide(Enemy , Bullet):
                Enemy.Health -= Bullet.Damage
                if not(Bullet.Penetrate):
                    Spaceship.Bullets.remove(Bullet)
                break
            else : continue

    for Enemy in Enemies :
        Enemy.Move_Wisp()
        if Enemy.Health <= 0:
            Enemies.remove(Enemy)
    for _ in Trail_Wisps:
        _.Display()


def Controls() :
    global Gameover , Temp_Twinkle

    Key_Pressed = pg.key.get_pressed()
    Mouse_Pressed = pg.mouse.get_pressed()
    Mouse_Position = pg.mouse.get_pos()

    for event in pg.event.get() :
        if event.type == pg.QUIT : Gameover = True

    if Key_Pressed[Controls_Quit]         : Gameover = True
    if Key_Pressed[Controls_Move_Left]    : Spaceship.Move(180)
    if Key_Pressed[Controls_Move_Right]   : Spaceship.Move(0)
    if Key_Pressed[Controls_Move_Down]    : Spaceship.Move(90)
    if Key_Pressed[Controls_Move_Up]      : Spaceship.Move(270)
    if Key_Pressed[Controls_Bullet_Fired] : Spaceship.Shoot()
    if Key_Pressed[Controls_Laser_Fired]  : Spaceship.Fire_Laser(270)
    if Key_Pressed[Controls_Twinkle] :
        if Temp_Twinkle : Spaceship.Twinkle()
    else : Temp_Twinkle = True



def Display_Effects() :
    Spaceship.Display_Particles()
    for Enemy in Enemies :
        Enemy.Display_Particles()
    for Star in Stars : Star.Display()

def Display_Bullets() :
    for Bullet in Spaceship.Bullets :
        Bullet.Display()

    for Laser in Spaceship.Lasers:
        Laser.stuff()
        Laser.display()

def Display() :
    for Enemy in Enemies :
        Enemy.Display()
    Display_Effects()
    Display_Bullets()
    Spaceship.Display()
