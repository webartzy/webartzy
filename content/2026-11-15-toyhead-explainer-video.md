# 🎬 Motion Content — `I BUILT A MONSTER UNDER THE BED: Fable alone vs Fable + ElevenLabs MCP`

> فرمت: پست X، عمودی `1080×1920`
> مدت: **~40 ثانیه** = 6 کلیپ حرف‌زدن (~34s) + 5 تا 6 ثانیه split-screen قبل/بعد
> قهرمان: **خودت**، پشت میز، نمای نزدیک، دارد توضیح می‌دهد چه ساخته (نه Toyhead)
> این برنامه جایگزین نسخه‌ی قبلی (Toyhead به‌عنوان مجری) است

## لینک‌ها

| | لینک |
|---|---|
| قبل: فقط Fable (پیکسل‌آرت، بوق مرورگر) | https://claude.ai/artifact/MfYZCVVkDiYvSruLE2nnVf |
| بعد: Fable + ElevenLabs MCP | https://claude.ai/artifact/CNcKQNqLd3Tzu6azgxWDAo |

هر دو لینک خصوصی‌اند؛ قبل از پست از منوی Share باز کن.

## حقایقی که در اسکریپت استفاده شده (همه واقعی‌اند)

- نسخه‌ی اول فقط با Fable ساخته شد: چراغ‌قوه، 6 داستان، فقط بوق ساده‌ی مرورگر.
- نسخه‌ی دوم با ElevenLabs MCP: صدای کلون‌شده‌ی خودت (voice_id `C6DTcqmFMHENR2zZdndE`)، 8 افکت، 1 لالایی. روی هم **21 فایل صوتی، هر کدام یک برداشت، 3٬511 کردیت**.
- زیرنویس بازی با زمان‌بندی کلمه‌ها از speech-to-text خود ElevenLabs هماهنگ می‌شود (0 کردیت).
- توجه: نسخه‌ی «بعد» علاوه بر صدا، طراحی نقاشی‌شده و شش شب هم دارد. اسکریپت فقط ادعای صدا می‌کند. اگر می‌خواهی ادعا کنی «فقط صدا فرق دارد»، باید نسخه‌ی پیکسلی + صدا را جدا منتشر کنیم (commit `a962f6b`).

## اسکریپت

هر خط یک کلیپ جدا است.

| کلیپ | زمان | دیالوگ | حرکت | متن روی تصویر |
|---|---|---|---|---|
| C1 | 0 → 7s | `[calm] I built a monster that lives under your bed. He doesn't scare you. [short pause] He tells you gothic bedtime stories.` | نگاه آرام به دوربین، تکان کوچک سر روی «bed»، یک پوزخند ریز | `Under the Bed` |
| C2 | 7 → 14s | `First version: Claude Fable on its own. A flashlight, six stories, one sad monster. It worked. [short pause] It also beeped.` | یک انگشت بالا انگار می‌شمارد، شانه‌ی خشک، نیم‌لبخند | `v1 · Fable alone` |
| C3 | 14 → 21s | `Then I plugged in the ElevenLabs MCP and gave him my voice. A clone of me, reading every story.` | یک لحظه به کنار نگاه می‌کند، برمی‌گردد با لبخند سرگرم‌شده | `v2 · + ElevenLabs MCP` |
| C4 | 21 → 28s | `Twenty-one audio files, one take each. A creaking bed, a heartbeat, a lullaby. [short pause] Even the captions follow his voice.` | سریع روی انگشت‌ها می‌شمارد، آخرش یک ابرو بالا | `21 files · 1 take each` |
| C5 | 28 → 30s | `Watch both.` | سر را به سمت چپ کادر کج می‌کند با نگاهی که یعنی «بفرما» | — |
| ✂ | 30 → 36s | *(split-screen: v1 چپ، v2 راست، با صدای خود بازی؛ تو ضبط می‌کنی)* | | `Fable alone` / `+ ElevenLabs MCP` |
| C6 | 36 → 40s | `[warmly] Which one would you let under your bed?` | کمی به دوربین نزدیک می‌شود، نیم‌لبخند گرم، یک مکث در تماس چشمی | — |

