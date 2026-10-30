# Audio

## Purpose

Sound gives feedback on every shot, announces angry ducks and makes the scene feel
alive.

## Requirements

**AUDIO-1:** Every shot during a round (hit or miss) must play `SHOT_SOUND` at
`SHOT_VOLUME` (0.8). Clicks outside a round play no shot sound.
Verified by: `test_every_shot_plays_a_sound_hit_or_miss`,
`test_no_shot_sound_after_round_is_over`, `test_no_shooting_during_name_entry`

**AUDIO-2:** Ambient duck calls from `AMBIENT_SOUNDS` must play at random intervals of
`AMBIENT_MIN_DELAY` to `AMBIENT_MAX_DELAY` (2–7 s) at `AMBIENT_VOLUME` (0.6), on every
screen.
Verified by: `test_plays_after_delay_and_reschedules`

**AUDIO-3:** When a sound is picked at random from a set, the same clip must not play
twice in a row (unless the set has only one clip).
Verified by: `test_never_repeats_the_same_sound_twice_in_a_row`

**AUDIO-4:** Without an audio device the game must run silently instead of failing.
Verified by: `test_silent_without_audio_device`

**AUDIO-5:** All sound files must load.
Verified by: `test_all_sounds_load`

**AUDIO-6:** When an angry duck appears (see [angry-ducks.md](angry-ducks.md), ANGRY-1),
`ANGRY_DUCK_SOUND` must start playing at `ANGRY_DUCK_VOLUME` (0.7). As soon as that duck
is gone (it was shot, it vanished, or the round ended), the sound must fade out over
`ANGRY_DUCK_SOUND_FADE` (0.2 s) instead of playing to the end.
- *Scenario:* Given an angry duck has just appeared, when the player shoots it, then its
  quacking fades out within `ANGRY_DUCK_SOUND_FADE`.
- *Scenario:* Given an angry duck is quacking, when it vanishes unshot after
  `ANGRY_DUCK_LIFETIME`, then its quacking fades out.
- *Scenario:* Given an angry duck is quacking, when the round ends, then its quacking
  fades out.

Verified by: `test_angry_duck_quacks_when_it_appears`,
`test_angry_duck_sound_fades_out_when_it_is_shot`,
`test_angry_duck_sound_fades_out_when_it_vanishes`,
`test_angry_duck_sound_fades_out_when_round_ends`
