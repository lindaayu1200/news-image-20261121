"""Entry for make.fun news-image-20261121.

Writes the bundled 1024x1024 entry image (a mosaic of the world's news
of Saturday 21 November 2026) to the output directory.
"""
import os
import shutil

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")  # judge writes here
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEST = os.path.join(OUT_DIR, "entry.png")
os.makedirs(os.path.dirname(DEST), exist_ok=True)
shutil.copyfile(SRC, DEST)
print("wrote", DEST, os.path.getsize(DEST), "bytes")
