import math, os, struct, zlib, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(SP, "..", ".."))  # repo root
VARIANT = sys.argv[1] if len(sys.argv) > 1 else "sisyphus"
if VARIANT not in ("sisyphus", "sisyphus-endless", "surfingphus", "rollingphus", "circusphus"):
    sys.exit("usage: gen.py [sisyphus|sisyphus-endless|surfingphus|rollingphus|circusphus]")
FD = OUT + "/" + VARIANT + "-frames"
K = 8
R = 4.5
HEAD_ANG = 15
# terrain per variant: slope from (0, Y0) up to a plateau at Y1 from x=88
Y0, Y1 = (34, 24) if VARIANT in ("surfingphus", "circusphus") else (34, 13)
S = (Y0 - Y1) / 88.0

def surf(x):
    if x <= 88: return Y0 - S * x
    return float(Y1)

def rock_y(x):
    return (surf(x) - R * math.sqrt(1 + S * S) - 0.4) if x <= 88 else Y1 - R - 0.4

# per frame: rock centre x, man foot x, mode
# modes: push (leg pose A/B), stand, droop, walk (A/B)
T = []
for i in range(11):
    T.append((14 + 7 * i, 4 + 7 * i, "pushA" if i % 2 == 0 else "pushB"))
T.append((92, 79, "stand"))
T += [(67, 79, "droop"), (41, 79, "droop"), (15, 79, "droop")]
T += [(14, 58, "walkA"), (14, 32, "walkB"), (14, 4, "walkA")]

# surfingphus: same push frames 0-10, then he climbs onto the boulder at the top,
# rides it down (rock x only; his feet follow the boulder), hops off at the bottom
if VARIANT == "surfingphus":
    T = T[:11]
    T.append((92, 83, "step"))
    T += [(84, 0, "surfA"), (68, 0, "surfB"), (52, 0, "surfA"), (36, 0, "surfB"), (20, 0, "surfA")]
    T.append((14, 6, "hop"))

# rollingphus: same push frames 0-10, then the boulder slips back and knocks him down (hit),
# rolls over him and he sticks to its rim (tumble:<rim angle in deg>:<pose>, screen angle,
# 90 = bottom, decreasing = counter-clockwise = rolling left), then he sits dazed at the bottom
if VARIANT == "rollingphus":
    T = T[:11]
    T.append((82, 73, "hit"))
    T += [(79, 0, "tumble:180:0"), (63, 0, "tumble:90:1:1.5"), (46, 0, "tumble:0:0"),
          (30, 0, "tumble:-90:1"), (14, 0, "tumble:-180:0")]
    T.append((14, 5, "dazed"))

# circusphus: same push frames 0-10 on the low terrain, then he jumps onto the boulder at the
# top and ball-walks on it like a circus clown (feet alternate, arms flail) as it rolls down
# (~16 px/frame, notch counter-clockwise), and hops off to the left once it has stopped
if VARIANT == "circusphus":
    T = T[:11]
    T.append((88, 0, "jump"))
    T += [(76, 0, "ballA"), (60, 0, "ballB"), (44, 0, "ballA"), (28, 0, "ballB"), (16, 0, "ballA")]
    T.append((14, 5, "hop"))

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

BOARD_TILT = math.radians(8)  # nose down-left, roughly following the slope

def board_frame(rx, ry):
    # board centre sits on top of the boulder, clear of its halo; u runs along the board
    # (uphill = right), n is the board's up normal
    u = (math.cos(BOARD_TILT), -math.sin(BOARD_TILT))
    n = (-math.sin(BOARD_TILT), -math.cos(BOARD_TILT))
    off = R + 0.9 + 0.9
    return (rx + n[0] * off, ry + n[1] * off), u, n

def board_pt(c, u, n, s, h):
    return (c[0] + u[0] * s + n[0] * h, c[1] + u[1] * s + n[1] * h)

