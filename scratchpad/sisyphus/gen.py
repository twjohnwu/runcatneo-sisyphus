import math, os, struct, zlib, sys
from PIL import Image, ImageDraw, ImageFont
SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(SP, "..", ".."))  # repo root
FD = OUT + "/sisyphus-frames"
K = 8
R = 4.5
HEAD_ANG = 15
S = 21 / 88.0

def surf(x):
    if x <= 88: return 34 - S * x
    return 13.0

def rock_y(x):
    return (surf(x) - R * math.sqrt(1 + S * S) - 0.4) if x <= 88 else 13 - R - 0.4

# per frame: rock centre x, man foot x, mode
# modes: push (leg pose A/B), stand, droop, walk (A/B)
T = []
for i in range(11):
    T.append((14 + 7 * i, 4 + 7 * i, "pushA" if i % 2 == 0 else "pushB"))
T.append((92, 79, "stand"))
T += [(67, 79, "droop"), (41, 79, "droop"), (15, 79, "droop")]
T += [(14, 58, "walkA"), (14, 32, "walkB"), (14, 4, "walkA")]

def P(x, y): return (x * K, y * K)

def line(d, a, b, w):
    d.line([P(*a), P(*b)], fill=255, width=int(w * K))
    for p in (a, b):
        d.ellipse([P(p[0] - w / 2, p[1] - w / 2), P(p[0] + w / 2, p[1] + w / 2)], fill=255)

def ik(hip, foot, l1, l2, sgn=1):
    dx, dy = foot[0] - hip[0], foot[1] - hip[1]
    dist = min(math.hypot(dx, dy), l1 + l2 - 1e-3)
    a = (l1 * l1 - l2 * l2 + dist * dist) / (2 * dist)
    h = math.sqrt(max(l1 * l1 - a * a, 0))
    mx, my = hip[0] + dx * a / dist, hip[1] + dy * a / dist
    return (mx + sgn * h * dy / dist * -1, my + sgn * h * dx / dist)

def torso(d, hip, sh, w):
    L = math.hypot(sh[0] - hip[0], sh[1] - hip[1])
    nx, ny = -(sh[1] - hip[1]) / L * w / 2, (sh[0] - hip[0]) / L * w / 2
    d.polygon([P(hip[0] + nx, hip[1] + ny), P(hip[0] - nx, hip[1] - ny),
               P(sh[0] - nx, sh[1] - ny), P(sh[0] + nx, sh[1] + ny)], fill=255)

def leg(d, hip, foot, bend):
    if bend:
        knee = ik(hip, foot, 3.2, 3.2, 1)
        line(d, hip, knee, 2.0); line(d, knee, foot, 2.0)
    else:
        line(d, hip, foot, 2.0)

def man(d, fx, mode, rx, ry):
    fy = surf(fx)
    if mode.startswith("push"):
        A = mode == "pushA"
        a, b, hh = (-3.8, 1.6, 4.7) if A else (-3.0, 2.2, 5.1)
        hip = (fx, fy - hh)
        t = math.radians(30)
        dv = (math.sin(t), -math.cos(t))
        sh = (hip[0] + 3.6 * dv[0], hip[1] + 3.6 * dv[1])
        t2 = math.radians(HEAD_ANG)
        head = (sh[0] + 2.8 * math.sin(t2), sh[1] - 2.8 * math.cos(t2))
        ft = [(fx + a, surf(fx + a)), (fx + b, surf(fx + b))]
        torso(d, hip, sh, 3.0)
        leg(d, hip, ft[0], not A)
        leg(d, hip, ft[1], True)
        ash = (sh[0] - 1.2 * dv[0], sh[1] - 1.2 * dv[1])
        for hy in (ry + 0.3, ry + 2.1):
            line(d, ash, (rx - 5.1, hy), 1.8)
    else:
        if mode == "stand":
            hip = (fx, fy - 6.0); sh = (fx, fy - 9.4); head = (fx, fy - 12.0)
            feet = [(fx - 1.2, surf(fx - 1.2)), (fx + 1.2, surf(fx + 1.2))]
            arms = [(-1.6, 4.8), (1.8, 5.0)]
        elif mode == "droop":
            hip = (fx, fy - 6.0); sh = (fx - 0.7, fy - 9.3); head = (fx - 2.1, fy - 11.4)
            feet = [(fx - 1.2, surf(fx - 1.2)), (fx + 1.2, surf(fx + 1.2))]
            arms = [(-1.9, 3.6), (-0.1, 3.6)]
        else:
            hip = (fx, fy - 6.0); sh = (fx - 0.4, fy - 9.4); head = (fx - 0.7, fy - 12.0)
            a, b = (-2.4, 2.4) if mode == "walkA" else (2.4, -2.4)
            feet = [(fx + a, surf(fx + a)), (fx + b, surf(fx + b))]
            arms = [(b * 0.6, 5.6), (a * 0.6, 5.6)]
        for f in feet: line(d, hip, f, 2.0)
        torso(d, hip, sh, 3.0)
        ash = (sh[0], sh[1] + 0.4)
        for dx, h in arms:
            line(d, ash, (sh[0] + dx, fy - h), 1.8)
    d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)

