import pygame

from duck_attack import settings
from duck_attack.hud import ScoreDisplay


def test_score_is_drawn_in_top_right_corner():
    pygame.init()
    screen = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    screen.fill((0, 0, 255))
    ScoreDisplay().draw(screen, 120)
    margin = settings.SCORE_MARGIN
    changed = [
        (x, y)
        for x in range(0, settings.SCREEN_WIDTH, 2)
        for y in range(0, 120, 2)
        if screen.get_at((x, y))[:3] != (0, 0, 255)
    ]
    pygame.quit()
    assert changed
    assert min(x for x, _ in changed) > settings.SCREEN_WIDTH / 2
    assert max(x for x, _ in changed) <= settings.SCREEN_WIDTH - margin
    assert min(y for _, y in changed) >= margin
