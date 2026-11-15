# BRIEF: build the final "Under the Bed" video for X

You are a Claude Code session on the user's Windows PC. You have local files, a shell, a browser, screen access and the ElevenLabs MCP connector. Build the finished video end to end. Work step by step, report after each step, and do not ask questions this brief already answers.

## 1. Deliverable

- One vertical MP4, 1080x1920, H.264 + AAC, 30 fps, about 40 s (38 to 44 s is fine), loudness about -14 LUFS, true peak below -1 dB.
- Burned-in word-synced captions and short motion-design text cards (section 7).
- Save it as `<WORKDIR>/final/under-the-bed-x.mp4` and tell me the full path.

## 2. Inputs

A. Six AI-generated talking clips of the user, made in Google Flow (side angles, dark room, desk, laptop, gold lamp). Ask the user for the folder path. Expected names: `C1.mp4` to `C6.mp4` (C1 to C4 about 8 s, C5 and C6 about 4 s). They contain Flow's own speech, which is to be replaced.

B. The game in two versions, as local HTML files from the repo `github.com/webartzy/webartzy`, branch `ccr-14353993-csabto`:

- BEFORE (Fable alone: pixel art, browser beeps): `under-the-bed/v1/index.html`
- AFTER (Fable + ElevenLabs MCP: painted look, cloned voice, sound effects, music): `under-the-bed/index.html`

Open them from disk in Chrome (internet is needed only for Google Fonts). Private hosted copies, login needed: BEFORE https://claude.ai/artifact/MfYZCVVkDiYvSruLE2nnVf and AFTER https://claude.ai/artifact/CNcKQNqLd3Tzu6azgxWDAo. Audio only starts after the click on "switch on the flashlight".

C. ElevenLabs MCP: the user's own cloned voice, `voice_id` `C6DTcqmFMHENR2zZdndE` (named "arash"), model `eleven_v4`. The face in the clips is the user's own, as an AI-generated video.

## 3. Script (do not change a word)

Tags in square brackets are delivery directions for the voice model and are not spoken.

| Clip | Length | Text for the voice | On-screen text |
|---|---|---|---|
| C1 | 8 s | `[calm] [dry] I built a monster that lives under your bed. He doesn't scare you. [short pause] He tells you gothic bedtime stories.` | Under the Bed |
| C2 | 8 s | `[calm] [dry] First version: Claude Fable on its own. A flashlight, six stories, one sad monster. It worked. [short pause] It also beeped.` | v1 · Fable alone |
| C3 | 8 s | `[calm] [dry] Then I plugged in the Eleven Labs M C P and gave him my voice. A clone of me, reading every story.` | v2 · + ElevenLabs MCP |
| C4 | 8 s | `[calm] [dry] Twenty-one audio files, one take each. A creaking bed, a heartbeat, a lullaby. [short pause] Even the captions follow his voice.` | 21 files · 1 take each |
| C5 | 4 s | `[calm] [dry] Watch both.` | none |
| split | 6 s | no speech; the two game captures (section 6) | Fable alone / + ElevenLabs MCP |
| C6 | 4 s | `[warmly] Which one would you let under your bed?` | which one would you let under your bed? |

On screen the name is written `ElevenLabs MCP`. Only the voice text spells it "Eleven Labs M C P" so it is pronounced correctly.

## 4. Voice with ElevenLabs

1. `creative_create_flow` named "Final video voice".
2. For each clip call `creative_generate_speech` with `estimate_only: true` first. One take of all six lines should cost about 530 credits. Then generate with `generations_count: 1`, `model_id: eleven_v4`, the voice id above, and no voice settings.
3. Poll `creative_get_flow_run_status` until done. Never call a generation a second time to "retry": it starts and charges a second generation.
4. Download the MP3s and `ffprobe` their durations.
5. Each line must end at least 0.4 s before its clip ends. If a line is too long, do the first of these that works: regenerate that line once with fewer `[short pause]` tags; speed the audio up with `atempo` by at most 1.08; stretch the video clip by at most 1.10x.
6. Stop and ask the user before spending more than 1,500 credits in total.

## 5. Lipsync

