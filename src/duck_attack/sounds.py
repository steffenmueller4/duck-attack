"""Background ambience: duck sounds at random intervals."""

import random
from pathlib import Path

import pygame

from duck_attack import settings


class AmbientSounds:
    """Plays one of the ambient sounds every few seconds, never the same one twice in a row.

    Stays silent (instead of crashing) when no audio device is available.
    """

    def __init__(self, paths: list[Path] = settings.AMBIENT_SOUNDS) -> None:
        self.sounds: list[pygame.mixer.Sound] = []
        if pygame.mixer.get_init():
            for path in paths:
                sound = pygame.mixer.Sound(path)
                sound.set_volume(settings.AMBIENT_VOLUME)
                self.sounds.append(sound)
        self.last_played: int | None = None
        self._schedule_next()

    def _schedule_next(self) -> None:
        self.next_in = random.uniform(settings.AMBIENT_MIN_DELAY, settings.AMBIENT_MAX_DELAY)

    def update(self, dt: float) -> None:
        self.next_in -= dt
        if self.next_in > 0:
            return
        self._schedule_next()
        if not self.sounds:
            return
        choices = [i for i in range(len(self.sounds)) if i != self.last_played] or [0]
        self.last_played = random.choice(choices)
        self.sounds[self.last_played].play()
