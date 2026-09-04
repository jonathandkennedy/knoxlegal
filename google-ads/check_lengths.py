#!/usr/bin/env python3
"""Verify every ad asset in rsa-copy.md fits Google's character limits.

Run:  python3 google-ads/check_lengths.py
Asset lines are prefixed:  H| headline  D| description  C| callout
SN| structured snippet  SL| sitelink text  SLD| sitelink description
"""

import re
import sys
from pathlib import Path

LIMITS = {"H": 30, "D": 90, "C": 25, "SN": 25, "SL": 25, "SLD": 35}

md = (Path(__file__).parent / "rsa-copy.md").read_text(encoding="utf-8")
failures = []
count = 0

for line in md.splitlines():
    m = re.match(r"^(H|D|C|SN|SL|SLD)\|\s?(.*)$", line.strip())
    if not m:
        continue
    kind, text = m.group(1), m.group(2).rstrip()
    count += 1
    n = len(text)
    limit = LIMITS[kind]
    mark = "OK " if n <= limit else "OVER"
    print(f"{mark} {kind:>3} {n:>2}/{limit}  {text}")
    if n > limit:
        failures.append(text)

print(f"\n{count} assets checked.")
if failures:
    print(f"{len(failures)} OVER the limit — fix before pasting into Google Ads.")
    sys.exit(1)
print("All within Google Ads limits.")
