import pygame

from pyplatformer.sprite import Sprite


class WindowManager:
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window

    def update_window(self) -> None:
        pygame.display.update()

    def display_game_over(self) -> None:
        raise NotImplementedError

    def display_game_won(self) -> None:
        raise NotImplementedError

    def draw(self, sprite: Sprite) -> None:
        pygame.draw.rect(self.window, sprite.color, sprite.shape())

    def create_sprite(self, x: int, y: int, width: int, height: int, color: str) -> Sprite:
        return Sprite(x, y, width, height, color)