تگ‌های کروشه‌ای فقط برای ساخت صدا با TTS بودند. چون صدا را Flow می‌گوید و تو جایگزین می‌کنی، لازم نیستند.

## پرامپت برای Agent در Google Flow

Flow خودش حرف می‌زند تا حس و ریتم طبیعی باشد؛ بعد صدا را خودت با ElevenLabs جایگزین می‌کنی. اول شیت چهره را در Characters آپلود کن، بعد این را بفرست:

```
Update: keep the side camera angles of the last still, but change his outfit and make everything look more natural and human, not like a polished AI render. NEVER film him straight on from the front. Every shot is from the side, with a clear angle, lens and light as described below.

Create 6 short vertical video clips (9:16, 1080x1920) of the man in my attached face sheet. He SPEAKS the lines below out loud with natural lip movement, in English, in a calm, dry, slightly tired, deadpan voice, at an unhurried pace, with the pauses marked by "...". Record clean close-mic speech only: no background music, no sound effects, no subtitles, no captions, no on-screen text.

First make one still of the first shot and show it to me. Only after I approve it, animate the clips.

PERSON: The man in the attached reference sheet (front, smiling, serious, three-quarter and profile views of the same person). Keep his face, short black quiff hairstyle, full thick black beard, black round-rectangular glasses and skin tone exactly the same in every clip. Do not beautify or change his face. He wears a simple gothic outfit: a plain matte black high-collar long-sleeve knit top, slightly worn, no logos, no patterns, no jewellery.

HUMAN LOOK: It must look like real phone footage of a real person, not a polished AI render. Natural skin with visible pores, fine lines, slight oiliness and uneven tone; no airbrushing, no beauty filter, no plastic or waxy skin. Beard hairs and a few flyaway strands of hair slightly out of place. Slightly asymmetrical, imperfect expressions. Shot like a modern phone camera in low light: natural grain, slight softness, real motion blur, 24 fps, a very subtle natural handheld sway even on the locked-off shots. Natural breathing, irregular blinks, a small swallow, a tiny hesitation before a line. Realistic hands with exactly five fingers each.

ROOM MAP (keep identical in every shot): He sits at a wooden desk. An open laptop faces him, its screen glowing softly on his face. A warm gold desk lamp stands on his right side. Behind him, deep in the dark, is the edge of an unmade bed with a dark red blanket. Night. Palette: ink black, bone white, deep blood red, candle gold. No blue or purple tint.

LIGHT: Low-key and moody. The gold lamp is the key light and makes a warm rim along his beard and nose. The laptop adds a soft fill on his face. Deep black shadows everywhere else. Film grain, shallow depth of field.

PERFORMANCE: Relaxed, dry humour, conversational like talking to a friend, never like an announcer or a presenter. Small natural movements only: blinks, small nods, a tiny smirk, an eyebrow raise. No big gestures. He looks at the laptop most of the time and turns to the camera only where written. Do not add or change any word of the lines.

CLIPS (he says each line exactly as written):
1. (8s) CAMERA: three-quarter view from his front-left at 45 degrees, 50mm, medium close-up, slow dolly-in. He is looking at the laptop, then turns his head to the camera, a tiny smirk, and says: "I built a monster that lives under your bed. He doesn't scare you... He tells you gothic bedtime stories."
2. (8s) CAMERA: full profile from his right, 85mm close-up, locked off. The gold lamp is a blurred glow in the foreground, the laptop light on his face. He looks at the screen, raises one finger as if counting, a dry shrug, and says: "First version: Claude Fable on its own. A flashlight, six stories, one sad monster. It worked... It also beeped."
3. (8s) CAMERA: low angle from desk level, front-left at 30 degrees, 35mm, the edge of the laptop blurred in the foreground, locked off. He glances aside for a moment, then to the camera with a small amused smile, and says: "Then I plugged in the Eleven Labs M C P and gave him my voice. A clone of me, reading every story."
4. (8s) CAMERA: tight three-quarter close-up from his left, 85mm, locked off, his fingers visible at the bottom of the frame. He counts quickly on his fingers, one eyebrow lifts at the end, and he says: "Twenty-one audio files, one take each. A creaking bed, a heartbeat, a lullaby... Even the captions follow his voice."
5. (4s) CAMERA: wide side-on shot from his left, 35mm, the whole desk, the laptop, him and the dark bed behind, locked off. He turns his head to the camera and tilts it toward the left of the frame with a look that says "go ahead", and says: "Watch both."
6. (4s) CAMERA: three-quarter view from his right, 50mm, slow dolly-in to a medium close-up. He looks at the camera with a warm half smile, holds eye contact for a beat at the end, and says: "Which one would you let under your bed?"
```

