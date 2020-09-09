# Author: Joanna Kus
import pygame as pg
from time import sleep

r = int(input("Pick a red value."))
g = int(input("Pick a green value."))
b = int(input("Pick a blue value."))

bgColor = (r, g, b)
White = (255, 255, 255)
(width, height) = (700, 700)

coords = [350, 350]
oldCoords = [350, 350]
drawBool = True
cursorBool = True

pg.init()
pg.mouse.set_cursor(*pg.cursors.diamond)

#Creates the screen.
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Etch-A-Sketch')
screen.fill(bgColor)

#Updates the screen.
pg.display.flip()

running = True
while running:

    #Stops the game from running when you click the X button.    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    #I - Up. K - Down. J - Left. L - Right.
    if pg.key.get_pressed()[pg.K_i]:
        if coords[1] >= 1:
            coords[1] -= 1
    if pg.key.get_pressed()[pg.K_k]:
        if coords[1] < 699:
            coords[1] += 1
    if pg.key.get_pressed()[pg.K_j]:
        if coords[0] >= 0:
            coords[0] -= 1
    if pg.key.get_pressed()[pg.K_l]:
        if coords[0] <= 698:
            coords[0] += 1

    if pg.key.get_pressed()[pg.K_p] and drawBool:
        drawBool = False
    elif pg.key.get_pressed()[pg.K_p] and not drawBool:
        drawBool = True

    #Locks the cursor on the window.
    if pg.key.get_pressed()[pg.K_ESCAPE] and cursorBool:
        cursorBool = False
    elif pg.key.get_pressed()[pg.K_ESCAPE] and not cursorBool:
        cursorBool = True

    #Clears the screen.
    if pg.key.get_pressed()[pg.K_y]:
        screen.fill(bgColor)

    #Keeps it from drawing too fast.
    sleep(0.015)
    #Draws a white line on the screen from 0,0 to 50,30, 5px wide.
    if drawBool:
        pg.draw.line(screen, White, oldCoords, coords, 2)
    if cursorBool:
        pg.mouse.set_pos(coords)
    pg.display.flip()

    #Helps draw the lines.
    oldCoords = coords

#This actually closes the window.
pg.quit()
