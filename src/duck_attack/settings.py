"""Game-wide constants."""

from pathlib import Path

TITLE = "Duck Attack"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

ASSETS_DIR = Path(__file__).parent / "assets"
BACKGROUND_IMAGE = ASSETS_DIR / "images" / "background.png"