def draw_board(d, rx, ry):
    c, u, n = board_frame(rx, ry)
    # ~14 px long, 1.8 px thick, pointed nose with a little rocker
    pts = [(-7.0, 0.4), (-5.0, 0.9), (5.0, 0.9), (6.6, 0.6), (6.6, -0.5), (5.0, -0.9), (-5.0, -0.9)]
    d.polygon([P(*board_pt(c, u, n, s, h)) for s, h in pts], fill=255)

def sparkle(d, rx, ry):
    # a few short radiating ticks at the board's ends: the board has just appeared
    c, u, n = board_frame(rx, ry)
    for s0, dirs in ((-7.6, ((-1, 0), (-0.8, -0.8), (-0.8, 0.8))), (7.6, ((1, 0), (0.8, -0.8)))):
        o = board_pt(c, u, n, s0, 0.0)
        for dx, dy in dirs:
            L = math.hypot(dx, dy)
            a = (o[0] + 1.2 * dx / L, o[1] + 1.2 * dy / L)
            b = (o[0] + 3.0 * dx / L, o[1] + 3.0 * dy / L)
            line(d, a, b, 0.9)

def surfman(d, mode, rx, ry):
    # surfer standing on the board across the boulder's top, side-on, facing left
    # (downhill): wide stance, knees bent, torso leaning back uphill (right), arms out
    c, u, n = board_frame(rx, ry)
    A = mode == "surfA"
    ss = (-3.4, 2.8) if A else (-3.0, 3.2)
    ft = [board_pt(c, u, n, s, 2.3) for s in ss]
    hip = ((ft[0][0] + ft[1][0]) / 2 + 0.8, min(ft[0][1], ft[1][1]) - 2.6)
    t = math.radians(26 if A else 18)
    sh = (hip[0] + 2.6 * math.sin(t), hip[1] - 2.6 * math.cos(t))
    head = (sh[0] - 0.2, sh[1] - 2.5)
    torso(d, hip, sh, 3.0)
    for f in ft: leg(d, hip, f, True)
    ash = (sh[0], sh[1] + 0.4)
    hands = [(-4.6, -0.9), (4.6, 0.7)] if A else [(-4.6, 0.7), (4.6, -0.9)]
    for dx, dy in hands: line(d, ash, (ash[0] + dx, ash[1] + dy), 1.8)
    d.ellipse([P(head[0] - 1.9, head[1] - 1.9), P(head[0] + 1.9, head[1] + 1.9)], fill=255)

def stuck(d, rx, ry, phi, pose):
    # man stuck to the rim like a sticker at screen angle phi: torso curves along the rim,
    # head toward +arc, limbs splayed outward; (da, h) = (arc offset in deg, distance from centre)
    # points are clamped above the slope so he never sinks into the hill
    if abs(phi - 90) < 1e-6:
        flat(d, rx, ry)
        return
    def Q(da, h, m=1.0):
        a = math.radians(phi + da)
        x, y = rx + h * math.cos(a), ry + h * math.sin(a)
        return (x, min(y, surf(x) - m))
    hb = R + 2.6
    hip, sh = Q(-22, hb, 1.8), Q(22, hb, 1.8)
    head = Q(52, hb + 0.4, 2.1)
    torso(d, hip, sh, 3.0)
    if pose == 0:
        legs = [(-48, hb + 1.6, -72, hb + 0.6), (-42, hb + 0.2, -66, hb + 2.6)]
        arms = [(40, hb + 3.2), (6, hb + 3.6)]
    else:
        legs = [(-46, hb + 2.2, -70, hb + 1.8), (-44, hb + 0.4, -72, hb + 0.9)]
        arms = [(46, hb + 2.4), (0, hb + 3.8)]
    for kd, kh, fd, fh in legs:
        line(d, hip, Q(kd, kh), 2.0); line(d, Q(kd, kh), Q(fd, fh), 2.0)
    for da, h in arms: line(d, sh, Q(da, h), 1.8)
    d.ellipse([P(head[0] - 1.9, head[1] - 1.9), P(head[0] + 1.9, head[1] + 1.9)], fill=255)

