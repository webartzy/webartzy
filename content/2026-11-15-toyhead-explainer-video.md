# 🎬 Motion Content — `TOYHEAD EXPLAINS: Fable alone vs Fable + ElevenLabs MCP`

> فرمت: پست X، عمودی `1080×1920` (مربعی هم جواب می‌ده)
> مدت: **~40 ثانیه** = 5 کلیپ حرف‌زدن (~30s) + 8 تا 10 ثانیه split-screen قبل/بعد
> قهرمان: خود Toyhead، پشت لپ‌تاپ، زیر تخت، دارد توضیح می‌دهد چطور ساخته شده

## لینک‌ها

| | لینک |
|---|---|
| قبل: فقط Fable (پیکسل‌آرت، بوق مرورگر) | https://claude.ai/artifact/MfYZCVVkDiYvSruLE2nnVf |
| بعد: Fable + ElevenLabs MCP | https://claude.ai/artifact/CNcKQNqLd3Tzu6azgxWDAo |

## حقایقی که در اسکریپت استفاده شده (همه واقعی‌اند)

- نسخه‌ی اول فقط با Fable ساخته شد و فقط بوق ساده‌ی مرورگر داشت.
- نسخه‌ی دوم با ElevenLabs MCP: صدای کلون‌شده‌ی خودت (voice_id `C6DTcqmFMHENR2zZdndE`)، 8 افکت، 1 لالایی. روی هم **21 فایل، هر کدام یک برداشت**.
- بریف هر دو یکی بود.
- توجه: نسخه‌ی «بعد» علاوه بر صدا، طراحی نقاشی‌شده و شش شب هم دارد. اسکریپت فقط می‌گوید «صدا اضافه شد»، که درست است. اگر می‌خواهی ادعا کنی «فقط صدا فرق دارد»، باید نسخه‌ی پیکسلی + صدا را جدا منتشر کنیم (commit `a962f6b`).

## اسکریپت

هر خط یک کلیپ جدا است، چون هر کلیپ جداگانه صدا و lipsync می‌گیرد. تگ‌های داخل کروشه فقط برای ElevenLabs هستند و گفته نمی‌شوند.

| کلیپ | زمان | دیالوگ | حرکت Toyhead | متن روی تصویر (موشن‌دیزاین) |
|---|---|---|---|---|
| C1 | 0 → 7s | `[deep voice] [slowly] [dry] Hello. I'm Toyhead. I live under your bed. I tell stories. [pause] Nobody asked me to be scary.` | با یک دست تنبل دست تکان می‌دهد، نیم‌لبخند، پلک آهسته روی «scary» | `TOYHEAD` |
| C2 | 7 → 14s | `[deep voice] [slowly] [dry] First, they built me with Fable alone. I looked wonderful. [short pause] I made small, polite beeps.` | به صفحه‌ی لپ‌تاپ نگاه می‌کند، بدون حالت، شانه‌ی خسته | `v1 · Fable alone` |
| C3 | 14 → 20s | `[deep voice] [slowly] [dry] Then they plugged in the ElevenLabs MCP. Same brief. [pause] Now I have a voice.` | ابروها کمی بالا، انگار از صدای خودش تعجب کرده، لبخند ملایم | `v2 · + ElevenLabs MCP` |
| C4 | 20 → 28s | `[deep voice] [slowly] [dry] The voice is borrowed. Twenty-one sounds, one take each. The bed creaks. [short pause] A music box plays. [pause] It isn't mine.` | سر کج، یک نگاه به پشت‌سر به تاریکی زیر تخت، یک برق طلایی کوچک، بعد برمی‌گردد معصوم | `21 sounds · 1 take each` |
| C5 | 28 → 30s | `[deep voice] [slowly] [dry] Watch both.` | کمی به دوربین نزدیک می‌شود، یک انگشت بالا | — |
| ✂ | 30 → 40s | *(split-screen: v1 چپ، v2 راست، با صدای خود بازی؛ تو ضبط می‌کنی)* | | `Fable alone` / `+ ElevenLabs MCP` |
| C6 | 40 → 46s | `[deep voice] [slowly] [softly] Then tell me which one you'd let under your bed. [pause] Goodnight.` | لبخند خسته، پلک آهسته، روی «Goodnight» آرام به تاریکی زیر تخت عقب می‌رود | `which one would you let under your bed?` |

