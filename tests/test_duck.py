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


def test_click_on_duck_pixel_hits(duck_image):
    duck = Duck(duck_image, y=100)
    duck.update(1.0)
    x, y = duck.mask.outline()[0]  # a pixel that belongs to the duck
    assert duck.is_hit_by((duck.rect.x + x, duck.rect.y + y))


def test_click_on_transparent_corner_misses(duck_image):
    duck = Duck(duck_image, y=100)
    duck.update(1.0)
    assert duck.rect.collidepoint(duck.rect.topleft)
    assert not duck.is_hit_by(duck.rect.topleft)


def test_shot_duck_falls_and_is_removed(duck_image):
    group = pygame.sprite.Group(duck := Duck(duck_image, y=100))
    duck.update(1.0)
    duck.shoot()
    assert not duck.is_hit_by(duck.rect.center)  # can't be shot twice
    y = duck.rect.y
    duck.update(0.1)
    assert duck.rect.y > y
    for _ in range(50):
        duck.update(0.1)
    assert not group
