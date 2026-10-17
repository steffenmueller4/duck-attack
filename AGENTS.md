# AGENTS.md

Duck Attack is a small Moorhuhn-style shooter built with Pygame (`pygame-ce`, imported as `pygame`).

## Commands

- Install: `pip install -r requirements-dev.txt` (editable install + dev tools)
- Run: `python -m duck_attack`
- Test: `pytest` (headless via `SDL_VIDEODRIVER=dummy` / `SDL_AUDIODRIVER=dummy`, set in
  `tests/conftest.py`)
- Lint/format: `ruff check .` and `ruff format .`

## Conventions

- Source lives in `src/duck_attack/`, tests in `tests/`.
- Game-wide constants (sizes, speeds, timings, colors, file paths) go in `settings.py`;
  don't hard-code tunable values elsewhere.
- Images live in `src/duck_attack/assets/images/`, sounds in `src/duck_attack/assets/sounds/`.
- Assets must have real transparency where needed; check with `file` (RGBA), since images
  that only show a checkerboard pattern are not actually transparent.
- Time-based logic takes `dt` (seconds) in `update(dt)` instead of reading the clock, so
  tests can drive it deterministically.
- Dependency ranges are declared in `pyproject.toml`; exact pins in `requirements*.txt`.
  Update both when adding a dependency.
- Keep `ruff check` and `pytest` passing before committing.
- Keep the docs current: with every change, update `README.md` (setup, how to play,
  layout) and `AGENTS.md` (commands, conventions, architecture, testing) in the same task.

## Architecture

- `game.py`: `Game` owns the loop (`handle_events` -> `update(dt)` -> `draw`) and a
  `State` machine: `PLAYING` (60 s round) -> `ROUND_OVER` (final score, 10 s) ->
  `HIGHSCORES` (click starts the next round).
- `duck.py`: `Duck` sprite with a random distance (`scale`) that sets its size, speed
  and `points`; pixel-mask hit test; falls when shot. One duck flies at a time.
- `crosshair.py`: crosshair as the system color cursor (hotspot on the red dot).
- `hud.py`: `render_text` (shadowed text), cached `Label`, `Hud` (score + timer).
- `screens.py`: `RoundOverScreen`, `HighScoreScreen` overlays.
- `highscores.py`: `HighScoreList`, top 10 persisted to `settings.HIGHSCORES_FILE`
  (`~/.duck-attack/highscores.json`); entries are identified by round start timestamp.
- `sounds.py`: `AmbientSounds` plays random duck calls; silent without an audio device.

## Testing

- `tests/conftest.py` redirects `settings.HIGHSCORES_FILE` to a temp path for every
  test; never write to the real high-score file from tests.
- Tests that create a `Game` should call `pygame.quit()` at the end.

## Git

- Never commit or push. The maintainer commits and pushes manually; leave changes in the
  working tree and don't offer to commit.
