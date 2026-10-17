# AGENTS.md

Duck Attack is a small Moorhuhn-style shooter built with Pygame (`pygame-ce`, imported as `pygame`).

## Commands

- Install: `pip install -r requirements-dev.txt` (editable install + dev tools)
- Run: `python -m duck_attack`
- Test: `pytest` (headless via `SDL_VIDEODRIVER=dummy`, set in `tests/conftest.py`)
- Lint/format: `ruff check .` and `ruff format .`

## Conventions

- Source lives in `src/duck_attack/`, tests in `tests/`.
- Game-wide constants go in `settings.py`; the main loop is `Game` in `game.py`.
- Images live in `src/duck_attack/assets/images/`.
- Dependency ranges are declared in `pyproject.toml`; exact pins in `requirements*.txt`.
  Update both when adding a dependency.
- Keep `ruff check` and `pytest` passing before committing.
