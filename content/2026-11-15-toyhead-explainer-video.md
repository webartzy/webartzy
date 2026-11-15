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
Create 6 short vertical video clips (9:16, 1080x1920) of the man in my attached face sheet, talking to the camera. He SPEAKS the lines below out loud with natural lip movement, in English, in a calm, dry, slightly tired, deadpan voice, at an unhurried pace, with the pauses marked by "...". Record clean close-mic speech only: no background music, no sound effects, no subtitles, no captions, no on-screen text.

First make one still frame of the setup and show it to me. Only after I approve it, animate the clips.

PERSON: The man in the attached reference sheet (front, smiling, serious and side views of the same person). Keep his face, short black quiff hairstyle, full thick black beard, black round-rectangular glasses and skin tone exactly the same in every clip. Do not beautify or change his face. He wears a plain dark grey crew-neck sweater.

SETTING: He sits behind a wooden desk in a dark room at night. A warm gold desk lamp is the only light, softly lighting one side of his face. A laptop is open on the desk, its screen glow barely visible at the bottom of the frame. Behind him, out of focus, the edge of an unmade bed with a dark red blanket. Palette: ink black, bone white, deep blood red, candle gold. No blue or purple tint.

CAMERA: Close-up, chest-up, eye level, like a webcam selfie video, locked off. Identical framing, lighting, room and starting pose in all six clips so they cut together cleanly. No zooms, no camera moves.

PERFORMANCE: Relaxed, dry humour, speaking straight to camera. Small natural movements only: blinks, small nods, a tiny smirk, an eyebrow raise. No big gestures.

CLIPS (he says each line exactly as written):
1. (8s) A calm look into the camera, a small nod, a tiny smirk, then he says: "I built a monster that lives under your bed. He doesn't scare you... He tells you gothic bedtime stories."
2. (8s) He raises one finger as if counting, then a dry shrug and a half smile, and says: "First version: Claude Fable on its own. A flashlight, six stories, one sad monster. It worked... It also beeped."
3. (8s) He glances aside for a moment, then back to camera with a small amused smile, and says: "Then I plugged in the Eleven Labs M C P and gave him my voice. A clone of me, reading every story."
4. (8s) He counts quickly on his fingers, one eyebrow lifts at the end, and he says: "Twenty-one audio files, one take each. A creaking bed, a heartbeat, a lullaby... Even the captions follow his voice."
5. (4s) He tilts his head toward the left of the frame with a look that says "go ahead", and says: "Watch both."
6. (4s) He leans slightly toward the camera with a warm half smile, and says: "Which one would you let under your bed?"
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