def frame(i):
    rx, fx, mode = T[i]
    ry = rock_y(rx)
    m = Image.new("L", (100 * K, 36 * K), 0)
    d = ImageDraw.Draw(m)
    d.polygon([P(0, 34), P(88, 13), P(96, 13), P(100, 16), P(100, 36), P(0, 36)], fill=255)
    man(d, fx, mode, rx, ry)
    h = R + 0.9
    d.ellipse([P(rx - h, ry - h), P(rx + h, ry + h)], fill=0)
    d.ellipse([P(rx - R, ry - R), P(rx + R, ry + R)], fill=255)
    ang = rx / R + 0.6
    nx, ny = rx + 2.5 * math.cos(ang), ry + 2.5 * math.sin(ang)
    d.ellipse([P(nx - .6, ny - .6), P(nx + .6, ny + .6)], fill=0)
    a = m.resize((100, 36), Image.LANCZOS)
    img = Image.new("RGBA", (100, 36), (0, 0, 0, 0))
    img.putalpha(a)
    px = img.load()
    for y in range(36):
        for x in range(100):
            px[x, y] = (0, 0, 0, px[x, y][3] if px[x, y][3] >= 6 else 0)  # drop Lanczos ringing
    return img

def chunk(t, data):
    c = struct.pack(">I", len(data)) + t + data
    return c + struct.pack(">I", zlib.crc32(t + data) & 0xffffffff)

def write_apng(frames, path, delay_ms=80):
    raw = []
    for im in frames:
        rows = b"".join(b"\x00" + im.tobytes()[y * 400:(y + 1) * 400] for y in range(36))
        raw.append(zlib.compress(rows, 9))
    o = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 100, 36, 8, 6, 0, 0, 0))
    o += chunk(b"acTL", struct.pack(">II", len(frames), 0))
    seq = 0
    for n, z in enumerate(raw):
        o += chunk(b"fcTL", struct.pack(">IIIIIHHBB", seq, 100, 36, 0, 0, delay_ms, 1000, 1, 0)); seq += 1
        if n == 0: o += chunk(b"IDAT", z)
        else:
            o += chunk(b"fdAT", struct.pack(">I", seq) + z); seq += 1
    o += chunk(b"IEND", b"")
    open(path, "wb").write(o)

if __name__ == "__main__":
    frames = [frame(i) for i in range(18)]
    os.makedirs(FD, exist_ok=True)
    for i, f in enumerate(frames):
        f.save(f"{FD}/sisyphus-frame-{i}.png")
    write_apng(frames, OUT + "/sisyphus-preview.png")
    Z = 6; cw, ch = 100 * Z + 20, 36 * Z + 28
    sheet = Image.new("RGB", (3 * cw, 6 * ch), (160, 160, 160))
    dr = ImageDraw.Draw(sheet)
    try: fnt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except Exception: fnt = ImageFont.load_default()
    for i, f in enumerate(frames):
        cx, cy = (i % 3) * cw + 10, (i // 3) * ch + 24
        dr.text((cx, cy - 22), str(i), fill=(0, 0, 0), font=fnt)
        big = f.resize((100 * Z, 36 * Z), Image.NEAREST)
        sheet.paste(big, (cx, cy), big)
    sheet.save(SP + "/contact.png")
    for i in (0, 17): print(i, T[i])
