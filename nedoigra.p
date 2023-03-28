from pygame import *
from random import*
import pygame as pg
import pymunk.pygame_util as pmu 
import pymunk as pm
pg.init()
okno = pg.display.set_mode((600,400))
pmu.positive_y_is_up = False
draw_opt = pmu.DrawOptions(okno)

app = QApplication([])
okno = QWidget()
okno.resize(600,400)

game = True

while game:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    okno.fill((0,0,0))

    

    space.debug_draw(draw_opt)
    pg.display.update()
    space.step(1/60)
    clock.tick(60)
    display.flip()
