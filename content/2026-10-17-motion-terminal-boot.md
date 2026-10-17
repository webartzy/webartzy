# 🎬 Motion Content — `WEBARTZY_TERMINAL v3.0 // BOOT SEQUENCE`

> بر اساس محتوای امروز (آپدیت پروفایل ترمینالی v3.0)
> فرمت: **ریلز / استوری / پست X** — عمودی `1080×1920` (نسخه‌ی مربعی `1080×1080` هم جواب می‌ده)
> مدت: **~18 ثانیه** · لوپ‌پذیر (آخرش برمی‌گرده به کرسر چشمک‌زن)

---

## 🎨 استایل

| آیتم | مقدار |
|---|---|
| پس‌زمینه | مشکی `#0A0A0A` + اسکن‌لاین خیلی کم‌رنگ (opacity 4%) |
| متن اصلی | سبز ترمینال `#39FF14` |
| متن فرعی | خاکستری `#8A8A8A` |
| اکسنت | سفید `#FFFFFF` برای کلمات کلیدی |
| فونت | `JetBrains Mono` یا `IBM Plex Mono` |
| افکت‌ها | تایپ‌رایتر، کرسر `▌` چشمک‌زن، گلیچ کوتاه (2–3 فریم) سر کات‌ها |
| صدا | صدای کیبورد مکانیکی + یه بیس لوفای/سینث آروم، «بیپ» سر هر `> ` |

---

## 🎞️ سناریو صحنه‌به‌صحنه

### Scene 1 — Boot (0.0s → 2.5s)
- صفحه مشکی، فقط کرسر `▌` دو بار چشمک می‌زنه.
- بالا سمت چپ با تایپ‌رایتر:
  ```
  ● WEBARTZY_TERMINAL — SESSION ACTIVE          v3.0
  ```
- **موشن:** نقطه‌ی `●` پالس سبز می‌زنه (scale 1 → 1.3 → 1).

### Scene 2 — Hello (2.5s → 5.0s)
- وسط صفحه، درشت:
  ```
  Hello, welcome to my profile▌
  ```
- **موشن:** تایپ حرف‌به‌حرف (~0.05s برای هر کاراکتر)، بعد یه گلیچ RGB کوتاه.

### Scene 3 — Access Granted (5.0s → 7.5s)
  ```
  > access granted —  ONCHAIN BUILDER  //  VIBE CODER
  ```
- **موشن:** `access granted` اول قرمز چشمک می‌زنه، بعد سبز می‌شه ✅
- `ONCHAIN BUILDER` و `VIBE CODER` از دو طرف اسلاید می‌شن و وسط `//` به هم می‌رسن.

### Scene 4 — Loadout (7.5s → 11.0s)
  ```
  $ cat loadout.json
  [■■■□□□□□□] loading modules...
  ```
- سه کارت از پایین یکی‌یکی می‌آن بالا (stagger 0.3s):
  - `CHAIN & CONTRACTS` → Solidity · Ethers.js · EVM
  - `AI & VIBE CODING` → Claude · Cursor · Prompt-driven dev
  - `SHIP & SERVE` → Node.js · Next.js · Vercel
- پروگرس‌بار پر می‌شه و می‌نویسه:
  ```
  > 3/3 modules loaded — ready.▌
  ```

### Scene 5 — Active Files (11.0s → 14.5s)
- صفحه دو نیم می‌شه (split-screen، روی عمودی بالا/پایین):
  - **FILE_01 · ONCHAIN** — Onchain Art Drops → `status: active development` (نقطه‌ی زرد چشمک‌زن)
  - **FILE_02 · AI TOOLING** — Vibe-Coded Tools → `status: shipping` (نقطه‌ی سبز)
- **موشن:** هر کارت مثل پنجره‌ی ترمینال با یه «پاپ» باز می‌شه.

### Scene 6 — Outro / Loop (14.5s → 18.0s)
- همه‌چی گلیچ می‌خوره و پاک می‌شه، فقط این می‌مونه:
  ```
  compiling_brand.exe
  building in public since day one▌
  ```
- زیرش کوچیک: `@webartzy`
- **موشن:** کرسر چشمک می‌زنه → فریم آخر = فریم اول (لوپ بی‌نقص).

---

## ✍️ کپشن پیشنهادی

**نسخه‌ی انگلیسی (X / Instagram):**
```
> booting webartzy_terminal v3.0 ▌

onchain builder // vibe coder
3/3 modules loaded. ship first, polish later.

building in public since day one 🟢
```

**نسخه‌ی فارسی:**
```
> ترمینال webartzy نسخه ۳ بالا اومد ▌

آنچین می‌سازم، با AI وایب‌کد می‌زنم.
اول شیپ، بعد پولیش.

از روز اول، ساختن جلوی چشم همه 🟢
```

**هشتگ‌ها:**
`#onchain #vibecoding #buildinpublic #web3 #crypto #onchainart #claude #cursor #solidity #motiondesign`

---

## ⚡ نسخه‌ی کوتاه (۶ ثانیه — برای استوری/X)
1. `● SESSION ACTIVE v3.0` (1s)
2. `> ONCHAIN BUILDER // VIBE CODER` (2s)
3. `> 3/3 modules loaded — ready.` (1.5s)
4. `building in public since day one▌` (1.5s)

---

## 🛠️ نکته برای ساخت
- **After Effects:** افکت `Typewriter` از Text Animator Presets + `VC Color Vibrance` برای گلو.
- **CapCut:** Text → Animation → «Typewriter» + افکت «Glitch» یا «VHS».
- **کد (اگه بخوای وایب‌کدش کنی):** یه صفحه HTML با GSAP + ضبط با OBS — کاملاً هم‌سبک با برندت.
