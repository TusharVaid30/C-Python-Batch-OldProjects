import subprocess as sp
import random 
def cls():
    tmp = sp.call('cls' , shell = True)
    
Height = Width = 20
wall  = "X"
head  = "#"
space = " "
Gameover = True
score = 0
d = dd = ""
def Setup() :
    global x,y,px,py,d,Gameover
    cls()
    x = int(Width/2) ; y = int(Height/2)
    px = random.randint(1,Width-1) ; py = random.randint(1,Height-1)
    d = "halt"
    Gameover = False
def Draw() :
    cls()
    for _ in range(Width+1) : print(wall,end="")
    print()
    for _ in range(Height):
        for __ in range(Width):
            if __ == 0 or  __ == Width-1 : print(wall,end="")
            if _  == y and __ == x     : print(head,end="")
            else : print(space,end="")
        print()
    for _ in range(Width+1) : print(wall,end="")
    print("\nScore :",score)
def Input() :
    global d,dd
    input(dd)
    if dd == "w" : d = "up"
    if dd == "a" : d = "left"
    if dd == "s" : d = "down"
    if dd == "d" : d = "right"
    
def Logic() :
    if d == "up"   : y -= 1
    if d == "down" : y += 1
    if d == "left" : x -= 1
    if d == "right": x += 1
    col()
def col() :
    global Gameover
    if x == 0 or x == Width :
        Gameover = True
    if y == 0 or y == Height :
        Gameover = True
def main() :
    Setup()
    while not Gameover :
        Draw()
        Input()
        Logic()

main()