1. Upload each clip with `creative_create_asset_upload` (name, mime type, exact byte size), PUT the bytes, then `creative_finalize_asset_upload` with the flow id. Connect the matching voice audio.
2. Use the lipsync model `sync-lipsync-v3` (fallback `veed-lipsync-v2`). I did not verify which node type it runs under: call `creative_get_flow_node_types`, `creative_get_model_guide` and `creative_get_model_schema` first, run `estimate_only`, and tell the user the price before running all six.
3. Check every result: extract frames at 25%, 50% and 75%. Face, glasses, beard, black top, necklace and cuff must stay the same, the mouth must move with the words, with no smeared mouth or teeth artifacts. If one clip is bad, redo only that clip once with the same input.
4. Fallback if lipsync is poor on the side shots (profile and wide: C2, C5): use Voice Changer (speech to speech) with the cloned voice on that clip's original Flow audio. It keeps the original mouth timing, so no lipsync is needed. Run Voice Isolator first if the Flow audio is noisy. Tell the user which clips used which method.

## 6. Record the game (BEFORE and AFTER)

Goal: one 10 to 12 s capture of each, with its own audio, 1080 px wide.

How to play it: open the page, click "switch on the flashlight", move the pointer into the dark gap under the bed (right half of the room, below the bed skirt) until two eyes appear, click the eyes. Toyhead slides out and says his intro line, then three story cards appear on the floor. Capture from the eye click until the cards are on the floor.

Audio: record the browser's own sound with OBS or another loopback capture. Playwright's `recordVideo` has no audio. If this PC cannot capture audio, tell the user exactly what to record by hand and stop at this step.

Make sure the AFTER capture is in ELEVENLABS mode (the switch at the top right, on by default) and that BEFORE has no ElevenLabs audio (BEEPS).

## 7. Edit

Timeline, with hard cuts: C1, C2, C3, C4, C5, SPLIT-SCREEN (6 s), C6. Trim each talking clip from 0.1 s before the speech starts to 0.35 s after it ends.

Split-screen: a vertical stack, BEFORE on top and AFTER below, each 1080 px wide, each labelled. Audio during the split: BEFORE's audio for the first 2 s, then a 0.3 s crossfade to AFTER's audio for the last 4 s.

Text cards: appear 0.3 s after the clip starts, stay 2.5 s, fade in and out over 0.2 s. Use the on-screen text from the table in section 3.

Style: ink black `#0B0B0D`, bone `#E8E2D6`, blood red `#8B0A1A` (accents only), candle gold `#C9A227` (key words). Fonts from Google Fonts: Pirata One for titles, IM Fell English italic for labels and captions. No neon, no purple, no blue. Keep all text at least 180 px from the bottom and 60 px from the sides.

Captions: burned in, word-synced, bone colour, about 56 px, bottom third, one short phrase at a time. Get the word timings by running the final speech through `creative_transcribe_audio` (it returns start and end for every word).

Audio mix: voice only on the talking clips, game audio only during the split-screen, short fades at the start and end, about -14 LUFS.

Tools: ffmpeg is fine (concat, xfade, overlay, drawtext or ASS subtitles). If a text card needs real motion, make it as an HTML or canvas animation and record it to video.

## 8. Verify and report

`ffprobe` the final file (resolution, fps, duration, audio streams). Extract 6 frames across the timeline and look at them. Check that the captions match the speech and that nothing is cut off at the edges. Report: the file path, the duration, the credits spent on every ElevenLabs call, and anything you changed from this brief.

## 9. Don'ts

- Do not change any word of the script and do not add music.
- Do not generate Toyhead or any other character. The presenter is the user.
- No blue, purple or neon.
- Do not repeat a paid generation without telling the user.
- The video is AI-generated. Never remove or hide the label in the post text below.

## 10. Post text (for reference, the user posts it)

    I built a monster that lives under your bed and tells gothic bedtime stories.

    v1: Claude Fable on its own. It worked. It beeped.
    v2: + ElevenLabs MCP. My cloned voice, 21 audio files, one take each.

    Watch both.

    (AI-generated video of me. Voice cloned with ElevenLabs.)

If the user has a partnership with ElevenLabs (ambassador, free credits), ask them whether to add a disclosure line.
