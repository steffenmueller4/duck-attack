# 0001: Angry ducks

- **Status:** Done
- **Affects:** new angry-ducks.md, round.md, presentation.md, README.md (spec table)

## Motivation

The single flying duck gets predictable after a few rounds. Every now and then an angry
duck pops up at a random spot on the screen and stays only briefly. The player has to
react quickly to grab its bonus points. That adds surprise and rewards fast aiming,
without making a round harder for players who ignore it.

## Requirement changes

### New

A new capability spec `angry-ducks.md`, with the ID prefix `ANGRY`:

**ANGRY-1:** During a round, an angry duck must appear after a random delay between
`ANGRY_DUCK_MIN_DELAY` (5 s) and `ANGRY_DUCK_MAX_DELAY` (15 s). The delay is counted
from the start of the round, and after that from the moment the previous angry duck is
gone (it was shot, or it vanished). At most one angry duck is on screen at a time, and
at most `ANGRY_DUCK_MAX_PER_ROUND` (2) appear per round.
- *Scenario:* Given a round has just started, when less than `ANGRY_DUCK_MIN_DELAY` has
  passed, then no angry duck is on screen.
- *Scenario:* Given an angry duck is on screen, when the next delay would run out, then
  no second angry duck appears.

**ANGRY-2:** An angry duck must use the image `ANGRY_DUCK_IMAGE`
(`assets/images/angry_duck.png`), `ANGRY_DUCK_WIDTH` (120 px) wide, keeping the image's
aspect ratio. Unlike flying ducks, it has no random distance.

**ANGRY-3:** An angry duck must appear at a random position where its whole image is on
screen. It must stay at least `ANGRY_DUCK_MARGIN` (80 px) away from the top edge, so it
never covers the score or timer. It may appear anywhere else, including over the ground
and over the flying duck.

**ANGRY-4:** An angry duck must pop up: it grows from nothing to full size within
`ANGRY_DUCK_POP_TIME` (0.15 s), and stays in place. If it isn't shot within
`ANGRY_DUCK_LIFETIME` (1.5 s, counted from when it appeared), it vanishes. Letting it
vanish costs no points.

**ANGRY-5:** A shot must only hit an angry duck on a non-transparent pixel of its image,
also while it is still growing. Clicks on the transparent area around it are misses
(unless they hit the flying duck, see ROUND-3).

**ANGRY-6:** A hit on an angry duck must add `ANGRY_DUCK_POINTS` (50) to the score. The
shot duck then turns upside down and falls like a shot flying duck (see DUCK-7), and
can't be hit again.

**ANGRY-7:** An angry duck must be drawn in front of all flying ducks.

### Changed

- **ROUND-3:** ~~A shot must hit at most one duck: the closest (drawn on top) flying
  duck whose visible pixels are under the crosshair's hotspot.~~ → A shot must hit at
  most one duck: the top-most duck whose visible pixels are under the crosshair's
  hotspot. An angry duck that isn't falling comes first (see ANGRY-7), then flying
  ducks from closest to farthest.
  - *Scenario:* Given an angry duck overlaps the flying duck, when the player shoots at
    the overlap, then only the angry duck is hit and the flying duck keeps flying.
- **ROUND-4:** ~~A hit must add the duck's points (see DUCK-3) to the score.~~ → A hit
  must add the duck's points to the score: DUCK-3 for flying ducks, ANGRY-6 for angry
  ducks.
- **ROUND-7:** ~~the ducks disappear~~ → the ducks, including any angry duck,
  disappear, and no new angry duck appears.
- **PRES-4:** ~~(duck, crosshair)~~ → (duck, angry duck, crosshair)

ROUND-2 stays as it is: angry ducks come on top of the one flying duck and don't affect
when the next flying duck is sent in.

### Removed

- none

## New settings

| Setting | Default |
| --- | --- |
| `ANGRY_DUCK_IMAGE` | `ASSETS_DIR / "images" / "angry_duck.png"` |
| `ANGRY_DUCK_WIDTH` | 120 (px) |
| `ANGRY_DUCK_MIN_DELAY` | 5.0 (s) |
| `ANGRY_DUCK_MAX_DELAY` | 15.0 (s) |
| `ANGRY_DUCK_MAX_PER_ROUND` | 2 |
| `ANGRY_DUCK_POP_TIME` | 0.15 (s) |
| `ANGRY_DUCK_LIFETIME` | 1.5 (s) |
| `ANGRY_DUCK_MARGIN` | 80 (px from the top edge) |
| `ANGRY_DUCK_POINTS` | 50 |

With a 30 s round, these defaults give 1 or 2 angry ducks per round (2 at most).

## Open questions

- Are 50 points right? A far-away flying duck is worth 30, so 50 makes the angry duck
  clearly the best target without dominating the score.
- Is 1.5 s on screen fair? It could also shrink back out instead of vanishing at once.
- Should the angry duck have its own sound when it appears (an angry quack)? That would
  need a new sound file under `assets/sounds/`.
- Should letting an angry duck get away cost points? This proposal says no.

## Out of scope

- A floating "+50" text where the duck was hit.
- More than one angry duck at a time, or angry ducks that move.
- Showing angry-duck hits separately on the round-over or high-score screens.
