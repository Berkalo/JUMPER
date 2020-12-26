from sys import exit
import pygame as pg
from pygame.locals import *
vk = pg.image.load("vk.jpg")
bgrd = pg.image.load("jb.png")
tree = pg.image.load("tree.jpg")
GO = pg.image.load("GO.jpg")
screensize = (600, 500)
win = pg.display.set_mode(screensize)
while True:
    a = True
    movex = 0
    pg.init()
    pg.display.set_caption("RectoRun")
    pg.display.set_icon(vk)
    y = 442
    x = 250
    win.blit(bgrd, (0, 0))
    win.blit(vk, (250, y))
    pg.display.update()
    dir_boolr = False
    dir_booll = False
    TC = True
    tx = 0
    ty = 442
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                P = True
                if event.key == K_UP:
                    while True:
                        if y >= 342 and P:
                            y -= 1
                            if y == 342:
                                P = False
                        elif y <= 438:
                            y += 1
                        else:
                            break
                        if dir_booll:
                            if x != 600:
                                x -= 1
                            else:
                                break
                        if dir_boolr:
                            if x != 600:
                                x += 1
                            else:
                                break
                        if TC:
                            tx += 1
                            if tx >= 600:
                                TC = False
                        if not TC:
                            tx -= 1
                            if tx < 0:
                                TC = True
                        win.blit(bgrd, (0, 0))
                        win.blit(vk, (x, y))
                        win.blit(tree, (tx, ty))
                        pg.display.update()
                        # pg.time.wait(25)
                if event.key == K_RIGHT:
                    movex = +1
                    dir_boolr = True
                elif event.key == K_LEFT:
                    movex = -1
                    dir_booll = True
            if event.type == pg.KEYUP:
                movex = 0
                dir_boolr = False
                dir_booll = False
        if TC:
            tx += 1
            if tx >= 600:
                TC = False
        elif not TC:
            tx -= 1
            if tx < 0:
                TC = True
        if x > 0 and x < 600:
            pass
        elif x >= 0:
            movex = 0
            x=3
        elif x <= 600:
            movex = 0
            x=555
        x += movex
        win.blit(bgrd, (0, 0))
        win.blit(vk, (x, y))
        win.blit(tree, (tx, ty))
        pg.display.update()
        if abs(tx - x) < 55 and abs(y - ty) < 150:
            break
    while a:
        win.blit(GO, (-215, -65))
        pg.display.update()
        for event in pg.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                a = False
    continue
