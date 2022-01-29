from abc import ABC, abstractmethod

import pygame

from pyplatformer.image import get_rgb_from_color


class Sprite(ABC):
    """Class to represent a sprite that gets blit onto a screen."""

    def __init__(self, x: int, y: int, height: int, width: int, color: str) -> None:
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color.upper()
        self.rgb = get_rgb_from_color(self.color)

    def shape(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    @abstractmethod
    def update(self):
        pass


class Block(Sprite):

    def update(self):
        pass


class Player(Sprite):
    vel = 20

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel

    def jump(self):
        raise NotImplementedError()
