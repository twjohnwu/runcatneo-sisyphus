# Sisyphus, Surfingphus, Rollingphus, Circusphus, Sisyphus-endless, Circusphus-endless & Rollingphus-endless — RunCat Neo runners

This repo holds seven custom runners for [RunCat Neo](https://runcat-dev.github.io/RunCatNeo/):
**Sisyphus** (below), **Surfingphus**, **Rollingphus**, **Circusphus**,
**Sisyphus-endless**, **Circusphus-endless** and **Rollingphus-endless** (further down). Each has its own frames, zip and preview.

## Sisyphus

![Sisyphus preview](sisyphus-preview.png)

Sisyphus pushes his boulder up the slope. At the top, the boulder rolls back
down, and he walks down after it to start again. The faster your CPU works,
the faster he pushes.

- 18 frames, 100 × 36 px, monochrome PNG with a transparent background
- Gallery tag: `fitness`

## Install

RunCat Neo requires macOS 26 or later.

### 1. Get the frames

Pick one:

- **From this repo:** download [`sisyphus-frames.zip`](sisyphus-frames.zip)
  and unzip it. You get a `sisyphus-frames/` folder with
  `sisyphus-frame-0.png` to `sisyphus-frame-17.png`.
- **From the Runner Gallery:** once it is listed there, open
  <https://runcat-dev.github.io/RunnerGallery/>, find **Sisyphus**, click
  **Download**, and unzip the file.
- **Clone:** `git clone https://github.com/twjohnwu/runcatneo-sisyphus.git`.
  The frames are already unzipped in `sisyphus-frames/`.

### 2. Add it to RunCat Neo

1. Open RunCat Neo's settings and go to the **Runner** tab.
2. Under **Custom Runners**, click **Add Custom Runner**.
3. In the **Custom Runner Editor**, set **Runner Name** to `Sisyphus` and
   choose **Monochrome**.
4. Click **Add Frame** and add the PNGs in order, from `sisyphus-frame-0.png`
   to `sisyphus-frame-17.png`. The order matters: frame 0 is the first
   frame of the animation.
5. Save, then select **Sisyphus** as your runner.

The labels above come from RunCat Neo's own UI text. Depending on your app
version, the exact path may differ a little.

## The story of Sisyphus

In Greek myth, Sisyphus was the king of Ephyra, the city later called Corinth.
He was clever and he was a cheat, and his worst offence was cheating death
itself, twice.

When Death (Thanatos) came for him, Sisyphus tricked Death into his own chains,
and for a while no one on earth could die. After the gods freed Death,
Sisyphus tried again. He told his wife not to give him the usual funeral
rites. Down in the underworld he complained that she had dishonoured him and
asked to go back to the living, just long enough to punish her. Once he was
home, he refused to return, and lived to an old age.

When he died at last, the gods gave him a punishment to match his cleverness.
He must roll a huge boulder up a hill. Every time he nears the top, the boulder
slips away and rolls back to the bottom, and he has to start again, forever.
Homer describes him at this task in the *Odyssey* (Book 11).

In 1942 Albert Camus took up the myth in *The Myth of Sisyphus*. He saw
Sisyphus as the figure of a person facing a life with no final meaning, and
ended with the line: *"One must imagine Sisyphus happy."*

That fits a menu-bar runner well. Your CPU never finishes its work either.

## Surfingphus — the variant that rides the boulder

![Surfingphus preview](surfingphus-preview.png)

Same boulder and the same push up the hill, on a slightly lower hilltop
so the rider fits. At the top, Surfingphus
climbs onto the boulder, and a surfboard pops into being across its top. He
surfs it back down standing on the board, arms out for balance, then the
board vanishes as he hops off at the bottom and starts pushing again.

- 18 frames, 100 × 36 px, monochrome PNG with a transparent background
- Frames 0–10 push the boulder up, as in Sisyphus (on the lower hill)

Install it the same way as Sisyphus (see [Install](#install)), with these
changes:

- **Frames:** [`surfingphus-frames.zip`](surfingphus-frames.zip) unzips to
  `surfingphus-frames/` with `surfingphus-frame-0.png` to
  `surfingphus-frame-17.png`.
- **Runner Name:** `Surfingphus`.
- **Frame order:** add the PNGs in order, from `surfingphus-frame-0.png` to
  `surfingphus-frame-17.png`.

## Rollingphus — the variant that rolls down with the boulder

![Rollingphus preview](rollingphus-preview.png)

Same boulder and the same steep hill as Sisyphus. Near the top the boulder
slips back and knocks Rollingphus flat, rolls over him, and he ends up stuck to
its rim. He spins round and round with it all the way down, then drops off
dazed at the bottom and starts pushing again.

- 18 frames, 100 × 36 px, monochrome PNG with a transparent background
- Frames 0–10 push the boulder up, exactly as in Sisyphus

Install it the same way as Sisyphus (see [Install](#install)), with these
changes:

- **Frames:** [`rollingphus-frames.zip`](rollingphus-frames.zip) unzips to
  `rollingphus-frames/` with `rollingphus-frame-0.png` to
  `rollingphus-frame-17.png`.
- **Runner Name:** `Rollingphus`.
- **Frame order:** add the PNGs in order, from `rollingphus-frame-0.png` to
  `rollingphus-frame-17.png`.

## Circusphus — the variant that ball-walks down on the boulder

![Circusphus preview](circusphus-preview.png)

Same boulder and the same lower hill as Surfingphus. At the top Circusphus
jumps up onto the boulder, knees tucked and arms raised, and stands on it with
no board. As it rolls back down he walks in place on top, feet stepping one
forward and one back and arms flailing for balance, like a circus clown on a
ball. At the bottom he hops off and starts pushing again.

- 18 frames, 100 × 36 px, monochrome PNG with a transparent background
- Frames 0–10 push the boulder up, as in Surfingphus (on the lower hill)

Install it the same way as Sisyphus (see [Install](#install)), with these
changes:

- **Frames:** [`circusphus-frames.zip`](circusphus-frames.zip) unzips to
  `circusphus-frames/` with `circusphus-frame-0.png` to
  `circusphus-frame-17.png`.
- **Runner Name:** `Circusphus`.
- **Frame order:** add the PNGs in order, from `circusphus-frame-0.png` to
  `circusphus-frame-17.png`.

## Sisyphus-endless — the close-up push loop that never ends

![Sisyphus-endless preview](sisyphus-endless-preview.png)

A close-up of Sisyphus pushing a bold boulder up a gentle slope without ever
reaching the top. The boulder is a lumpy rock with flat faces, a chipped corner and a
few small chips along one side; it turns 45 degrees per frame, so the rolling is
easy to see even at menu-bar size. The ground is a single thin line with a few large pebbles that scroll
past, and man, boulder and ground are always separated by a clear gap. He
pushes in surges: the boulder jumps forward about 2 px as he drives and settles
back a little, and his body bobs with it. The faster your CPU works, the faster
he pushes.

- 8 frames, 100 × 36 px, monochrome PNG with a transparent background
- The whole loop is the push: there is no roll-back

Install it the same way as Sisyphus (see [Install](#install)), with these
changes:

- **Frames:** [`sisyphus-endless-frames.zip`](sisyphus-endless-frames.zip)
  unzips to `sisyphus-endless-frames/` with `sisyphus-endless-frame-0.png` to
  `sisyphus-endless-frame-7.png`.
- **Runner Name:** `Sisyphus-endless`.
- **Frame order:** add the PNGs in order, from `sisyphus-endless-frame-0.png`
  to `sisyphus-endless-frame-7.png`.

## Circusphus-endless — the clown ride in the close-up style

![Circusphus-endless preview](circusphus-endless-preview.png)

Circusphus drawn in the Sisyphus-endless close-up style: the camera follows the
lumpy chipped boulder on a thin, steep ground line with pebbles. He pushes it up
(the ground scrolls left and the boulder turns forward), jumps up onto it, and
as it rolls back down he ball-walks on top like a circus clown, feet stepping
and arms flailing (the ground scrolls right and the boulder turns back). Once it
stops he hops off to the left and starts pushing again. The boulder is smaller
than in Sisyphus-endless so that he fits standing on top of it.

- 16 frames, 100 × 36 px, monochrome PNG with a transparent background
- Frames 0–7 push up, 8 jumps on, 9–14 ride down, 15 hops off

Install it the same way as Sisyphus (see [Install](#install)), with these
changes:

- **Frames:** [`circusphus-endless-frames.zip`](circusphus-endless-frames.zip)
  unzips to `circusphus-endless-frames/` with `circusphus-endless-frame-0.png`
  to `circusphus-endless-frame-15.png`.
- **Runner Name:** `Circusphus-endless`.
- **Frame order:** add the PNGs in order, from `circusphus-endless-frame-0.png`
  to `circusphus-endless-frame-15.png`.

## Rollingphus-endless — the tumble in the close-up style

![Rollingphus-endless preview](rollingphus-endless-preview.png)

Rollingphus drawn in the Sisyphus-endless close-up style, on the same steep
ground line and with the same boulder as Circusphus-endless. He pushes it up,
then it slips back and knocks him over. It rolls back down with him stuck to
its rim like a sticker, turning round with it and bumping up each time it rolls
over him. Once it stops he sits beside it, dazed, then gets up and pushes again.

- 16 frames, 100 × 36 px, monochrome PNG with a transparent background
- Frames 0–7 push up, 8 knocked back, 9–14 roll down stuck to the rim, 15 sits dazed

Install it the same way as Sisyphus (see [Install](#install)), with these
changes:

- **Frames:** [`rollingphus-endless-frames.zip`](rollingphus-endless-frames.zip) unzips to `rollingphus-endless-frames/` with
  `rollingphus-endless-frame-0.png` to `rollingphus-endless-frame-15.png`.
- **Runner Name:** `Rollingphus-endless`.
- **Frame order:** add the PNGs in order, from `rollingphus-endless-frame-0.png` to
  `rollingphus-endless-frame-15.png`.

## Rebuilding the frames

The frames are drawn by a script, not by hand. You need Python 3 and Pillow:

```sh
python3 -m venv venv
venv/bin/pip install pillow
venv/bin/python scratchpad/sisyphus/gen.py   # writes sisyphus-frames/ and sisyphus-preview.png
venv/bin/python scratchpad/vchk.py           # checks frame sizes and that the preview matches the frames
```

For Surfingphus, pass the variant name to both scripts:

```sh
venv/bin/python scratchpad/sisyphus/gen.py surfingphus   # writes surfingphus-frames/ and surfingphus-preview.png
venv/bin/python scratchpad/vchk.py surfingphus
```

For Rollingphus:

```sh
venv/bin/python scratchpad/sisyphus/gen.py rollingphus   # writes rollingphus-frames/ and rollingphus-preview.png
venv/bin/python scratchpad/vchk.py rollingphus
```

For Circusphus:

```sh
venv/bin/python scratchpad/sisyphus/gen.py circusphus   # writes circusphus-frames/ and circusphus-preview.png
venv/bin/python scratchpad/vchk.py circusphus
```

For Sisyphus-endless:

```sh
venv/bin/python scratchpad/sisyphus/gen.py sisyphus-endless   # writes sisyphus-endless-frames/ and sisyphus-endless-preview.png
venv/bin/python scratchpad/vchk.py sisyphus-endless
venv/bin/python scratchpad/sisyphus/gen.py circusphus-endless   # writes circusphus-endless-frames/ and circusphus-endless-preview.png
venv/bin/python scratchpad/vchk.py circusphus-endless
venv/bin/python scratchpad/sisyphus/gen.py rollingphus-endless   # writes rollingphus-endless-frames/ and rollingphus-endless-preview.png
venv/bin/python scratchpad/vchk.py rollingphus-endless
```

To rebuild the zip without macOS junk files:

```sh
zip -r sisyphus-frames.zip sisyphus-frames -x "*.DS_Store" "__MACOSX/*"
zip -r surfingphus-frames.zip surfingphus-frames -x "*.DS_Store" "__MACOSX/*"
zip -r rollingphus-frames.zip rollingphus-frames -x "*.DS_Store" "__MACOSX/*"
zip -r circusphus-frames.zip circusphus-frames -x "*.DS_Store" "__MACOSX/*"
zip -r sisyphus-endless-frames.zip sisyphus-endless-frames -x "*.DS_Store" "__MACOSX/*"
zip -r circusphus-endless-frames.zip circusphus-endless-frames -x "*.DS_Store" "__MACOSX/*"
zip -r rollingphus-endless-frames.zip rollingphus-endless-frames -x "*.DS_Store" "__MACOSX/*"
```

## Files

| Path | What it is |
|---|---|
| `sisyphus-frames/` | the 18 animation frames |
| `sisyphus-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `sisyphus-preview.png` | animated PNG preview |
| `surfingphus-frames/` | the 18 Surfingphus animation frames |
| `surfingphus-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `surfingphus-preview.png` | animated PNG preview of Surfingphus |
| `rollingphus-frames/` | the 18 Rollingphus animation frames |
| `rollingphus-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `rollingphus-preview.png` | animated PNG preview of Rollingphus |
| `circusphus-frames/` | the 18 Circusphus animation frames |
| `circusphus-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `circusphus-preview.png` | animated PNG preview of Circusphus |
| `sisyphus-endless-frames/` | the 8 Sisyphus-endless animation frames |
| `sisyphus-endless-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `sisyphus-endless-preview.png` | animated PNG preview of Sisyphus-endless |
| `circusphus-endless-frames/` | the 16 Circusphus-endless animation frames |
| `circusphus-endless-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `circusphus-endless-preview.png` | animated PNG preview of Circusphus-endless |
| `rollingphus-endless-frames/` | the 16 Rollingphus-endless animation frames |
| `rollingphus-endless-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `rollingphus-endless-preview.png` | animated PNG preview of Rollingphus-endless |
| `scratchpad/sisyphus/gen.py` | the frame generator for all seven runners (`sisyphus`, `surfingphus`, `rollingphus`, `circusphus`, `sisyphus-endless`, `circusphus-endless` or `rollingphus-endless`) |
| `scratchpad/vchk.py` | the frame and preview checker (same variant argument) |
| `scratchpad/sisyphus/zoom.py` | makes an enlarged view of the frames for review |

## License

[MIT](LICENSE) © 2026 twjohnwu. The copy submitted to the
[Runner Gallery](https://github.com/runcat-dev/RunnerGallery) is also
distributed there under that repository's Apache-2.0 license.
