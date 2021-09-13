from Functions import *

def main() :
    while not Gameover :
        pg.time.Clock().tick(FPS)
        Window.fill(Color_Black)
        Controls()
        Logic()
        Display()
        pg.display.flip()
        if pg.key.get_pressed()[pg.K_ESCAPE]: break
main()

pg.quit()
quit()
