"""
File containing various functions for colours as well
as rgb values for various common colours
"""

RED   = [255,0,0]
GREEN = [0,255,0]
BLACK = [0,0,0]
WHITE = [255,255,255]

BLUE_SHADOW     = [9, 11, 13]
BLUE_BASE       = [20, 45, 61]
BLUE_HIGHLIGHT  = [30, 90, 129]
BLUE_GLOW       = [21, 139, 216]

GREEN_SHADOW    = [7, 36, 7]
GREEN_BASE      = [31, 134, 31]
GREEN_HIGHLIGHT = [0, 255, 0]

RED_SHADOW      = [41, 3, 3]
RED_BASE        = [79, 6, 6]
RED_HIGHLIGHT   = [163, 12, 12]
RED_GLOW        = [255, 0, 0]

BROWN_SHADOW    = [0, 0, 0,]
BROWN_BASE      = [54, 41, 29]
BROWN_HIGHLIGHT = [120, 91, 62]
BROWN_GLOW      = [199, 148, 98]

BASE_COLOURS = [
    BLUE_SHADOW,
    BLUE_BASE,
    BLUE_HIGHLIGHT,
    BLUE_GLOW,
    GREEN_SHADOW,
    GREEN_BASE,
    GREEN_HIGHLIGHT,
    RED_SHADOW,
    RED_BASE,
    RED_HIGHLIGHT,
    RED_GLOW,
    BROWN_SHADOW,
    BROWN_BASE,
    BROWN_HIGHLIGHT,
    BROWN_GLOW,
]
def rgb_to_hex(rgb):
    """Converts the rgb values @rgb to its hexadecimal equivalent.
    Note that rgb must be a 3-tuple containing only integers.
    converting an rgba to hex will not preserve transparency."""
    pass

def hex_to_rgb(hex_code):
    """Converts the hex value @hex to its rgb equivalent"""
    pass

