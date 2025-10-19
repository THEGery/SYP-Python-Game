# -*- coding: utf-8 -*-
"""This module represents the main submarine - the R.O.V.

So far it mainly consists of the Submarine class but everything
related to the main subject, the R.O.V., will be added here.
"""

import pygame
import os

WHITE = (255, 255, 255)


class Submarine(pygame.sprite.Sprite):
    """Submarine class; derives from the Sprite class."""

    def __init__(self, color, width, height, speed):
        """Call the parent class (Sprite) constructor."""
        super().__init__()

        # Instead we could load a proper pciture of a submarine...
        # self.image = pygame.image.load("submarine.png").convert_alpha()
        # BASE_PATH = os.path.dirname(__file__)
        # image_path = os.path.join(BASE_PATH, "..",
        #                           "art", "assets", "player", "player.png")
        # self.image = pygame.image.load(image_path)

        # Pass in color, x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Initialise attributes of the submarine.
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        # Draw the submarine (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch rectangle object which has the dimensions of the image
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        """Move character to the right."""
        self.rect.x += pixels

    def move_left(self, pixels):
        """Move character to the left."""
        self.rect.x -= pixels

    def move_forward(self, speed):
        """Move character forward."""
        self.rect.y += self.speed * speed / 20

    def move_backward(self, speed):
        """Move character backwards."""
        self.rect.y -= self.speed * speed / 20

    def change_speed(self, speed):
        """Change the speed of the player character."""
        self.speed = speed

    def repaint(self, color):
        """Define color of the player character."""
        self.color = color
        pygame.draw.rect(self.image, self.color,
                         [0, 0, self.width, self.height])