اگر کل ویدیو باید دقیقاً 40 ثانیه باشد، split-screen را 5 تا 6 ثانیه کن.

## پرامپت برای Agent در Google Flow

اول شیت شخصیت را در بخش Characters با نام `Toyhead` آپلود کن، بعد این را بفرست:

```
Create 6 short vertical video clips (9:16, 1080x1920), each at most 8 seconds. Do NOT generate any dialogue, voice or music audio: I will add the voice later with ElevenLabs lip-sync. The mouth should still move naturally as if he is speaking calmly to the camera.

First make one still frame of the setup and show it to me. Only after I approve it, animate the clips.

CHARACTER: Toyhead, exactly as in my character sheet (Characters > Toyhead). Messy dark yarn-like hair, heavy drooping eyelids over big amber eyes, a small stitched seam on the forehead, freckles, a striped pyjama shirt under a dark red velvet waistcoat with small gold buttons. Keep his face, proportions and outfit identical in every clip. Handcrafted stop-motion puppet look, like the sheet.

SETTING: A dark bedroom at night, camera at floor level. Toyhead sits half out from under a bed, behind an open laptop resting on the floorboards, as if recording a selfie video. The laptop screen is the only light on his face: soft warm white, no blue or purple tint. A small candle glows gold far behind him. Deep black shadow under the bed. Palette only: ink black, bone white, one dark blood red, candle gold.

CAMERA: Fixed selfie-style framing, chest-up, from the laptop webcam position, slightly low angle. Identical framing, lighting, room and starting pose in all six clips so they cut together cleanly. No zooms, no camera moves.

PERFORMANCE: Dry, gentle, a little sad, a little funny. Small movements only: slow blinks, head tilts, a tired shrug. No jump scares, no gore, no sudden movements.

CLIPS:
1. (7s) Lazy one-handed wave, half smile, slow blink at the end.
2. (7s) Glances at the laptop screen, deadpan, small tired shrug, looks back at camera.
3. (6s) Eyebrows lift a little, as if surprised by his own voice, then a gentle smile.
4. (8s) Tilts his head, glances over his shoulder at the dark under the bed where a tiny gold glint appears, then turns back innocently.
5. (4s) Leans slightly toward the camera and raises one finger, then lowers it.
6. (6s) Soft tired smile, slow blink, then slowly slides back a little into the dark under the bed. The laptop light stays on.
```

## ترتیب کار

1. اسکریپت بالا را تأیید یا ویرایش کن.
2. Flow Agent، 6 کلیپ می‌سازد. خروجی‌ها را بدون صدا نگه دار.
3. من با ElevenLabs MCP، 6 صدا با voice_id خودت می‌سازم (قبلش با `estimate_only` قیمت را نشان می‌دهم) و زمان‌بندی کلمه‌ها را می‌گیرم.
4. کلیپ‌ها را در flow ElevenLabs آپلود می‌کنی (لینکش را بعد از تأیید می‌دهم) یا لینک مستقیم می‌دهی؛ من lipsync را اجرا می‌کنم (`sync-lipsync-v3`).
5. چسباندن کلیپ‌ها، split-screen و زیرنویس با ffmpeg؛ موشن‌دیزاین متن‌ها بعد از آن.

## کپشن X (پیش‌نویس)

```
I built a character that lives under your bed and tells gothic stories.

v1: Fable alone. Beeps.
v2: + ElevenLabs MCP. A voice, a creaking bed, a music box in the dark.

Which one would you let under your bed?
```

اگر با ElevenLabs رابطه‌ی همکاری یا حمایت داری (ambassador، کردیت رایگان و…)، آخر کپشن بنویس. این پست را تبلیغ حساب می‌کنند.
