"""Game-wide constants."""

from pathlib import Path

TITLE = "Duck Attack"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

ASSETS_DIR = Path(__file__).parent / "assets"
BACKGROUND_IMAGE = ASSETS_DIR / "images" / "background.png"
DUCK_IMAGE = ASSETS_DIR / "images" / "duck.png"
CROSSHAIR_IMAGE = ASSETS_DIR / "images" / "crosshair.png"

CROSSHAIR_SIZE = 64  # cursor size in pixels (square)
# Aim point as a fraction of the image size: the red dot, which sits slightly above center.
CROSSHAIR_HOTSPOT = (0.501, 0.485)

DUCK_WIDTH = 140  # on-screen width in pixels; height keeps the image's aspect ratio
DUCK_SPEED = 260  # pixels per second
DUCK_FALL_GRAVITY = 1500  # pixels per second squared, for shot ducks

POINTS_PER_HIT = 10

SCORE_FONT_SIZE = 48
SCORE_COLOR = (255, 255, 255)
SCORE_SHADOW_COLOR = (20, 20, 20)
SCORE_MARGIN = 20  # distance from the top-right corner in pixels
# Ducks fly somewhere in the sky band between these y positions.
DUCK_MIN_Y = 40
DUCK_MAX_Y = 320
