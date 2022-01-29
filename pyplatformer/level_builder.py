from typing import List

from pyplatformer.window import WindowManager

level_example = [
    "          ",
    "          ",
    "          ",
    "          ",
    "    xxx   ",
    "          ",
    "     x    ",
    " p  xxx   ",
    "xxxxxxxxxx",
    "xxxxxxxxxx",
]


def build_level(level: List[str], window_manager: WindowManager, block_size: int):
    for y, horizontal in enumerate(level):
        for x, block in enumerate(horizontal):
            if block == "x":
                block = window_manager.create_block(
                    x*block_size, y*block_size, block_size, block_size, 'purple')
                window_manager.draw(block)
            elif block == "p":
                player = window_manager.create_player(
                    x*block_size, y*block_size, block_size, block_size, 'red')
                window_manager.draw(player)
