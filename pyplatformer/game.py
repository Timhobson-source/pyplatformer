import pygame

from pyplatformer.window import WindowManager


class GameMeta:
    def __init__(self) -> None:
        self._game_won = False

    def game_over(self):
        return False

    def game_won(self):
        return self._game_won

    def set_game_won(self):
        self._game_won = True


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.fps = 60
        self.clock = pygame.time.Clock()

    def create_window(self, width: int = 500, height: int = 500) -> pygame.Surface:
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Platformer!")
        return window

    def setup(self, window_manager: WindowManager):
        example = window_manager.create_sprite(250, 250, 10, 10, 'red')
        window_manager.draw(example)

    def play(self) -> None:
        meta = GameMeta()
        window = self.create_window()
        manager = WindowManager(window)

        self.setup(manager)

        playing = True
        while playing:
            pygame.time.delay(50)

            if meta.game_over():
                self.playing = False
                window.display_game_over_window()
            elif meta.game_won():
                self.playing = False
                window.display_game_won()

            manager.update_window()
            self.clock.tick(self.fps)
