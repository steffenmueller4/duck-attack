import os

# Run Pygame headless so tests work without a display (e.g. in CI).
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
