"""Main game loop."""

import pygame

from duck_attack import settings


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.running = False

    def update(self, dt: float) -> None:
        """Advance the game state by ``dt`` seconds."""

    def draw(self) -> None:
        self.screen.fill(settings.SKY_COLOR)
        pygame.display.flip()

    def run(self, max_frames: int | None = None) -> None:
        """Run the game loop until the window is closed (or ``max_frames`` have passed)."""
        frames = 0
        try:
            while self.running:
                dt = self.clock.tick(settings.FPS) / 1000
                self.handle_events()
                self.update(dt)
                self.draw()
                frames += 1
                if max_frames is not None and frames >= max_frames:
                    break
        finally:
            pygame.quit()
