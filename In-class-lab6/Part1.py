import sys
import pygame as pg


class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x  # Position X
        self.y = y  # Position Y
        self.w = w  # Width
        self.h = h  # Height

    def draw(self, screen):
        pg.draw.rect(screen, (100, 20, 100), (self.x, self.y, self.w, self.h))


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    def isMouseOn(self):
        mouse_pos = pg.mouse.get_pos()
        self = pg.draw.rect(screen, (100, 20, 100),
                            (self.x, self.y, self.w, self.h))
        if self.collidepoint(mouse_pos):
            return True
        else:
            return False


pg.init()
run = True

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))


btn = Button(350, 200, 100, 100)
while (run):
    screen.fill((255, 255, 255))

    btn.draw(screen)

    if btn.isMouseOn():
        pg.draw.rect(screen, (128, 128, 128), (btn.x, btn.y, btn.w, btn.h))
        if pg.mouse.get_pressed()[0]:
            pg.draw.rect(screen, 'red', (btn.x, btn.y, btn.w, btn.h))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
