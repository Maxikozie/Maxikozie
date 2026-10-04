"""Draws the profile hero: a self-drawing topographic contour map.

A new landscape every day: the date is the random seed. Writes a light and a
dark variant so the README can pick the one matching the viewer's GitHub theme.

    python assets/make_hero.py                    # today's map, into ./dist
    python assets/make_hero.py --date 2026-10-04  # any day's map
"""

import argparse
import datetime as dt
from pathlib import Path

import numpy as np
from skimage.measure import find_contours

W, H = 1200, 420
LEVELS = 22
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "light": {"ink": "#1f2328", "muted": "#656d76", "line": "#8c959f", "accent": "#1a7f37"},
    "dark": {"ink": "#e6edf3", "muted": "#8b949e", "line": "#6e7681", "accent": "#3fb950"},
}


def terrain(rng: np.random.Generator) -> np.ndarray:
    ys, xs = np.mgrid[0:H:2, 0:W:2].astype(float)
    z = np.zeros_like(xs)
    # a few hills, weighted to the right so the text side stays calm
    for _ in range(6):
        cx = rng.uniform(0.5, 0.98) * W
        cy = rng.uniform(0.1, 0.9) * H
        sx, sy = rng.uniform(50, 150), rng.uniform(45, 120)
        z += rng.uniform(0.5, 1.0) * np.exp(-((xs - cx) ** 2 / (2 * sx**2) + (ys - cy) ** 2 / (2 * sy**2)))
    # low-frequency ripple so lines don't look like perfect ellipses
    for _ in range(4):
        fx, fy = rng.uniform(0.004, 0.012, 2)
        z += 0.06 * np.sin(xs * fx + rng.uniform(0, 6)) * np.cos(ys * fy + rng.uniform(0, 6))
    return z


def to_path(c: np.ndarray, step: int = 3) -> str:
    pts = c[::step]
    if len(c) and not np.array_equal(pts[-1], c[-1]):
        pts = np.vstack([pts, c[-1]])
    coords = [f"{x * 2:.1f},{y * 2:.1f}" for y, x in pts]
    return f"M{coords[0]}L" + " ".join(coords[1:])


def contours(seed: int) -> tuple[list[str], str]:
    z = terrain(np.random.default_rng(seed))
    levels = np.linspace(z.min(), z.max(), LEVELS + 2)[1:-1]

    paths, trace, fallback = [], (0, ""), (0, "")
    for i, lv in enumerate(levels):
        index = i % 5 == 4  # every fifth line is an index contour, like on a real map
        for c in find_contours(z, lv):
            if len(c) < 12:
                continue
            d = to_path(c)
            cls = "c i" if index else "c"
            paths.append(f'<path class="{cls}" style="animation-delay:{i * 0.07:.2f}s" pathLength="1" d="{d}"/>')
            # the green trace loops around a hill; fall back to any long line if no hill closes
            if i >= LEVELS // 3 and len(c) > trace[0] and np.allclose(c[0], c[-1]):
                trace = (len(c), d)
            if len(c) > fallback[0]:
                fallback = (len(c), d)
    return paths, (trace if trace[0] else fallback)[1]


def render(paths: list[str], trace: str, day: dt.date, t: dict[str, str]) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none">
<style>
  .c {{ stroke: {t["line"]}; stroke-width: 1; opacity: .55; stroke-linejoin: round;
        stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw 2.6s cubic-bezier(.4,0,.2,1) forwards; }}
  .c.i {{ stroke-width: 1.6; opacity: .9; }}
  .t {{ stroke: {t["accent"]}; stroke-width: 2.4; stroke-linecap: round; stroke-dasharray: .05 .95;
        stroke-dashoffset: 1; animation: trace 14s linear 3.2s infinite; }}
  .name {{ fill: {t["ink"]}; font: 600 64px {FONT}; letter-spacing: -1px; }}
  .tag {{ fill: {t["muted"]}; font: 24px {FONT}; }}
  .small {{ fill: {t["muted"]}; font: 18px {FONT}; }}
  .bar {{ stroke: {t["muted"]}; stroke-width: 1.5; }}
  .fade {{ opacity: 0; animation: in 1s ease .3s forwards; }}
  @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
  @keyframes trace {{ to {{ stroke-dashoffset: -1; }} }}
  @keyframes in {{ to {{ opacity: 1; }} }}
</style>
<defs>
  <linearGradient id="g" x1="0" x2="1" y1="0" y2="0">
    <stop offset=".28" stop-color="#fff" stop-opacity="0"/>
    <stop offset=".62" stop-color="#fff" stop-opacity="1"/>
  </linearGradient>
  <mask id="m"><rect width="{W}" height="{H}" fill="url(#g)"/></mask>
</defs>
<g mask="url(#m)">
{chr(10).join(paths)}
<path class="t" pathLength="1" d="{trace}"/>
</g>
<g class="fade">
  <text class="small" x="66" y="120">sheet {day.isoformat()}</text>
  <text class="name" x="64" y="192">maxikozie</text>
  <text class="tag" x="66" y="238">terrain changes daily.</text>
  <path class="bar" d="M66 296v8h120v-8M126 300v4"/>
  <text class="small" x="61" y="332">0</text>
  <text class="small" x="138" y="332">1 weekend</text>
</g>
</svg>
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", type=dt.date.fromisoformat, default=dt.datetime.now(dt.timezone.utc).date())
    ap.add_argument("--out", type=Path, default=Path("dist"))
    args = ap.parse_args()

    paths, trace = contours(int(args.date.strftime("%Y%m%d")))
    args.out.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        f = args.out / f"hero-{name}.svg"
        f.write_text(render(paths, trace, args.date, theme), encoding="utf-8")
        print(f"wrote {f} ({f.stat().st_size / 1024:.0f} KB, {len(paths)} paths)")


if __name__ == "__main__":
    main()
