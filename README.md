# Sisyphus, Surfingphus, Rollingphus, Circusphus, Sisyphus-endless, Circusphus-endless & Rollingphus-endless — RunCat Neo runners

This repo holds seven custom runners for [RunCat Neo](https://runcat-dev.github.io/RunCatNeo/):
Sisyphus and six variants of him, listed below. Each has its own frames, zip
and preview.

## All runners

| Runner | What happens | Animation | Download |
|---|---|---|---|
| [Sisyphus](#sisyphus) | Pushes the boulder up the hill; it rolls back down and he walks after it. (18 frames) | ![Sisyphus](sisyphus-preview.png) | [`sisyphus-frames.zip`](sisyphus-frames.zip) |
| **Surfingphus** | Pushes it up, then a surfboard pops in and he surfs it down. (18 frames) | ![Surfingphus](surfingphus-preview.png) | [`surfingphus-frames.zip`](surfingphus-frames.zip) |
| **Rollingphus** | The boulder slips back, rolls over him, and he rolls down stuck to it. (18 frames) | ![Rollingphus](rollingphus-preview.png) | [`rollingphus-frames.zip`](rollingphus-frames.zip) |
| **Circusphus** | Pushes it up, jumps on, and ball-walks down like a circus clown. (18 frames) | ![Circusphus](circusphus-preview.png) | [`circusphus-frames.zip`](circusphus-frames.zip) |
| **Sisyphus-endless** | Close-up: pushes forever up a scrolling slope, never reaching the top. (8 frames) | ![Sisyphus-endless](sisyphus-endless-preview.png) | [`sisyphus-endless-frames.zip`](sisyphus-endless-frames.zip) |
| **Circusphus-endless** | Close-up Circusphus: pushes up, jumps on, ball-walks down, hops off. (16 frames) | ![Circusphus-endless](circusphus-endless-preview.png) | [`circusphus-endless-frames.zip`](circusphus-endless-frames.zip) |
| **Rollingphus-endless** | Close-up Rollingphus: pushes up, gets knocked over, rolls down stuck to the rim, sits dazed. (16 frames) | ![Rollingphus-endless](rollingphus-endless-preview.png) | [`rollingphus-endless-frames.zip`](rollingphus-endless-frames.zip) |

All runners are 100 × 36 px monochrome PNG frames on a transparent background.
Install any of them as described in [Install](#install), using the runner's
name from the table as **Runner Name** and its own frames zip.

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

For any other runner in the [table](#all-runners), use its zip (for example
`circusphus-endless-frames.zip`), set **Runner Name** to its name (for
example `Circusphus-endless`), and add its PNGs in order from
`<name>-frame-0.png` to the last frame.

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
