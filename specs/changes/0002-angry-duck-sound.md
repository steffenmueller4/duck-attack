# 0002: Angry duck sound

- **Status:** Done
- **Affects:** audio.md, angry-ducks.md (cross-reference only)

## Motivation

An angry duck appears silently at a random spot and is easy to miss, especially when the
player is focused on the flying duck. An angry quacking sound tells the player that an
angry duck has appeared and adds to its character. The clip (`angry_duck.mp3`) is about
5 s of steady quacking, while an angry duck is on screen for only 1.5 s. The sound
should therefore end with the duck, fading out instead of cutting off with a click.

## Requirement changes

### New

**AUDIO-6:** When an angry duck appears (see [angry-ducks.md](../angry-ducks.md),
ANGRY-1), `ANGRY_DUCK_SOUND` must start playing at `ANGRY_DUCK_VOLUME` (0.7). As soon as
that duck is gone (it was shot, it vanished, or the round ended), the sound must fade
out over `ANGRY_DUCK_SOUND_FADE` (0.2 s) instead of playing to the end.
- *Scenario:* Given an angry duck has just appeared, when the player shoots it, then its
  quacking fades out within `ANGRY_DUCK_SOUND_FADE`.
- *Scenario:* Given an angry duck is quacking, when it vanishes unshot after
  `ANGRY_DUCK_LIFETIME`, then its quacking fades out.
- *Scenario:* Given an angry duck is quacking, when the round ends, then its quacking
  fades out.

### Changed

- **AUDIO-5:** wording unchanged ("All sound files must load"); its test also checks
  `ANGRY_DUCK_SOUND` from now on.

AUDIO-4 (silent without an audio device) also applies to the new sound.

### Removed

- none

## New settings

| Setting | Default |
| --- | --- |
| `ANGRY_DUCK_SOUND` | `ASSETS_DIR / "sounds" / "angry_duck.mp3"` |
| `ANGRY_DUCK_VOLUME` | 0.7 (0.0 - 1.0; the clip is loud, so a bit below `SHOT_VOLUME`) |
| `ANGRY_DUCK_SOUND_FADE` | 0.2 (s) |

## Open questions

- none

## Out of scope

- A separate sound when an angry duck is hit (the shot sound already plays, AUDIO-1).
- Trimming or editing the sound file itself.
