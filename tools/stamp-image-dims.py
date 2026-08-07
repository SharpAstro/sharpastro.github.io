"""Stamp every <img> in index.html with its file's real intrinsic width/height.

Why this exists: the images are `loading="lazy"`, and a lazy image with no declared size is a
ZERO-height box until it loads -- so the demo section's figure collapsed to its 1px border and
the screenshot simply was not there. Declared dimensions let the browser reserve the right
aspect-ratio box up front, which fixes that and removes the layout shift as each one arrives.

Re-run after replacing or re-capturing any screenshot; hand-written numbers go stale silently
(they already had -- three imgs carried 2880x1620 for files that were 1800x1160).

    python tools/stamp-image-dims.py
"""

import io
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "index.html")

IMG_TAG = re.compile(r'<img\s+[^>]*?src="(assets/img/[^"]+)"[^>]*?>', re.IGNORECASE)


def stamp(tag: str, src: str) -> str:
    path = os.path.join(ROOT, src.replace("/", os.sep))
    if not os.path.exists(path):
        print(f"  MISSING {src} -- left unstamped")
        return tag

    with Image.open(path) as im:
        w, h = im.size

    cleaned = re.sub(r'\s+(?:width|height)="\d+"', "", tag)
    # Insert right after the src attribute so the markup stays readable.
    stamped = cleaned.replace(f'src="{src}"', f'src="{src}" width="{w}" height="{h}"', 1)
    print(f"  {src}: {w}x{h}")
    return stamped


def main() -> int:
    html = io.open(PAGE, encoding="utf-8").read()
    print("stamping intrinsic dimensions:")
    out = IMG_TAG.sub(lambda m: stamp(m.group(0), m.group(1)), html)

    if out == html:
        print("no change")
        return 0

    io.open(PAGE, "w", encoding="utf-8", newline="").write(out)
    print(f"wrote {PAGE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
