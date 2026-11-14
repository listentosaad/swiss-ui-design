#!/usr/bin/env python3
"""Measure the "color power" of a screenshot: how much of the first viewport is flat, saturated
color or near-black, versus pale paper / washed-out tints.

    python3 -I scripts/color_power.py shot.png [--crop-h 900] [--paper-ground]

Needs Pillow only. Reads the top `crop-h` pixels (default: a 16:10 viewport for the image width),
so a full-page screenshot is judged by what the visitor sees first.

Counts per pixel (HSV):
  saturated  S >= 0.50 and V >= 0.35          flat strong color (yellow, red, blue, violet ...)
  black      V <= 0.14                         ink as a ground
  paper      S < 0.15 and V >= 0.80            white / cream / light grey
  tint       everything else                   pastels, mid greys, anti-aliasing, photo midtones
power = saturated + black.

Two modes, calibrated on real Swiss-style posters:
  default           ground looks (strong color ground, color bands, black ground): power >= 60%
                    (references measured 83-97%).
  --paper-ground    looks that keep a paper ground and carry color in the ink and a tinted panel
                    (violet ink, gig poster): paper <= 70%, i.e. at least 30% of the viewport is
                    not paper (references measured 35-59% non-paper).
"""
import argparse
import colorsys
import sys
from collections import Counter

from PIL import Image


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--crop-h", type=int, default=0, help="pixels from the top to judge (default: width*0.625)")
    ap.add_argument("--min", type=float, default=60.0, help="ground looks: minimum power %% (default 60)")
    ap.add_argument("--paper-ground", action="store_true", help="paper-ground looks: require >= 30%% non-paper instead")
    a = ap.parse_args()

    im = Image.open(a.image).convert("RGB")
    w, h = im.size
    ch = min(h, a.crop_h or round(w * 0.625))
    im = im.crop((0, 0, w, ch))
    scale = 260 / im.width
    im = im.resize((260, max(1, round(im.height * scale))), Image.BILINEAR)
    px = list(getattr(im, "get_flattened_data", im.getdata)())
    n = len(px)

    sat = blk = pap = 0
    buckets: Counter = Counter()
    for r, g, b in px:
        hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if v <= 0.14:
            blk += 1
        elif s >= 0.50 and v >= 0.35:
            sat += 1
        elif s < 0.15 and v >= 0.80:
            pap += 1
        buckets[(r >> 4, g >> 4, b >> 4)] += 1

    top = []
    hues = set()
    for (r, g, b), c in buckets.most_common(8):
        if c / n < 0.03:
            break
        rr, gg, bb = (r << 4) + 8, (g << 4) + 8, (b << 4) + 8
        hh, s, v = colorsys.rgb_to_hsv(rr / 255, gg / 255, bb / 255)
        if s >= 0.5 and v >= 0.35:
            hues.add(int(hh * 360 // 30))
        top.append(f"#{rr:02X}{gg:02X}{bb:02X} {100 * c / n:.0f}%")

    power = 100 * (sat + blk) / n
    print(f"viewport judged: {w}x{ch}")
    print(f"power {power:.0f}%  = saturated {100 * sat / n:.0f}% + black {100 * blk / n:.0f}%   "
          f"| paper {100 * pap / n:.0f}%  tint/other {100 * (n - sat - blk - pap) / n:.0f}%")
    print(f"strong hues (30-degree buckets): {len(hues)}   top flats: {', '.join(top)}")
    nonpaper = 100 - 100 * pap / n
    if a.paper_ground:
        ok = nonpaper >= 30
        msg = f"non-paper {nonpaper:.0f}% vs minimum 30%"
    else:
        ok = power >= a.min
        msg = f"power {power:.0f}% vs minimum {a.min:.0f}%"
    print(f"{'PASS' if ok else 'LOW'}: {msg}"
          + ("" if ok else "  -> make a strong color or ink the ground, enlarge the color planes, or tint the photo to the palette"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
