import curses
import time
from curses import textpad

snakeskin = "#"
snakehead = "#"
snakeafter = " "
safe0 = 5
safe1 = 5

def main(s) :
    curses.curs_set(0)
    sh , sw = s.getmaxyx()
    box = [ [safe0 , safe0] , [sh - safe1 , sw - safe1] ]
    textpad.rectangle(s,box[0][0],box[0][1],box[1][0],box[1][1])
    snake = [ [sh//2  , sw//2 + 1] , [sh//2  , sw//2] , [sh//2  , sw//2 - 1] ]
    direction = curses.KEY_RIGHT
    for y , x in snake :
        s.addstr( y , x , snakeskin )
    while True :
        key = s.getch()
        if key in [curses.KEY_RIGHT,
                      curses.KEY_LEFT,
                      curses.KEY_UP,
                      curses.KEY_DOWN] :
            direction = key
            
        head = snake[0]

        
        if direction == curses.KEY_RIGHT :
            new_head = [head[0]   , head[1] + 1]
            
        if direction == curses.KEY_LEFT :
            new_head = [head[0]   , head[1] - 1]
            
        if direction == curses.KEY_UP :
            new_head = [head[0] - 1 , head[1]  ]
            
        if direction == curses.KEY_DOWN :
            new_head = [head[0] + 1 , head[1]  ]

            
        snake.insert(0,new_head)
        s.addstr(new_head[0] , new_head[1] , snakehead)
        s.addstr(snake[-1][0] , snake[-1][1] , snakeafter)
        snake.pop()


        
        s.refresh()
        
curses.wrapper(main)    
