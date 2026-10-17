"""On-screen display: the score counter."""

import pygame

from duck_attack import settings


class ScoreDisplay:
    """Draws the score in the top-right corner, re-rendering the text only when it changes."""

    def __init__(self) -> None:
        self.font = pygame.font.Font(None, settings.SCORE_FONT_SIZE)
        self._score: int | None = None
        self._text: pygame.Surface | None = None

    def _render(self, score: int) -> pygame.Surface:
        label = f"Score: {score}"
        text = self.font.render(label, True, settings.SCORE_COLOR)
        shadow = self.font.render(label, True, settings.SCORE_SHADOW_COLOR)
        # Drop shadow keeps the text readable on bright sky and clouds.
        surface = pygame.Surface((text.get_width() + 3, text.get_height() + 3), pygame.SRCALPHA)
        surface.blit(shadow, (3, 3))
        surface.blit(text, (0, 0))
        return surface

    def draw(self, screen: pygame.Surface, score: int) -> None:
        if score != self._score:
            self._score = score
            self._text = self._render(score)
        rect = self._text.get_rect(
            topright=(screen.get_width() - settings.SCORE_MARGIN, settings.SCORE_MARGIN)
        )
        screen.blit(self._text, rect)
