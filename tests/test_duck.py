import pygame
import pytest

from duck_attack import settings
from duck_attack.duck import Duck, load_duck_image


@pytest.fixture
def duck_image():
    pygame.init()
    pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    yield load_duck_image()
    pygame.quit()


def test_duck_image_is_scaled_and_transparent(duck_image):
    assert duck_image.get_width() == settings.DUCK_WIDTH
    assert duck_image.get_at((0, 0)).a == 0


def test_duck_starts_off_screen_left_and_flies_right(duck_image):
    duck = Duck(duck_image, y=100)
    assert duck.rect.right <= 0
    start = duck.rect.x
    duck.update(0.5)
    assert duck.rect.x > start


def test_duck_is_removed_after_leaving_screen_right(duck_image):
    group = pygame.sprite.Group(duck := Duck(duck_image, y=100))
    crossing_time = (settings.SCREEN_WIDTH + 2 * duck.rect.width) / settings.DUCK_SPEED
    for _ in range(int(crossing_time / 0.1) + 1):
        duck.update(0.1)
    assert not group
