# Angry ducks

## Purpose

Every now and then an angry duck pops up at a random spot on the screen and stays only
briefly. Shooting it in time gives bonus points; letting it go costs nothing. Added by
[changes/0001-angry-ducks.md](changes/0001-angry-ducks.md).

## Requirements

**ANGRY-1:** During a round, an angry duck must appear after a random delay between
`ANGRY_DUCK_MIN_DELAY` (5 s) and `ANGRY_DUCK_MAX_DELAY` (15 s). The delay is counted
from the start of the round, and after that from the moment the previous angry duck is
gone (it was shot, or it vanished). At most one angry duck is on screen at a time (a
shot one that is still falling doesn't count), and at most `ANGRY_DUCK_MAX_PER_ROUND`
(2) appear per round.
- *Scenario:* Given a round has just started, when less than `ANGRY_DUCK_MIN_DELAY` has
  passed, then no angry duck is on screen.
- *Scenario:* Given an angry duck is on screen, when the next delay would run out, then
  no second angry duck appears.
- *Scenario:* Given two angry ducks have already appeared this round, when the delay
  runs out again, then no further angry duck appears.

Verified by: `test_angry_duck_appears_after_a_random_delay`,
`test_only_one_angry_duck_on_screen_at_a_time`,
`test_next_angry_duck_delay_counts_from_when_the_previous_is_gone`,
`test_at_most_max_angry_ducks_per_round`

**ANGRY-2:** An angry duck must use the image `ANGRY_DUCK_IMAGE`
(`assets/images/angry_duck.png`), `ANGRY_DUCK_WIDTH` (120 px) wide, keeping the image's
aspect ratio. Unlike flying ducks, it has no random distance.
Verified by: `test_angry_duck_image_is_scaled_and_transparent`

**ANGRY-3:** An angry duck must appear at a random position where its whole image is on
screen. It must stay at least `ANGRY_DUCK_MARGIN` (80 px) away from the top edge, so it
never covers the score or timer. It may appear anywhere else, including over the ground
and over the flying duck.
Verified by: `test_angry_duck_appears_fully_on_screen_below_the_hud`

**ANGRY-4:** An angry duck must pop up: it grows from nothing to full size within
`ANGRY_DUCK_POP_TIME` (0.15 s), and stays in place. If it isn't shot within
`ANGRY_DUCK_LIFETIME` (1.5 s, counted from when it appeared), it vanishes. Letting it
vanish costs no points.
Verified by: `test_angry_duck_pops_up_then_vanishes_unshot`

**ANGRY-5:** A shot must only hit an angry duck on a non-transparent pixel of its image,
also while it is still growing. Clicks on the transparent area around it are misses
(unless they hit the flying duck, see ROUND-3).
Verified by: `test_click_on_angry_duck_pixel_hits_also_while_growing`,
`test_click_on_angry_duck_transparent_corner_misses`

**ANGRY-6:** A hit on an angry duck must add `ANGRY_DUCK_POINTS` (50) to the score. The
shot duck then turns upside down and falls like a shot flying duck (see DUCK-7), and
can't be hit again.
Verified by: `test_angry_duck_hit_adds_its_points`,
`test_shot_angry_duck_falls_and_is_removed`

**ANGRY-7:** An angry duck must be drawn in front of all flying ducks.
Verified by: `test_angry_duck_in_front_of_flying_duck_is_hit_first` (hit order), manual
(drawing)
