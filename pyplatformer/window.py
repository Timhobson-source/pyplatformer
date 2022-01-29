import pygame
from pyplatformer.image import get_rgb_from_color

from pyplatformer.sprite import Block, Player, Sprite


class WindowManager:
    bg_color = 'BLACK'

    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self._sprites_on_screen = []

    def update_window(self) -> None:
        self.draw_background()
        for sprite in self._sprites_on_screen:
            sprite.update()
            self.draw(sprite)
        pygame.display.update()

    def display_game_over(self) -> None:
        raise NotImplementedError

    def display_game_won(self) -> None:
        raise NotImplementedError

    def draw(self, sprite: Sprite) -> None:
        pygame.draw.rect(self.window, sprite.rgb, sprite.shape())

    def create_sprite(self, sprite_cls, *args, **kwargs) -> Sprite:
        sprite = sprite_cls(*args, **kwargs)
        self._sprites_on_screen.append(sprite)
        return sprite

    def create_player(self, x: int, y: int, width: int, height: int, color: str) -> Player:
        return self.create_sprite(Player, x, y, width, height, color)

    def create_block(self, x: int, y: int, width: int, height: int, color: str) -> Block:
        return self.create_sprite(Block, x, y, width, height, color)

    def draw_background(self):
        color = get_rgb_from_color(self.bg_color)
        width = self.window.get_width()
        height = self.window.get_height()
        return pygame.draw.rect(self.window, color, pygame.Rect(0, 0, width, height))
