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

# Each duck gets a random distance, expressed as a scale factor of DUCK_WIDTH:
# 1.0 is the closest (full size), smaller values are farther away.
DUCK_MIN_SCALE = 0.35
DUCK_MAX_SCALE = 1.0

# Points for a full-size duck. Farther ducks are worth more (POINTS_PER_HIT / scale,
# rounded to POINTS_ROUNDING): e.g. 10 at scale 1.0, 20 at 0.5, 30 at 0.35.
POINTS_PER_HIT = 10
POINTS_ROUNDING = 5

SCORE_FONT_SIZE = 48
SCORE_COLOR = (255, 255, 255)
SCORE_SHADOW_COLOR = (20, 20, 20)
SCORE_MARGIN = 20  # distance from the top-right corner in pixels
# Ducks fly somewhere in the sky band between these y positions.
DUCK_MIN_Y = 40
DUCK_MAX_Y = 320
