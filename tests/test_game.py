import pygame

from duck_attack import settings
from duck_attack.game import Game


def test_game_runs_a_few_frames():
    game = Game()
    assert game.screen.get_size() == (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    assert game.background.get_size() == game.screen.get_size()
    game.run(max_frames=3)
    assert len(game.ducks) == 1
    assert not pygame.get_init()


def test_escape_stops_game():
    game = Game()
    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE))
    game.run(max_frames=100)
    assert not game.running


def test_left_click_shoots_duck_and_next_one_starts():
    game = Game()
    game.update(1.0)
    (duck,) = game.ducks
    x, y = duck.mask.outline()[0]
    pygame.event.post(
        pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(duck.rect.x + x, duck.rect.y + y))
    )
    game.handle_events()
    assert duck.shot
    assert game.score == settings.POINTS_PER_HIT
    game.update(0.01)
    assert len(game.ducks) == 2  # the falling one plus a fresh one
    pygame.quit()


def test_missed_shot_hits_nothing():
    game = Game()
    game.update(1.0)
    assert not game.shoot((settings.SCREEN_WIDTH - 1, settings.SCREEN_HEIGHT - 1))
    assert game.score == 0
    pygame.quit()


def test_each_hit_adds_points():
    game = Game()
    for _ in range(3):
        game.update(1.0)
        duck = next(d for d in game.ducks if not d.shot)
        x, y = duck.mask.outline()[0]
        assert game.shoot((duck.rect.x + x, duck.rect.y + y))
    assert game.score == 3 * settings.POINTS_PER_HIT
    pygame.quit()
