import pygame as pg
import config as cfg
import sys

def main():
    pg.init()
    window = pg.display.set_mode((cfg.RES_X, cfg.RES_Y))
    pg.display.set_caption(cfg.game_name)
    pg.mouse.set_visible(1)
    pg.key.set_repeat(1, 30)

    clock = pg.time.Clock()
   
    running = True

    try:
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
        pg.quit()
    except SystemExit:
        pg.quit()



        
   

if __name__ == '__main__':
    main()
