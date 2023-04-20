import sys
import pygame as pg


class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x  # Position X
        self.y = y  # Position Y
        self.w = w  # Width
        self.h = h  # Height

    def draw(self, screen):
        pg.draw.rect(screen, 'cyan', (self.x, self.y, self.w, self.h))


pg.init()
run = True

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
square = Rectangle(350, 200, 100, 100)
while (run):
    screen.fill((255, 255, 255))
    square.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            square.y += 20
            print("Key S down")
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            square.y -= 20
            print("Key W up")

        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            square.x -= 20
            print("Key A left")

        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            square.x += 20
            print("Key D right")
