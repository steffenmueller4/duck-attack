import pygame
import pytest

from duck_attack import settings
from duck_attack.sounds import AmbientSounds


@pytest.fixture
def mixer():
    pygame.mixer.init()
    yield
    pygame.mixer.quit()


def test_all_ambient_sounds_load(mixer):
    ambience = AmbientSounds()
    assert len(ambience.sounds) == len(settings.AMBIENT_SOUNDS) == 3


def test_plays_after_delay_and_reschedules(mixer):
    ambience = AmbientSounds()
    first_delay = ambience.next_in
    assert settings.AMBIENT_MIN_DELAY <= first_delay <= settings.AMBIENT_MAX_DELAY
    ambience.update(first_delay - 0.1)
    assert ambience.last_played is None
    ambience.update(0.2)
    assert ambience.last_played is not None
    assert settings.AMBIENT_MIN_DELAY <= ambience.next_in <= settings.AMBIENT_MAX_DELAY


def test_never_repeats_the_same_sound_twice_in_a_row(mixer):
    ambience = AmbientSounds()
    previous = None
    for _ in range(30):
        ambience.update(settings.AMBIENT_MAX_DELAY)
        assert ambience.last_played != previous
        previous = ambience.last_played


def test_silent_without_audio_device():
    pygame.mixer.quit()
    ambience = AmbientSounds()
    assert ambience.sounds == []
    ambience.update(settings.AMBIENT_MAX_DELAY)  # must not raise
    assert ambience.last_played is None
