import pygame
import pytest

from duck_attack import settings
from duck_attack.angry_duck import AngryDuck, load_angry_duck_image


@pytest.fixture
def angry_image():
    pygame.init()
    pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    yield load_angry_duck_image()
    pygame.quit()


def _grown(image, center=(400, 400)):
    duck = AngryDuck(image, center=center)
    duck.update(settings.ANGRY_DUCK_POP_TIME)
    return duck


def _duck_pixel(duck):
    x, y = duck.mask.outline()[0]  # a pixel that belongs to the duck
    return duck.rect.x + x, duck.rect.y + y


def test_angry_duck_image_is_scaled_and_transparent(angry_image):
    assert angry_image.get_width() == settings.ANGRY_DUCK_WIDTH
    assert angry_image.get_at((0, 0)).a == 0
    assert _grown(angry_image).rect.size == angry_image.get_size()


def test_angry_duck_appears_fully_on_screen_below_the_hud(angry_image):
    w, h = angry_image.get_size()
    for _ in range(200):
        duck = AngryDuck(angry_image)
        duck.update(settings.ANGRY_DUCK_POP_TIME)
        assert duck.rect.left >= 0 and duck.rect.right <= settings.SCREEN_WIDTH
        assert duck.rect.top >= settings.ANGRY_DUCK_MARGIN - 1  # rounding of the center
        assert duck.rect.bottom <= settings.SCREEN_HEIGHT + 1


def test_angry_duck_pops_up_then_vanishes_unshot(angry_image):
    group = pygame.sprite.Group(duck := AngryDuck(angry_image, center=(400, 400)))
    assert duck.rect.width < angry_image.get_width()
    duck.update(settings.ANGRY_DUCK_POP_TIME / 2)
    half = duck.rect.width
    assert 0 < half < angry_image.get_width()
    assert duck.rect.center == (400, 400)  # grows in place
    duck.update(settings.ANGRY_DUCK_POP_TIME / 2)
    assert duck.rect.width == angry_image.get_width()
    duck.update(settings.ANGRY_DUCK_LIFETIME - settings.ANGRY_DUCK_POP_TIME - 0.01)
    assert group
    duck.update(0.02)
    assert not group


def test_click_on_angry_duck_pixel_hits_also_while_growing(angry_image):
    duck = AngryDuck(angry_image, center=(400, 400))
    duck.update(settings.ANGRY_DUCK_POP_TIME / 2)
    assert duck.is_hit_by(_duck_pixel(duck))
    grown = _grown(angry_image)
    assert grown.is_hit_by(_duck_pixel(grown))


def test_click_on_angry_duck_transparent_corner_misses(angry_image):
    duck = _grown(angry_image)
    assert duck.rect.collidepoint(duck.rect.topleft)
    assert not duck.is_hit_by(duck.rect.topleft)


def test_shot_angry_duck_falls_and_is_removed(angry_image):
    group = pygame.sprite.Group(duck := _grown(angry_image))
    assert duck.points == settings.ANGRY_DUCK_POINTS
    duck.shoot()
    assert not duck.is_hit_by(duck.rect.center)  # can't be shot twice
    y = duck.rect.y
    duck.update(0.1)
    assert duck.rect.y > y
    for _ in range(50):
        duck.update(0.1)
    assert not group