def flat(d, rx, ry):
    # squashed flat under the boulder: thin body lying on the slope, limbs out sideways
    th = math.atan(S)
    u = (math.cos(th), -math.sin(th))
    n = (-math.sin(th), -math.cos(th))
    gx = rx
    gy = surf(rx)
    def G(s, h):
        return (gx + u[0] * s + n[0] * h, gy + u[1] * s + n[1] * h)
    hh = 1.0
    line(d, G(-3.0, hh), G(2.6, hh), 1.8)
    line(d, G(-3.0, hh), G(-9.0, hh + 0.9), 1.1); line(d, G(-3.2, hh + 0.3), G(-7.4, hh + 1.9), 1.1)
    line(d, G(2.6, hh), G(8.6, hh + 0.9), 1.1); line(d, G(2.4, hh + 0.3), G(7.0, hh + 1.9), 1.1)
    c = G(4.2, 1.0)
    d.ellipse([P(c[0] - 1.8, c[1] - 1.0), P(c[0] + 1.8, c[1] + 1.0)], fill=255)

def man(d, fx, mode, rx, ry):
    fy = surf(fx)
    if mode.startswith("tumble"):
        _, phi, pose = mode.split(":")[:3]
        stuck(d, rx, ry, float(phi), int(pose))
        return
    if mode == "jump":
        # airborne above the boulder's top, knees tucked, arms thrown up
        hip = (rx - 3.0, ry - 10.2); sh = (rx - 2.7, ry - 13.2); head = (rx - 2.4, ry - 15.8)
        torso(d, hip, sh, 3.0)
        for f in ((rx - 4.4, ry - 7.2), (rx - 0.8, ry - 7.4)): leg(d, hip, f, True)
        for dx, dy in ((-2.8, -3.2), (3.0, -3.0)):
            line(d, (sh[0], sh[1] + 0.4), (sh[0] + dx, sh[1] + dy), 1.8)
        d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)
        return
    if mode.startswith("ball"):
        # standing on the boulder's top, facing left: feet swap forward/back each frame
        # (one swinging foot lifted), torso swaying, arms flailing up/down alternately
        A = mode == "ballA"
        dxs, lifts = ((-3.0, 1.6), (0.0, 1.0)) if A else ((-1.6, 3.0), (1.0, 0.0))
        rr = R + 1.5
        ft = [(rx + dx, ry - math.sqrt(rr * rr - dx * dx) - lf) for dx, lf in zip(dxs, lifts)]
        hip = (rx + (-0.5 if A else 0.5), (ft[0][1] + ft[1][1]) / 2 - 5.0)
        t = math.radians(-9 if A else 9)
        sh = (hip[0] + 3.2 * math.sin(t), hip[1] - 3.2 * math.cos(t))
        head = (sh[0] + 0.6 * math.sin(t), sh[1] - 2.6)
        torso(d, hip, sh, 3.0)
        for f in ft: leg(d, hip, f, True)
        hands = [(-4.2, -3.4), (4.4, 1.0)] if A else [(-4.2, 1.0), (4.4, -3.4)]
        for dx, dy in hands: line(d, (sh[0], sh[1] + 0.4), (sh[0] + dx, sh[1] + dy), 1.8)
        d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)
        return
    if mode == "hit":
        # knocked backward (left) by the boulder: torso thrown back, arms flung up, one leg kicked up
        hip = (fx, fy - 5.6)
        t = math.radians(-48)
        sh = (hip[0] + 3.6 * math.sin(t), hip[1] - 3.6 * math.cos(t))
        t2 = math.radians(-70)
        head = (sh[0] + 3.0 * math.sin(t2), sh[1] - 3.0 * math.cos(t2))
        torso(d, hip, sh, 3.0)
        leg(d, hip, (fx - 1.0, surf(fx - 1.0)), True)
        leg(d, hip, (fx + 3.6, fy - 3.6), True)
        for dx, dy in ((3.4, -4.6), (0.6, -5.4)):
            line(d, (sh[0] + 0.2, sh[1] - 0.2), (sh[0] + dx, sh[1] + dy), 1.8)
        d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)
        return
    if mode == "dazed":
        # sitting up on the ground left of the boulder, knees up, head drooping, dizzy ticks above
        hip = (fx - 0.6, fy - 1.6)
        sh = (fx - 1.4, fy - 5.2)
        head = (fx - 1.4, fy - 8.4)
        knee = (fx + 3.2, fy - 3.6)
        torso(d, hip, sh, 3.0)
        line(d, hip, knee, 2.0); line(d, knee, (fx + 3.4, surf(fx + 3.4)), 2.0)
        line(d, (sh[0], sh[1] + 0.6), (knee[0] - 0.4, knee[1] - 0.6), 1.8)
        d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)
        for ox, oy in ((fx + 4.4, fy - 12.0),):
            line(d, (ox - 1.1, oy), (ox + 1.1, oy), 0.9); line(d, (ox, oy - 1.1), (ox, oy + 1.1), 0.9)
        return
    if mode.startswith("surf"):
        draw_board(d, rx, ry)
        surfman(d, mode, rx, ry)
        return
    if mode == "step":
        # crouched on the slope, one foot already up on the boulder's flank, reaching up
        hip = (fx, fy - 5.4)
        sh = (hip[0] + 0.2, hip[1] - 3.2)
        head = (sh[0] - 0.6, sh[1] - 2.6)
        back = (fx - 1.4, surf(fx - 1.4))
        front = (rx - 2.6, ry - 4.9)
        torso(d, hip, sh, 3.0)
        leg(d, hip, back, True); leg(d, hip, front, True)
        for hd in ((rx - 6.0, ry - 2.0), (rx - 5.8, ry - 4.0)):
            line(d, (sh[0] - 0.3, sh[1] + 0.4), hd, 1.8)
        d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)
        return
    if mode == "hop":
        # airborne, both feet off the ground, hopping off to the left
        hip = (fx, fy - 8.2); sh = (fx - 0.4, hip[1] - 3.3); head = (fx - 0.8, sh[1] - 2.7)
        feet = [(fx - 2.4, fy - 3.4), (fx + 1.6, fy - 3.0)]
        torso(d, hip, sh, 3.0)
        for f in feet: leg(d, hip, f, True)
        for dx, dy in ((-2.8, -2.6), (3.8, -2.4)):
            line(d, (sh[0], sh[1] + 0.4), (sh[0] + dx, sh[1] + dy), 1.8)
        d.ellipse([P(head[0] - 2, head[1] - 2), P(head[0] + 2, head[1] + 2)], fill=255)
        return
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

