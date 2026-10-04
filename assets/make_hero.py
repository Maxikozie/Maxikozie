"""Generates hero.svg: a self-drawing topographic contour map.

    python assets/make_hero.py
"""

import sys
from pathlib import Path

import numpy as np
from skimage.measure import find_contours

W, H = 1200, 420
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 4
LEVELS = 22
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_name("hero.svg")


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


def main() -> None:
    z = terrain(np.random.default_rng(SEED))
    levels = np.linspace(z.min(), z.max(), LEVELS + 2)[1:-1]

    paths, longest = [], (0, "")
    for i, lv in enumerate(levels):
        index = i % 5 == 4  # every fifth line is an index contour, like on a real map
        for c in find_contours(z, lv):
            if len(c) < 12:
                continue
            d = to_path(c)
            cls = "c i" if index else "c"
            paths.append(f'<path class="{cls}" style="--d:{i * 0.07:.2f}s" pathLength="1" d="{d}"/>')
            closed = np.allclose(c[0], c[-1])
            if closed and i >= LEVELS // 3 and len(c) > longest[0]:
                longest = (len(c), d)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none">
<style>
  svg {{ --ink: #1f2328; --muted: #656d76; --line: #8c959f; --accent: #1a7f37; }}
  @media (prefers-color-scheme: dark) {{
    svg {{ --ink: #e6edf3; --muted: #8b949e; --line: #6e7681; --accent: #3fb950; }}
  }}
  .c {{ stroke: var(--line); stroke-width: 1; opacity: .55; stroke-linejoin: round; }}
  .c.i {{ stroke-width: 1.6; opacity: .9; }}
  .t {{ stroke: var(--accent); stroke-width: 2.4; stroke-linecap: round; stroke-dasharray: .05 .95; stroke-dashoffset: 1; }}
  .name {{ fill: var(--ink); font: 600 64px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; letter-spacing: -1px; }}
  .tag {{ fill: var(--muted); font: 24px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
  .scale {{ fill: var(--muted); font: 18px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
  .bar {{ stroke: var(--muted); stroke-width: 1.5; }}
  @media (prefers-reduced-motion: no-preference) {{
    .c {{ stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw 2.6s cubic-bezier(.4,0,.2,1) var(--d) forwards; }}
    .t {{ animation: trace 14s linear 3.2s infinite; }}
    .fade {{ opacity: 0; animation: in 1s ease .3s forwards; }}
  }}
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
<path class="t" pathLength="1" d="{longest[1]}"/>
</g>
<g class="fade">
  <text class="name" x="64" y="200">maxikozie</text>
  <text class="tag" x="66" y="248">small tools, mostly built because</text>
  <text class="tag" x="66" y="282">I wanted them to exist.</text>
  <path class="bar" d="M66 352v8h120v-8M126 356v4"/>
  <text class="scale" x="61" y="388">0</text>
  <text class="scale" x="138" y="388">1 weekend</text>
</g>
</svg>
"""
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB, {len(paths)} paths)")


if __name__ == "__main__":
    main()
