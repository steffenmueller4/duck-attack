"""Game-wide constants."""

from pathlib import Path

TITLE = "Duck Attack"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

ASSETS_DIR = Path(__file__).parent / "assets"
BACKGROUND_IMAGE = ASSETS_DIR / "images" / "background.png"
DUCK_IMAGE = ASSETS_DIR / "images" / "duck.png"

DUCK_WIDTH = 140  # on-screen width in pixels; height keeps the image's aspect ratio
DUCK_SPEED = 260  # pixels per second
# Ducks fly somewhere in the sky band between these y positions.
DUCK_MIN_Y = 40
DUCK_MAX_Y = 320
