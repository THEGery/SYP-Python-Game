# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 23:35:41 2025

@author: gerald

This module represents the main submarine - the R.O.V.
So far it mainly consists of the Submarine class but everything related to the
main subject, the R.O.V., will be added here.
"""

import pygame
import os
WHITE = (255, 255, 255)

class Submarine(pygame.sprite.Sprite):
    #This class represents a submarine. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Instead we could load a proper pciture of a submarine...
        # self.image = pygame.image.load("submarine.png").convert_alpha()
        # base_path = os.path.dirname(__file__)
        # image_path = os.path.join(base_path, "..", "art", "assets", "player", "player.png")
        # self.image = pygame.image.load(image_path)
        
        # Pass in the color of the submarine, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        #Initialise attributes of the submarine.
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
 
        # Draw the submarine (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    
    def moveRight(self, pixels):
        self.rect.x += pixels
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
        
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
        
    def changeSpeed(self, speed):
        self.speed = speed
        
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])