# duck-attack
A small Pygame game similar to Moorhuhn.

## Setup

Requires Python 3.12+ (developed on 3.14). The repo's `.python-version` points at a
pyenv virtualenv named `duck_attack_venv`:

```sh
pyenv virtualenv 3.14.2 duck_attack_venv   # once; activates automatically in this folder
pip install -r requirements-dev.txt
```

Without pyenv, any virtualenv works:

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Run

```sh
duck-attack          # or: python -m duck_attack
```

Press `Esc` or close the window to quit.

## How to play

Click ducks to shoot them. A round lasts 60 seconds. Close ducks are worth 10 points;
farther (smaller) ones are worth more, up to 30. After the round, your score is shown,
followed by the high-score list. Click to start the next round.

High scores are saved in `~/.duck-attack/highscores.json`.

## Develop

```sh
pytest               # tests (run headless)
ruff check .         # lint
ruff format .        # format
```

## Layout

```
src/duck_attack/     game package (entry point: __main__.py)
  assets/images/     game graphics
tests/               pytest tests
```
