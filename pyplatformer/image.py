
color_to_rgb = dict(
    BLACK=(0, 0, 0),
    WHITE=(255, 255, 255),
    RED=(255, 0, 0),
    YELLOW=(255, 255, 0),
    PURPLE=(102, 0, 102),
    GREEN=(0, 255, 0),
    PINK=(220, 20, 60),
)


def get_rgb_from_color(color: str):
    try:
        return color_to_rgb[color]
    except KeyError:
        raise ValueError("Color not supported.")
