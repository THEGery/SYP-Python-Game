# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:16:56 2025

@author: gerald
"""

import pygame, random
#Let's import the Submarine Class
from submarine import Submarine
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)


SCREENWIDTH=800
SCREENHEIGHT=1000

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Adventures Of R.O.V.")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()


rov = Submarine(RED, 60, 80, 70)
rov.rect.x = 160
rov.rect.y = SCREENHEIGHT - 100

obstacle_1 = Submarine(PURPLE, 60, 80, random.randint(50,100))
obstacle_1.rect.x = 60
obstacle_1.rect.y = -100

obstacle_2 = Submarine(YELLOW, 60, 80, random.randint(50,100))
obstacle_2.rect.x = 160
obstacle_2.rect.y = -600

obstacle_3 = Submarine(CYAN, 60, 80, random.randint(50,100))
obstacle_3.rect.x = 260
obstacle_3.rect.y = -300

obstacle_4 = Submarine(BLUE, 60, 80, random.randint(50,100))
obstacle_4.rect.x = 360
obstacle_4.rect.y = -900


# Add the car to the list of objects
all_sprites_list.add(rov)
# all_sprites_list.add(obstacle_1)
# all_sprites_list.add(obstacle_2)
# all_sprites_list.add(obstacle_3)
# all_sprites_list.add(obstacle_4)

all_coming_obstacles = pygame.sprite.Group()
all_coming_obstacles.add(obstacle_1)
all_coming_obstacles.add(obstacle_2)
all_coming_obstacles.add(obstacle_3)
all_coming_obstacles.add(obstacle_4)


#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()

while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     carryOn=False
                     
        # polling vs event-triggered
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rov.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            rov.moveRight(5)
        if keys[pygame.K_UP]:
            speed += 0.05
        if keys[pygame.K_DOWN]:
            speed -= 0.05


        #Game Logic
        for obstacle in all_coming_obstacles:
            obstacle.moveForward(speed)
            if obstacle.rect.y > SCREENHEIGHT:
                obstacle.changeSpeed(random.randint(50,100))
                obstacle.repaint(random.choice(colorList))
                obstacle.rect.y = -200
                
        #Check if there is a obstacle collision
        obstacle_collision_list = pygame.sprite.spritecollide(rov,all_coming_obstacles,False)
        for obstacle in obstacle_collision_list:
            print("obstacle crash!")
            #End Of Game
            carryOn=False
                
        all_sprites_list.update()
        all_coming_obstacles.update()

        #Drawing on Screen
        screen.fill(GREEN)
        #Draw The Road
        pygame.draw.rect(screen, GREY, [40,0, 400,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)


        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        # Actually it's items in the list: player plus 4 others
        all_sprites_list.draw(screen)
        all_coming_obstacles.draw(screen)
        # Draw other cars to screen
        # all_coming_obstacles.draw(screen)

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()