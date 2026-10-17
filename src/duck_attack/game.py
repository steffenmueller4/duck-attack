"""Main game loop."""

import pygame

from duck_attack import settings
from duck_attack.crosshair import make_crosshair_cursor
from duck_attack.duck import Duck, load_duck_image
from duck_attack.hud import ScoreDisplay


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = self._load_background()
        self.duck_image = load_duck_image()
        self.ducks: pygame.sprite.Group = pygame.sprite.Group()
        pygame.mouse.set_cursor(make_crosshair_cursor())
        self.score = 0
        self.score_display = ScoreDisplay()

    def _load_background(self) -> pygame.Surface:
        image = pygame.image.load(settings.BACKGROUND_IMAGE).convert()
        if image.get_size() != self.screen.get_size():
            image = pygame.transform.smoothscale(image, self.screen.get_size())
        return image

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.shoot(event.pos)

    def shoot(self, pos: tuple[int, int]) -> bool:
        """Fire at screen position ``pos``. Hits at most one duck; returns whether one was hit."""
        # Check the top-most (last drawn) duck first.
        for duck in reversed(self.ducks.sprites()):
            if duck.is_hit_by(pos):
                duck.shoot()
                self.score += settings.POINTS_PER_HIT
                return True
        return False

    def update(self, dt: float) -> None:
        """Advance the game state by ``dt`` seconds."""
        # Send in a new duck once no duck is flying anymore (left the screen or shot).
        if all(duck.shot for duck in self.ducks):
            self.ducks.add(Duck(self.duck_image))
        self.ducks.update(dt)

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))
        self.ducks.draw(self.screen)
        self.score_display.draw(self.screen, self.score)
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
