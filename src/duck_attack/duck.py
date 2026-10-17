"""The duck sprite."""

import math
import random

import pygame

from duck_attack import settings


def load_duck_image() -> pygame.Surface:
    """Load the duck image scaled to ``settings.DUCK_WIDTH``. Needs an open display."""
    image = pygame.image.load(settings.DUCK_IMAGE).convert_alpha()
    w, h = image.get_size()
    size = (settings.DUCK_WIDTH, round(h * settings.DUCK_WIDTH / w))
    return pygame.transform.smoothscale(image, size)


class Duck(pygame.sprite.Sprite):
    """A duck that flies from just off the left edge across the screen to the right."""

    def __init__(self, image: pygame.Surface, y: float | None = None) -> None:
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.base_y = random.uniform(settings.DUCK_MIN_Y, settings.DUCK_MAX_Y) if y is None else y
        # Track position as floats; rect coordinates are ints and would lose sub-pixel motion.
        self.x = float(-self.rect.width)
        self.time = 0.0
        self.rect.topleft = (round(self.x), round(self.base_y))

    def update(self, dt: float) -> None:
        self.time += dt
        self.x += settings.DUCK_SPEED * dt
        bob = math.sin(self.time * 3) * 12  # gentle up-and-down while flying
        self.rect.topleft = (round(self.x), round(self.base_y + bob))
        if self.rect.left > settings.SCREEN_WIDTH:
            self.kill()
