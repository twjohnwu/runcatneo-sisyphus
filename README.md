# Sisyphus — a RunCat Neo runner

![Sisyphus preview](sisyphus-preview.png)

A custom runner for [RunCat Neo](https://runcat-dev.github.io/RunCatNeo/).
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

## Rebuilding the frames

The frames are drawn by a script, not by hand. You need Python 3 and Pillow:

```sh
python3 -m venv venv
venv/bin/pip install pillow
venv/bin/python scratchpad/sisyphus/gen.py   # writes sisyphus-frames/ and sisyphus-preview.png
venv/bin/python scratchpad/vchk.py           # checks frame sizes and that the preview matches the frames
```

To rebuild the zip without macOS junk files:

```sh
zip -r sisyphus-frames.zip sisyphus-frames -x "*.DS_Store" "__MACOSX/*"
```

## Files

| Path | What it is |
|---|---|
| `sisyphus-frames/` | the 18 animation frames |
| `sisyphus-frames.zip` | the same frames, zipped in the Runner Gallery format |
| `sisyphus-preview.png` | animated PNG preview |
| `scratchpad/sisyphus/gen.py` | the frame generator |
| `scratchpad/vchk.py` | the frame and preview checker |
| `scratchpad/sisyphus/zoom.py` | makes an enlarged view of the frames for review |

## License

[MIT](LICENSE) © 2026 twjohnwu. The copy submitted to the
[Runner Gallery](https://github.com/runcat-dev/RunnerGallery) is also
distributed there under that repository's Apache-2.0 license.
