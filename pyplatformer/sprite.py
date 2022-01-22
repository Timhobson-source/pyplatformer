import pygame
from pyplatformer.image import get_rgb_from_color


class Sprite:
    """Class to represent a sprite that gets blit onto a screen."""

    def __init__(self, x: int, y: int, height: int, width: int, color: str) -> None:
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color.upper()
        self.rgb = get_rgb_from_color(self.color)

    def shape(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
