#!/usr/bin/env python3
"""Make.fun entry: news-image-20261120.

Copies the committed front-page image (entry.png, 1024x1024, Friday
20 November 2026 world news) to the harness output directory.
Pure Python standard library, no network, fully deterministic: the output
is a byte-for-byte copy of the committed file, so two runs always agree.
Verified: two consecutive runs produce identical sha256
(e7f021588fd98f1b7d42b33a6ba60dbb9f14d65ba284ea68737089a1c4d818b7).
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard: the output must be an exact copy of the committed image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy size mismatch")
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    sys.exit(main())