def frame_circus(i, rx, fx, mode, ry):
    # layered so the man and his separation outline never cut the hill:
    # hill | man (minus boulder halo) | boulder (minus man outline, minus notch)
    W, H = 100 * K, 36 * K
    g = Image.new("L", (W, H), 0)
    ImageDraw.Draw(g).polygon([P(0, Y0), P(88, Y1), P(96, Y1), P(100, Y1 + 3), P(100, 36), P(0, 36)], fill=255)
    mm = Image.new("L", (W, H), 0)
    man(ImageDraw.Draw(mm), fx, mode, rx, ry)
    h = R + 0.9
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).ellipse([P(rx - h, ry - h), P(rx + h, ry + h)], fill=255)
    mm.paste(0, mask=halo)
    bl = Image.new("L", (W, H), 0)
    bd = ImageDraw.Draw(bl)
    bd.ellipse([P(rx - R, ry - R), P(rx + R, ry + R)], fill=255)
    bl.paste(0, mask=mm.filter(ImageFilter.MaxFilter(11)))
    ang = 0.6 - math.radians(75) * (min(i, 17) - 11) if i >= 11 else rx / R + 0.6
    nx, ny = rx + 2.5 * math.cos(ang), ry + 2.5 * math.sin(ang)
    bd.ellipse([P(nx - .6, ny - .6), P(nx + .6, ny + .6)], fill=0)
    m = g.copy()
    m.paste(255, mask=mm)
    m.paste(255, mask=bl)
    return m

