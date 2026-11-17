# Sisyphus, Surfingphus & Rollingphus — RunCat Neo runners

This repo holds three custom runners for [RunCat Neo](https://runcat-dev.github.io/RunCatNeo/):
**Sisyphus** (below), **Surfingphus** and **Rollingphus** (further down). Each
has its own frames, zip and preview.

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

To rebuild the zip without macOS junk files:

```sh
zip -r sisyphus-frames.zip sisyphus-frames -x "*.DS_Store" "__MACOSX/*"
zip -r surfingphus-frames.zip surfingphus-frames -x "*.DS_Store" "__MACOSX/*"
zip -r rollingphus-frames.zip rollingphus-frames -x "*.DS_Store" "__MACOSX/*"
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
| `scratchpad/sisyphus/gen.py` | the frame generator for all three runners (`sisyphus`, `surfingphus` or `rollingphus`) |
| `scratchpad/vchk.py` | the frame and preview checker (same variant argument) |
| `scratchpad/sisyphus/zoom.py` | makes an enlarged view of the frames for review |

## License

[MIT](LICENSE) © 2026 twjohnwu. The copy submitted to the
[Runner Gallery](https://github.com/runcat-dev/RunnerGallery) is also
distributed there under that repository's Apache-2.0 license.
