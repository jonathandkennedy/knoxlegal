#!/usr/bin/env python3
"""Stamp city landing pages out of _template-city-probate.html.

Add a city to CITIES and run:  python3 pages/build.py
Each entry becomes pages/<slug>-probate-lawyer.html.
Point each Google Ads campaign's final URL at its own city page.
"""

from pathlib import Path

PHONE_DISPLAY = "(954) 738-4883"
PHONE_TEL = "+19547384883"

CITIES = [
    {
        "CITY": "Miami Beach",
        "CITY_SLUG": "miami-beach",
        "COUNTY": "Miami-Dade County",
        "COURT_LINE": "the Miami-Dade County Probate Division in Miami",
        "LOCAL_LINE": (
            "Many Miami Beach estates involve a condo or home owned by a family "
            "from out of state. That's ancillary probate — a Florida proceeding "
            "that runs alongside the home state's — and it's routine work for us. "
            "You won't need to fly in for it."
        ),
    },
    {
        "CITY": "Pompano Beach",
        "CITY_SLUG": "pompano-beach",
        "COUNTY": "Broward County",
        "COURT_LINE": "the Broward County Probate Division in Fort Lauderdale",
        "LOCAL_LINE": (
            "Pompano Beach and greater Broward County are full of homes owned by "
            "seasonal residents and out-of-state families. Whether your loved one "
            "lived here year-round or wintered here, we open and settle the "
            "Broward estate — usually without you needing to travel."
        ),
    },
]

HERE = Path(__file__).parent
template = (HERE / "_template-city-probate.html").read_text(encoding="utf-8")

for city in CITIES:
    html = template
    tokens = dict(city, PHONE_DISPLAY=PHONE_DISPLAY, PHONE_TEL=PHONE_TEL)
    for key, value in tokens.items():
        html = html.replace("{{%s}}" % key, value)

    leftover = [line for line in html.splitlines() if "{{" in line]
    if leftover:
        raise SystemExit(f"Unreplaced tokens for {city['CITY']}: {leftover}")

    out = HERE / f"{city['CITY_SLUG']}-probate-lawyer.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out}")
