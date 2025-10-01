#!/usr/bin/env python

"""
SYP Python prototype | Author viktor.barath7@gmail.com

Main code for the game, it should contain the core of the game and tie the components together.
For now for experimentation and to better understad the code, it'll contain all the basic code.

**REMEINDER** to split up the code into (possibly more, depending on the complexity):
- main
- constants
- renderer
- actors
"""

import pygame

pygame.init()


SCREEN_HIGHT = 900
SCREEN_WIDTH = int(SCREEN_HIGHT * 0.8)

screen = pygame.display.set_mode((SCREEN_HIGHT, SCREEN_WIDTH))
pygame.display.set_caption("SYP Python Game Prototype")
clock = pygame.time.Clock()
dt = 0


#player dot
player_pos = pygame.Vector2(SCREEN_HIGHT / 2, SCREEN_WIDTH / 2)


#player sprite
#needs some images to call, will replace player dot
"""
x = 200
y = 200
img = pygame.image.load('<path to image files>')
rect = img.get_rect()
"""


#running = True means the game runs. Used in the game loop
running = True
#game loop
while running:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False
      

    screen.fill("navy")

    pygame.draw.circle(screen, "white", player_pos, 20 )


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt



    pygame.display.flip()


    #dt is delta time in seconds since last frame, used for framerate
    dt = clock.tick(60) / 1000


pygame.quit()