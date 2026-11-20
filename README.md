# Sisyphus — RunCat Neo runners

## Sisyphus

![Sisyphus preview](sisyphus-preview.png)

Sisyphus pushes his boulder up the slope. At the top, the boulder rolls back
down, and he walks down after it to start again. The faster your CPU works,
the faster he pushes.

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
| **Surfingphus-endless** | Close-up Surfingphus: pushes up, jumps on, a surfboard pops in and he surfs down, hops off. (16 frames) | ![Surfingphus-endless](surfingphus-endless-preview.png) | [`surfingphus-endless-frames.zip`](surfingphus-endless-frames.zip) |

All runners are 100 × 36 px monochrome PNG frames on a transparent background.
Install any of them as described in [Install](#install), using the runner's
name from the table as **Runner Name** and its own frames zip.

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

## License

[MIT](LICENSE) © 2026 twjohnwu. The copy submitted to the
[Runner Gallery](https://github.com/runcat-dev/RunnerGallery) is also
distributed there under that repository's Apache-2.0 license.