- «Eleven Labs M C P» با فاصله نوشته شده تا Flow درست تلفظ کند. روی تصویر همان `ElevenLabs MCP` می‌ماند.
- Flow کلیپ‌ها را 4، 6 یا 8 ثانیه می‌سازد. کلیپ‌های 8 ثانیه‌ای را موقع تدوین کوتاه کن.
- اگر Flow عکس چهره را رد کرد: Frames to video با عکس روبه‌رو به‌عنوان فریم اول، یا کلیپ‌ها را خودت فیلم بگیر.

## جایگزینی صدا با ElevenLabs

ساده‌ترین راه Voice Changer (speech to speech) است، نه lipsync: صدای هر کلیپ را با صدای کلون‌شده‌ی خودت جایگزین کن. زمان‌بندی، مکث‌ها و حس همان صدای Flow می‌ماند، پس دهان هم همچنان جور است. این‌ها را رعایت کن:

- Voice Changer کلمه‌ها و تلفظ را عوض نمی‌کند، فقط صدا را. پس متن را قبل از ساخت کلیپ‌ها نهایی کن.
- اگر صدای Flow نویز اتاق یا موسیقی دارد، اول Voice Isolator.
- افکت‌ها و موسیقی بازی در split-screen با صدای خود بازی می‌آیند.

## ترتیب کار

1. اسکریپت بالا را تأیید یا ویرایش کن.
2. Flow Agent، 6 کلیپ با صدا می‌سازد.
3. صدای هر کلیپ را با Voice Changer ElevenLabs و صدای خودت جایگزین کن.
4. چسباندن، split-screen و زیرنویس با ffmpeg (زمان کلمه‌ها را می‌توانم از speech-to-text بگیرم)؛ بعد موشن‌دیزاین متن‌ها.

## پست X (پیش‌نویس)

```
I built a monster that lives under your bed and tells gothic bedtime stories.

v1: Claude Fable on its own. It worked. It beeped.
v2: + ElevenLabs MCP. My cloned voice, 21 audio files, one take each.

Watch both.

(AI-generated video of me. Voice cloned with ElevenLabs.)
```

ریپلای اول (توضیح اینکه چه ساخته):

```
What the ElevenLabs MCP made, in one session:

• 12 voice lines in my cloned voice (6 stories, 3 intros, 3 goodnights)
• 8 sound effects: bed creak, slide out and back, flashlight click, candle, music box, wind, heartbeat
• 1 looping 30s dark lullaby
• word timings so the captions follow his voice

3,511 credits. The game has a BEEPS / ELEVENLABS switch so you can hear the difference.
```

ریپلای دوم: لینک بازی (بعد از Share).

اگر با ElevenLabs رابطه‌ی همکاری یا حمایت داری (ambassador، کردیت رایگان و…)، آخر کپشن بنویس. این پست را تبلیغ حساب می‌کنند.
