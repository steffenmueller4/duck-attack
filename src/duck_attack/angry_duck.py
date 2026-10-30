"""The angry duck sprite: a bonus target that briefly pops up at a random spot."""

import random

import pygame

from duck_attack import settings


def load_angry_duck_image() -> pygame.Surface:
    """Load the angry duck image scaled to ``settings.ANGRY_DUCK_WIDTH``. Needs an open display."""
    image = pygame.image.load(settings.ANGRY_DUCK_IMAGE).convert_alpha()
    w, h = image.get_size()
    size = (settings.ANGRY_DUCK_WIDTH, round(h * settings.ANGRY_DUCK_WIDTH / w))
    return pygame.transform.smoothscale(image, size)


def random_center(image: pygame.Surface) -> tuple[float, float]:
    """A random center where the whole image is on screen and clear of the HUD at the top."""
    w, h = image.get_size()
    x = random.uniform(w / 2, settings.SCREEN_WIDTH - w / 2)
    y = random.uniform(settings.ANGRY_DUCK_MARGIN + h / 2, settings.SCREEN_HEIGHT - h / 2)
    return x, y


class AngryDuck(pygame.sprite.Sprite):
    """An angry duck that pops up in place and vanishes again if it isn't shot in time.

    It grows to full size within ``settings.ANGRY_DUCK_POP_TIME``, stays for
    ``settings.ANGRY_DUCK_LIFETIME`` and, once shot, turns upside down and falls.
    """

    def __init__(self, image: pygame.Surface, center: tuple[float, float] | None = None) -> None:
        super().__init__()
        self.full_image = image
        # Track position as floats; rect coordinates are ints and would lose sub-pixel motion.
        self.x, self.y = random_center(image) if center is None else center
        self.time = 0.0
        self.shot = False
        self.fall_speed = 0.0
        self._resize(0.0)

    def _resize(self, factor: float) -> None:
        w, h = self.full_image.get_size()
        size = (max(1, round(w * factor)), max(1, round(h * factor)))
        self.image = (
            self.full_image if factor >= 1 else pygame.transform.smoothscale(self.full_image, size)
        )
        # Pixel mask so clicks on the transparent area around the duck don't count as hits.
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(round(self.x), round(self.y)))

    @property
    def points(self) -> int:
        return settings.ANGRY_DUCK_POINTS

    def is_hit_by(self, pos: tuple[int, int]) -> bool:
        """Whether a shot at screen position ``pos`` hits this (not yet shot) duck."""
        if self.shot or not self.rect.collidepoint(pos):
            return False
        return bool(self.mask.get_at((pos[0] - self.rect.x, pos[1] - self.rect.y)))

    def shoot(self) -> None:
        self.shot = True
        self.image = pygame.transform.flip(self.image, False, True)

    def update(self, dt: float) -> None:
        if self.shot:
            self.fall_speed += settings.DUCK_FALL_GRAVITY * dt
            self.y += self.fall_speed * dt
            self.rect.center = (round(self.x), round(self.y))
            if self.rect.top > settings.SCREEN_HEIGHT:
                self.kill()
            return
        growing = self.time < settings.ANGRY_DUCK_POP_TIME
        self.time += dt
        if self.time >= settings.ANGRY_DUCK_LIFETIME:
            self.kill()
        elif growing:
            self._resize(min(1.0, self.time / settings.ANGRY_DUCK_POP_TIME))
