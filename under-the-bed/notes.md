# Under the Bed — notes

- Artifact: https://claude.ai/artifact/CNcKQNqLd3Tzu6azgxWDAo
- Page: `under-the-bed/index.html` (single file, audio embedded as base64). Built from `src.html` by `build.py`.
- ElevenLabs flow (all generations live here): https://elevenlabs.io/app/flows/ViRedKmipfnjSXINXIa1
- Original downloads: `audio/*.mp3`. Smaller re-encodes used in the page: `build/*.mp3`.
- Word timings used for caption sync: `audio/timings.json` (from the ElevenLabs speech-to-text node, 0 credits).

## How a night works

There are six nights, one story each. Each night:

1. Shine the flashlight under the bed and tap the eyes; Toyhead slides out and offers up to three of the untold stories.
2. Pick a card. Before he tells it, find three things from that story in the room with the flashlight (the caption lists them). No new audio was generated for this; finding something plays the first seconds of `music-box.mp3`.
3. He tells the story while the three things and the room glow red, says goodnight and slides back.

Each night the flashlight is a little smaller. If you are stuck, the next thing glints after 9 to 22 seconds (longer on later nights). After the sixth story the nights can be started again.

The look is painted in code (soft gradients, no pixels) using only tints of ink, bone, blood red and candle gold.

## The switch

- **BEEPS** ("before"): browser oscillators only, captions revealed on a timer.
- **ELEVENLABS** ("after", default): the cloned voice, generated sound effects and music, captions lit from real word timings.

## Credits spent

| Group | Credits |
|---|---|
| Voice, 12 clips | 2,921 |
| Sound effects, 8 clips | 140 |
| Music, 1 clip | 450 |
| Word timings, 12 runs | 0 |
| **Total** | **3,511** |

One take each; nothing was regenerated.

## Voice — model `eleven_v4`, voice_id `C6DTcqmFMHENR2zZdndE` ("arash", cloned)

The bracketed words are delivery tags added after the request for a scarier read; the spoken words are the approved text, unchanged.

| File | Length | Credits | Prompt |
|---|---|---|---|
| intro1.mp3 | 7.0 s | 107 | `[deep voice] [slowly] [eerie] oh... you found me. [pause] don't scream, it's rude. [whispers] pick a story.` |
| intro2.mp3 | 6.4 s | 115 | `[deep voice] [slowly] [eerie] yes... i live down here. [short pause] the rent is reasonable. [whispers] choose one.` |
| intro3.mp3 | 7.5 s | 137 | `[deep voice] [slowly] [tired] i'm not here to scare you. [short pause] i'm too tired. [pause] [eerie] three stories. [whispers] take one.` |
| night1.mp3 | 5.0 s | 107 | `[deep voice] [slowly] [softly] that's all. [pause] close your eyes. [whispers] i'll keep watch on the dust.` |
| night2.mp3 | 6.3 s | 116 | `[deep voice] [slowly] [softly] goodnight. [pause] if something creaks, it's only me, [whispers] getting comfortable.` |
| night3.mp3 | 6.4 s | 109 | `[deep voice] [slowly] [softly] sleep now. [pause] i'll be underneath, as usual. [whispers] someone has to be.` |
| story-mirror.mp3 | 24.7 s | 369 | `[deep voice] [slowly] [eerie] a mirror in the hall kept every face it was shown. the vain, the tired, the ones only checking their teeth. it pressed them behind the glass like flowers. [pause] one night a girl looked in and saw nothing. [pause] the mirror had no face of its own. [short pause] so she drew one with her finger. [whispers] it is still smiling, crookedly.` |
| story-candle.mp3 | 23.4 s | 368 | `[deep voice] [slowly] [eerie] a candle was afraid of the dark, which is awkward in a candle. every night it burned as hard as it could, and every night it grew a little shorter. [pause] at last it was only a puddle with a wick. [short pause] it went out. [long pause] and the dark, who had been waiting years to say so, whispered: [whispers] thank you for the company.` |
| story-musicbox.mp3 | 26.6 s | 391 | `[deep voice] [slowly] [eerie] every night at three, the music box played by itself. the family blamed the cat, then the pipes, then each other. the boy stayed up to catch the ghost. [pause] the lid opened. [pause] the little dancer turned once, looked at him, and yawned. [short pause] she was not haunted. she was practising. [whispers] the daytime, she explained, has far too many critics.` |
| story-ghosts.mp3 | 25.9 s | 370 | `[deep voice] [slowly] [eerie] a girl painted ghosts, because nobody else would sit still for her. pale ladies. a sailor, still dripping. a dog made of fog. she hung them in the cold corridor, and each morning one more frame was empty. [pause] she was not frightened. she had only wanted them to feel at home. [pause] [whispers] now someone always leaves the kettle warm.` |
| story-door.mp3 | 26.8 s | 369 | `[deep voice] [slowly] [eerie] at the top of the stairs stood a door with no room behind it. open it, and there was only wall. still, every night, someone knocked from the other side. politely. three times. [pause] one night the boy knocked back. [long pause] a pause. then a small voice said: [whispers] oh, good. i was starting to think i was the one who wasn't there.` |
| story-attic.mp3 | 24.2 s | 363 | `[deep voice] [slowly] [eerie] the last toy in the attic was a bear with one eye and no name. the others had been carried downstairs, loved, and lost. he waited forty years in the dust. [pause] then the hatch opened, and an old man climbed up, slowly. [short pause] he was not looking for a toy. [whispers] he was looking for the only one who remembered him small.` |