# ---- sisyphus-endless: close-up in-place push loop on a bumpy uphill slope ----
# Everything is drawn in slope coordinates (s along the slope, n up from it) and rotated onto
# the canvas by W(). The ground scrolls down-slope GS px per frame; the boulder rolls without
# slipping (15 deg per frame), so 16 frames = 2 foot cycles = 2/3 boulder turn = one bump period.
ENF = 16
ER = 14.0                          # boulder radius (old close-up: 11.8)
SC = 1.15 * ER / 12.6              # figure scale (drawn for ER 12.6, enlarged 15% for the close-up)
ECROP = 6.5                        # px of the boulder's top cut off by the canvas top edge
EOX = 84.0                         # canvas x of the boulder centre (man sits at the middle, boulder to his right)
ETH = math.radians(19)             # slope angle
GS = ER * math.radians(15)         # ground scroll per frame = rolling distance at 15 deg per frame
EPER = ENF * GS                    # bump pattern period (= total scroll over the loop)
EO = [EOX, 0.0]                   # canvas point of the boulder's contact with the mean slope line (y set below)

def W(s, n):
    return (EO[0] + s * math.cos(ETH) - n * math.sin(ETH), EO[1] - s * math.sin(ETH) - n * math.cos(ETH))

# bump profile: sines whose periods divide EPER, plus a few rocks/pebbles (half-discs)
_SINES = ((1, .65, 0.3), (2, .55, 2.1), (3, .42, 4.4), (5, .30, 1.0), (7, .22, 5.2))
_ROCKS = ((0.12, 2.0), (0.43, 1.2), (0.70, 1.6), (0.88, 0.9))   # (position / EPER, radius)

def hump(p):
    p %= EPER
    v = sum(a * math.sin(2 * math.pi * k * p / EPER + ph) for k, a, ph in _SINES)
    for f, r in _ROCKS:
        for sh in (-EPER, 0, EPER):
            dx = p - f * EPER + sh
            if abs(dx) < r: v = max(v, math.sqrt(r * r - dx * dx) * 1.0 + 0.2)
    return v

def boulder_n(sc):
    # lowest centre height (slope frame) that keeps the boulder's halo clear of the bumps
    rh = ER + 0.9
    return max(hump(q * 0.25 + sc) + math.sqrt(rh * rh - (q * 0.25) ** 2) for q in range(-int(rh * 4), int(rh * 4) + 1))

# top of the boulder at its highest bob sits ECROP px above the canvas edge (cropped)
EO[1] = -ECROP + ER + max(boulder_n(GS * k) for k in range(ENF)) * math.cos(ETH)

def sis_man(d, i, sc, hs, hn, ap):
    m = SC
    ta = math.radians(ap)
    sh = (hs + 11.5 * m * math.sin(ta), hn + 11.5 * m * math.cos(ta))
    head = (sh[0] + 3.2 * m, sh[1] - 0.9 * m)   # canvas offset: ahead of and above the shoulder
    line(d, W(hs, hn), W(*sh), 3.2 * m)
    for ph in (0, 2):
        u = (i + ph) % 4
        tri = u if u <= 2 else 4 - u   # stance 2 frames backwards with the ground, swing 2 frames forwards
        rel = 4.0 * m - GS * tri
        lift = 4.6 * m * math.sin(math.pi * (u - 2) / 2) if u >= 2 else 0.0
        fs = hs + rel
        foot = W(fs, hump(fs + sc) + 1.5 * m + lift)
        knee = ik(W(hs, hn), foot, 8.4 * m, 8.4 * m, -1)
        line(d, W(hs, hn), knee, 2.4 * m); line(d, knee, foot, 2.4 * m)
    return W(*sh), W(*head)

