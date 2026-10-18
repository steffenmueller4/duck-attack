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

Aim with the crosshair and click ducks to shoot them; every shot goes bang. A round lasts
30 seconds; the time left is shown top-left (red in the last 10 seconds), your score
top-right.

Ducks fly in at random distances. Close (big) ducks are worth 10 points; farther (smaller)
ones are worth more, up to 30. Duck calls play in the background from time to time.

After the round, your score is shown for 10 seconds, followed by the top-10 high-score
list (your round is highlighted). Click to start the next round.

High scores are saved in `~/.duck-attack/highscores.json`. Delete the file to reset them.

Round length, points, duck size/speed, sound volume and more can be tuned in
`src/duck_attack/settings.py`.

## Develop

```sh
pytest               # tests (run headless)
ruff check .         # lint
ruff format .        # format
```

## Layout

```
src/duck_attack/
  __main__.py        entry point
  game.py            main loop and round flow (playing -> round over -> high scores)
  settings.py        tunable constants
  duck.py            duck sprite: flight, distance/size, hit test, points
  crosshair.py       crosshair mouse cursor
  hud.py             score and timer display, text rendering
  screens.py         round-over and high-score screens
  highscores.py      high-score list (JSON file)
  sounds.py          shot sound and ambient duck calls
  assets/images/     background, duck, crosshair
  assets/sounds/     shot sound and ambient duck calls
tests/               pytest tests
```