## Sound effects — model `eleven_text_to_sound_v2`

| File | Length | Loop | Prompt influence | Credits | Prompt |
|---|---|---|---|---|---|
| bed-creak.mp3 | 2.5 s | no | 0.5 | 8 | `Old wooden bed frame creaking slowly, one long strained groan, close-mic, quiet room` |
| slide-out.mp3 | 3 s | no | 0.5 | 10 | `Heavy cloth body dragging slowly across dusty wooden floorboards, close-mic, low scraping rustle` |
| slide-back.mp3 | 3 s | no | 0.5 | 10 | `Cloth body dragging away across wooden floorboards, receding, soft scraping rustle fading out` |
| flashlight-click.mp3 | 0.5 s | no | 0.6 | 2 | `Single small plastic flashlight switch click, dry, close-mic` |
| candle-flicker.mp3 | 5 s | yes | 0.5 | 17 | `Single candle flame fluttering in a draft, faint wick crackle, very quiet, close-mic` |
| music-box.mp3 | 12 s | no | 0.5 | 40 | `Old wind-up music box playing a slow eerie minor lullaby, slightly out of tune, delicate metal tines, mechanism ticking` |
| window-wind.mp3 | 10 s | yes | 0.5 | 33 | `Cold night wind moaning low through a gap in an old window frame, hollow, steady, no rain` |
| heartbeat.mp3 | 6 s | yes | 0.6 | 20 | `Slow heavy muffled heartbeat, deep low thump, steady, about 55 beats per minute` |

## Music — model `eleven_music_v2_5`, instrumental

| File | Length | Credits | Prompt |
|---|---|---|---|
| dark-lullaby.mp3 | 30 s | 450 | `Dark gothic lullaby, slow waltz time, celesta and music box melody over a low bowed cello drone, minor key, haunting, tender and sad, sparse, no drums, no vocals` |

The page loops it with a 1.5 s crossfade.

## Where each sound plays

- flashlight-click: turning the light on, and tapping anywhere that is not the eyes.
- bed-creak: when he is called, when he goes back, and now and then while he hides.
- slide-out / slide-back: his entrance and exit.
- window-wind and dark-lullaby: from the moment the flashlight is on.
- heartbeat and candle-flicker: under every story.
- music-box: only under "the music box at 3am".