def frame_endless(i):
    Wd, Ht = 100 * K, 36 * K
    sc = GS * i
    g = Image.new("L", (Wd, Ht), 0)
    gd = ImageDraw.Draw(g)
    pts = [W(s * 0.5, hump(s * 0.5 + sc)) for s in range(-500, 501)]
    gd.polygon([P(*q) for q in pts] + [P(*W(250, -400)), P(*W(-250, -400))], fill=255)
    # boulder rests on the bumps: lowest centre height that keeps the halo clear of the ground
    rh = ER + 0.9
    cn = boulder_n(sc)
    cxy = W(0, cn)
    hs, ap = -29.0 * SC, 62.0
    hn = 13.4 * SC + 0.6 * math.cos(2 * math.pi * i / 4)
    bm = Image.new("L", (Wd, Ht), 0)
    shw, head = sis_man(ImageDraw.Draw(bm), i, sc, hs, hn, ap)
    HR = 2.5 * SC                      # head radius
    # head: own blob, tucked toward the boulder, thin gap to the torso and arms
    hm = Image.new("L", (Wd, Ht), 0)
    ImageDraw.Draw(hm).ellipse([P(head[0] - HR, head[1] - HR), P(head[0] + HR, head[1] + HR)], fill=255)
    # arms: bent, hands (palm blobs) flat on the boulder's left flank just outside its halo
    am = Image.new("L", (Wd, Ht), 0)
    hipc = W(hs, hn)
    for al, f in ((-14, 0.92), (-44, 0.62)):
        a = math.radians(al)
        ext = 0.5 * math.sin(2 * math.pi * i / 4) * (1 if al == -14 else -1)
        hxy = (cxy[0] - (rh + 1.7) * math.cos(a) + ext, cxy[1] - (rh + 1.7) * math.sin(a))
        st = (hipc[0] + f * (shw[0] - hipc[0]), hipc[1] + f * (shw[1] - hipc[1]))   # chest point on the torso axis
        el = ik(st, hxy, 5.4 * SC, 5.4 * SC, 1)
        a2 = Image.new("L", (Wd, Ht), 0)
        ad = ImageDraw.Draw(a2)
        line(ad, st, el, 2.0 * SC); line(ad, el, hxy, 2.0 * SC)
        ad.ellipse([P(hxy[0] - 2.0, hxy[1] - 2.0), P(hxy[0] + 2.0, hxy[1] + 2.0)], fill=255)
        a2.paste(0, mask=am.filter(ImageFilter.MaxFilter(17)))   # thin gap between the two arms
        am.paste(255, mask=a2)
    am.paste(0, mask=bm.filter(ImageFilter.MaxFilter(17)))
    am.paste(0, mask=hm.filter(ImageFilter.MaxFilter(17)))
    bm.paste(0, mask=hm.filter(ImageFilter.MaxFilter(17)))
    mm = Image.new("L", (Wd, Ht), 0)
    md = ImageDraw.Draw(mm)
    for L in (bm, am, hm): mm.paste(255, mask=L)
    t = i % 8
    if t < 5:   # sweat drop flicked off the head
        sx, sy = head[0] - 2.4 - 1.1 * t, head[1] - 3.0 + 0.2 * t * t
        md.ellipse([P(sx - .8, sy - .8), P(sx + .8, sy + .8)], fill=255)
    halo = Image.new("L", (Wd, Ht), 0)
    ImageDraw.Draw(halo).ellipse([P(cxy[0] - rh, cxy[1] - rh), P(cxy[0] + rh, cxy[1] + rh)], fill=255)
    mm.paste(0, mask=halo)
    g.paste(0, mask=halo)
    g.paste(0, mask=mm.filter(ImageFilter.MaxFilter(9)))
    bl = Image.new("L", (Wd, Ht), 0)
    bd = ImageDraw.Draw(bl)
    bd.ellipse([P(cxy[0] - ER, cxy[1] - ER), P(cxy[0] + ER, cxy[1] + ER)], fill=255)
    bl.paste(0, mask=mm.filter(ImageFilter.MaxFilter(9)))
    base = math.radians(15 * i)  # clockwise; 3-fold notch pattern, 10 deg short of closing is avoided: 16*15 = 240 = 2 * 120
    for k in range(3):
        a = base + math.radians(120 * k)
        nx, ny = cxy[0] + 8.2 * math.cos(a), cxy[1] + 8.2 * math.sin(a)
        bd.ellipse([P(nx - .9, ny - .9), P(nx + .9, ny + .9)], fill=0)
        a2 = a + math.radians(60)
        nx, ny = cxy[0] + 3.6 * math.cos(a2), cxy[1] + 3.6 * math.sin(a2)
        bd.ellipse([P(nx - .6, ny - .6), P(nx + .6, ny + .6)], fill=0)
    m = g.copy()
    m.paste(255, mask=mm)
    m.paste(255, mask=bl)
    return m

def frame(i):
    if VARIANT == "sisyphus-endless":
        return to_img(frame_endless(i))
    rx, fx, mode = T[i]
    ry = rock_y(rx)
    if mode.startswith("tumble") and mode.count(":") > 2:
        ry -= float(mode.split(":")[3])  # boulder hops over him
    if VARIANT == "circusphus":
        return to_img(frame_circus(i, rx, fx, mode, ry))
    m = Image.new("L", (100 * K, 36 * K), 0)
    d = ImageDraw.Draw(m)
    d.polygon([P(0, Y0), P(88, Y1), P(96, Y1), P(100, Y1 + 3), P(100, 36), P(0, 36)], fill=255)
    h = R + 0.9
    ang = rx / R + 0.6
    if mode.startswith("tumble"):
        ang = math.radians(float(mode.split(":")[1]) + 150)  # notch rolls with the boulder
        # the hill is never cut by the man: only the boulder layer gets his transparent outline
        g = m.copy()
        d.ellipse([P(rx - h, ry - h), P(rx + h, ry + h)], fill=0)
        mm = Image.new("L", (100 * K, 36 * K), 0)
        man(ImageDraw.Draw(mm), fx, mode, rx, ry)
        if mode.split(":")[1] != "90":
            mm.paste(0, mask=g)  # man stays out of the hill (the flat one lies on its surface)
        m.paste(255, mask=mm)
        bl = Image.new("L", (100 * K, 36 * K), 0)
        bd = ImageDraw.Draw(bl)
        bd.ellipse([P(rx - R, ry - R), P(rx + R, ry + R)], fill=255)
        bl.paste(0, mask=mm.filter(ImageFilter.MaxFilter(7 if mode.split(":")[1] == "90" else 2 * K + 1)))
        nx, ny = rx + 2.5 * math.cos(ang), ry + 2.5 * math.sin(ang)
        bd.ellipse([P(nx - .6, ny - .6), P(nx + .6, ny + .6)], fill=0)
        m.paste(255, mask=bl)
        d = ImageDraw.Draw(m)
    else:
        man(d, fx, mode, rx, ry)
        d.ellipse([P(rx - h, ry - h), P(rx + h, ry + h)], fill=0)
        d.ellipse([P(rx - R, ry - R), P(rx + R, ry + R)], fill=255)
        nx, ny = rx + 2.5 * math.cos(ang), ry + 2.5 * math.sin(ang)
        d.ellipse([P(nx - .6, ny - .6), P(nx + .6, ny + .6)], fill=0)
    if VARIANT == "surfingphus" and i == 12:
        sparkle(d, rx, ry)
    return to_img(m)

def to_img(m):
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
    NF = ENF if VARIANT == "sisyphus-endless" else 18
    frames = [frame(i) for i in range(NF)]
    os.makedirs(FD, exist_ok=True)
    for i, f in enumerate(frames):
        f.save(f"{FD}/{VARIANT}-frame-{i}.png")
    write_apng(frames, OUT + "/" + VARIANT + "-preview.png")
    Z = 6; cw, ch = 100 * Z + 20, 36 * Z + 28
    sheet = Image.new("RGB", (3 * cw, ((NF + 2) // 3) * ch), (160, 160, 160))
    dr = ImageDraw.Draw(sheet)
    try: fnt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except Exception: fnt = ImageFont.load_default()
    for i, f in enumerate(frames):
        cx, cy = (i % 3) * cw + 10, (i // 3) * ch + 24
        dr.text((cx, cy - 22), str(i), fill=(0, 0, 0), font=fnt)
        big = f.resize((100 * Z, 36 * Z), Image.NEAREST)
        sheet.paste(big, (cx, cy), big)
    sheet.save(SP + ("/contact.png" if VARIANT == "sisyphus" else "/contact-" + VARIANT + ".png"))
    if VARIANT != "sisyphus-endless":
        for i in (0, 17): print(i, T[i])
