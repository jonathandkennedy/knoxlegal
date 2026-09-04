#!/usr/bin/env python3
"""Assemble the Knox Law landing-page hub from pages/src/.

Run:  python3 pages/build.py
Each entry in PAGES (plus each city in CITIES) becomes a self-contained
HTML file at the REPO ROOT (so any static host — Vercel included — serves
the hub with zero routing config). Point each Google Ads ad group's final
URL at the page that matches its intent.
"""

import base64
import json
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "src"

PHONE_DISPLAY = "(954) 738-4883"
PHONE_TEL = "+19547384883"

# Firm logo (white-text variant for the navy header/footer), embedded as a
# data URI so each page stays one self-contained file. Full-resolution
# original: assets/knox-legal-logo.png. The -embed version is ~10 KB.
LOGO_URI = "data:image/png;base64," + base64.b64encode(
    (HERE / "assets" / "knox-legal-logo-embed.png").read_bytes()
).decode()

# Rachel's photo (background removed; full-res transparent cutout at
# assets/rachel-knox.png, circle-cropped ~31 KB version embedded below).
RACHEL_URI = "data:image/png;base64," + base64.b64encode(
    (HERE / "assets" / "rachel-knox-embed.png").read_bytes()
).decode()

CALL_CTA = (
    '<a href="tel:{{PHONE_TEL}}" class="js-call">{{PHONE_DISPLAY}}</a>'
    "<small>{{CALL_NOTE}}</small>"
)
SITE_CTA = (
    '<a href="https://knoxlegal.com/">knoxlegal.com</a>'
    "<small>The firm&rsquo;s main site</small>"
)
STICKY_BAR = """<div class="sticky-bar" aria-label="Quick actions">
  <a class="s-call js-call" href="tel:{{PHONE_TEL}}">Call now<small>{{CALL_NOTE}}</small></a>
  <a class="s-form" href="#case-review">{{STICKY_FORM_LABEL}}<small>2-minute form</small></a>
</div>"""

DEFAULTS = {
    "HEADER_CTA": CALL_CTA,
    "STICKY": STICKY_BAR,
    "CALL_NOTE": "Probate &amp; estate matters",
    "STICKY_FORM_LABEL": "Free case review",
    "FORM_TITLE": "Start Your Free Case Review",
    "FORM_SUB": (
        "Tell us a little about the situation. We'll tell you exactly what the "
        "process looks like, what it involves, and what it costs."
    ),
    "FORM_PLACEHOLDER": (
        "e.g., My father passed in March. He owned a condo in Miami and had "
        "accounts at two banks. There is a will."
    ),
    "FORM_BUTTON": "Request My Free Case Review",
    "ON_INDEX": "", "ON_RESULTS": "", "ON_ADMIN": "", "ON_LIT": "",
    "ON_BEN": "", "ON_OOS": "", "ON_TRUST": "", "ON_PLAN": "",
    "DKI_JSON": "null",
}


def city_dki(city, county):
    """Whitelisted headline variants for a city page, keyed by substrings of
    the bidded keyword (first match wins). Ads pass the keyword via the
    Final URL suffix kw={keyword:probate} — see google-ads/keywords.md."""
    return json.dumps({
        "rules": [
            ["personal representative", "prep"],
            ["executor", "prep"],
            ["letters of administration", "letters"],
            ["summary administration", "summary"],
            ["formal administration", "formal"],
            ["estate administration", "estate_admin"],
            ["without a will", "no_will"],
            ["no will", "no_will"],
            ["attorney", "attorney"],
        ],
        "variants": {
            "attorney": {"h1": f"{city} Probate Attorney"},
            "prep": {
                "h1": f"{city} Probate — Help for Personal Representatives",
                "lead": ("Named personal representative or executor? We handle "
                         "the filings, the deadlines, and the court — you make "
                         "the decisions that matter."),
            },
            "letters": {
                "h1": f"Letters of Administration in {county}",
                "lead": ("The court document banks and title companies ask "
                         "for. Getting it issued is one of the first things we "
                         "do when we open the estate."),
            },
            "summary": {"h1": f"Summary Administration in {county}"},
            "formal": {"h1": f"Formal Administration in {county}"},
            "estate_admin": {"h1": f"{city} Estate Administration Lawyer"},
            "no_will": {
                "h1": f"No Will? {city} Probate, Handled.",
                "lead": ("Florida's intestacy law decides who inherits — the "
                         "estate still goes through probate, and we handle "
                         "every step for the family."),
            },
        },
    })


LITIGATION_DKI = json.dumps({
    "rules": [
        ["contest", "contest"],
        ["undue influence", "undue"],
        ["remove", "remove_exec"],
        ["inheritance", "inheritance"],
        ["trust litigation", "trust_lit"],
    ],
    "variants": {
        "contest": {"h1": "Contesting a Will in Florida Is a Race Against the Clock."},
        "undue": {"h1": "Undue Influence Claims, Investigated and Proven."},
        "remove_exec": {"h1": "Removing an Executor Who Shouldn't Be in Charge."},
        "inheritance": {"h1": "Your Inheritance Is Worth Defending."},
        "trust_lit": {"h1": "When the Fight Is Over a Trust, Not a Will."},
    },
})

OOS_DKI = json.dumps({
    "rules": [
        ["ancillary", "ancillary"],
        ["out of state", "oos"],
        ["non resident", "oos"],
        ["inherited", "inherited"],
    ],
    "variants": {
        "ancillary": {"h1": "Florida Ancillary Probate, Handled Remotely."},
        "oos": {"h1": "Florida Probate for Out-of-State Families."},
        "inherited": {"h1": "Inherited Florida Property? We Settle It From Here."},
    },
})

PAGES = [
    {
        "out": "index.html",
        "body": "body-index.html",
        "SLUG": "hub-home",
        "TITLE": "Florida Probate & Estate Administration | Knox Law",
        "META_DESC": (
            "Probate administration, estate disputes, and trust matters across "
            "Florida — handled by Attorney Rachel Knox since 1997. Free case review."
        ),
        "ON_INDEX": ' class="on"',
    },
    {
        "out": "case-results.html",
        "body": "body-results.html",
        "SLUG": "case-results",
        "TITLE": "Results — Florida Estates Settled | Knox Law",
        "META_DESC": (
            "Estates administered, will contests resolved, assets recovered, "
            "titles cleared — nearly three decades of Florida probate results "
            "from Attorney Rachel Knox."
        ),
        "ON_RESULTS": ' class="on"',
    },
    {
        "out": "probate-administration.html",
        "body": "body-administration.html",
        "SLUG": "probate-administration",
        "TITLE": "Florida Probate Administration | Knox Law",
        "META_DESC": (
            "Summary and formal administration for Florida estates — letters of "
            "administration, creditor claims, property sales, distributions. "
            "Free case review."
        ),
        "ON_ADMIN": ' class="on"',
        "CALL_NOTE": "For probate after a death",
        "FORM_TITLE": "Start Your Probate Case Review",
        "FORM_SUB": (
            "Tell us a little about the estate. We'll tell you which type of "
            "Florida administration applies, what it involves, and what it costs."
        ),
    },
    {
        "out": "probate-litigation.html",
        "body": "body-litigation.html",
        "SLUG": "probate-litigation",
        "TITLE": "Florida Estate Disputes & Probate Litigation | Knox Law",
        "META_DESC": (
            "Will contests, undue influence, fiduciary misconduct, disputed "
            "assets. Deadlines can be 90 days or less — get a confidential case "
            "assessment now."
        ),
        "ON_LIT": ' class="on"',
        "DKI_JSON": LITIGATION_DKI,
        "CALL_NOTE": "Estate dispute matters",
        "STICKY_FORM_LABEL": "Case assessment",
        "FORM_TITLE": "Request a Confidential Case Assessment",
        "FORM_SUB": (
            "Estate disputes run on short statutory clocks. Tell us what's "
            "happening — we'll check the deadlines first and tell you where you "
            "stand."
        ),
        "FORM_PLACEHOLDER": (
            "e.g., My mother's will was changed three weeks before she passed "
            "and everything now goes to her caretaker."
        ),
        "FORM_BUTTON": "Request My Case Assessment",
    },
    {
        "out": "beneficiary-representation.html",
        "body": "body-beneficiary.html",
        "SLUG": "beneficiary-representation",
        "TITLE": "Beneficiary Representation in Florida Estates | Knox Law",
        "META_DESC": (
            "Heir left in the dark? Florida beneficiaries have a right to "
            "notice, inventories, accountings, and timely distributions. We "
            "enforce them."
        ),
        "ON_BEN": ' class="on"',
        "CALL_NOTE": "Estate &amp; inheritance matters",
        "FORM_TITLE": "Get a Free Beneficiary Case Review",
        "FORM_SUB": (
            "Tell us what the estate looks like from where you sit — the "
            "silence, the numbers that don't add up. We'll tell you what "
            "Florida law entitles you to."
        ),
        "FORM_PLACEHOLDER": (
            "e.g., My brother is the executor of Dad's estate. It's been a year "
            "and we've never seen an inventory."
        ),
    },
    {
        "out": "out-of-state-probate.html",
        "body": "body-oos.html",
        "SLUG": "out-of-state-probate",
        "TITLE": "Florida Probate for Out-of-State Families | Knox Law",
        "META_DESC": (
            "Settle a Florida estate from anywhere — full probate and ancillary "
            "administration handled remotely. Most clients never travel to "
            "Florida."
        ),
        "ON_OOS": ' class="on"',
        "DKI_JSON": OOS_DKI,
        "CALL_NOTE": "For probate after a death",
        "FORM_SUB": (
            "Tell us about the Florida property or accounts and where the "
            "family lives. We'll map the whole process — handled from our end, "
            "not yours."
        ),
        "FORM_PLACEHOLDER": (
            "e.g., We're in New York. Mom passed in June and owned a condo in "
            "Miami Beach plus a bank account down there."
        ),
    },
    {
        "out": "trust-administration.html",
        "body": "body-trust.html",
        "SLUG": "trust-administration",
        "TITLE": "Florida Trust Administration After a Death | Knox Law",
        "META_DESC": (
            "Successor trustee duties, beneficiary notices, accountings, and "
            "distributions under Florida law — guided start to finish. Free "
            "trust review."
        ),
        "ON_TRUST": ' class="on"',
        "CALL_NOTE": "Trust matters after a death",
        "STICKY_FORM_LABEL": "Free trust review",
        "FORM_TITLE": "Start a Free Trust Review",
        "FORM_SUB": (
            "Tell us about the trust and what's happened since the death. We'll "
            "tell you the duties, the deadlines, and the next step."
        ),
        "FORM_PLACEHOLDER": (
            "e.g., I'm the successor trustee of my father's living trust. The "
            "house is in the trust; I'm not sure what I'm required to send my "
            "sisters."
        ),
    },
    {
        "out": "estate-planning.html",
        "body": "body-planning.html",
        "SLUG": "estate-planning",
        "TITLE": "Wills, Trusts & Planning Ahead | Knox Law",
        "META_DESC": (
            "Planning ahead? Knox Law drafts customized wills, trusts, and "
            "guardianship arrangements — informed by thirty years of seeing "
            "plans tested in probate court."
        ),
        "ON_PLAN": ' class="on"',
        # Planning visitors are welcome — but the PPC phone line stays reserved
        # for probate, so this page routes to the form and the main site.
        "HEADER_CTA": SITE_CTA,
        "STICKY": "",
    },
]

CITIES = [
    {
        "out": "miami-beach-probate-lawyer.html",
        "SLUG": "miami-beach-probate-lawyer",
        "CITY": "Miami Beach",
        "COUNTY": "Miami-Dade County",
        "COURT_LINE": "the Miami-Dade County Probate Division in Miami",
        "LOCAL_LINE": (
            "Many Miami Beach estates involve a condo or home owned by a family "
            "from out of state. That's ancillary probate — a Florida proceeding "
            "that runs alongside the home state's — and it's routine work for "
            "us. You won't need to fly in for it."
        ),
    },
    {
        "out": "pompano-beach-probate-lawyer.html",
        "SLUG": "pompano-beach-probate-lawyer",
        "CITY": "Pompano Beach",
        "COUNTY": "Broward County",
        "COURT_LINE": "the Broward County Probate Division in Fort Lauderdale",
        "LOCAL_LINE": (
            "Pompano Beach and greater Broward County are full of homes owned "
            "by seasonal residents and out-of-state families. Whether your "
            "loved one lived here year-round or wintered here, we open and "
            "settle the Broward estate — usually without you needing to travel."
        ),
    },
]

for city in CITIES:
    PAGES.append({
        "out": city["out"],
        "body": "body-city.html",
        "SLUG": city["SLUG"],
        "TITLE": f"{city['CITY']} Probate Lawyer — Probate After a Death | Knox Law",
        "META_DESC": (
            f"A loved one has passed and the Florida estate needs to be opened. "
            f"Knox Law helps heirs and personal representatives with probate in "
            f"{city['COUNTY']}. Free case review."
        ),
        "CALL_NOTE": "For probate after a death",
        "FORM_TITLE": "Start Your Probate Case Review",
        "FORM_SUB": (
            "Tell us a little about the estate. We'll tell you which type of "
            "Florida administration applies, what it involves, and what it costs."
        ),
        "FORM_PLACEHOLDER": (
            f"e.g., My father passed in March. He owned a condo in "
            f"{city['CITY']} and had accounts at two banks. There is a will."
        ),
        "DKI_JSON": city_dki(city["CITY"], city["COUNTY"]),
        "CITY": city["CITY"],
        "COUNTY": city["COUNTY"],
        "COURT_LINE": city["COURT_LINE"],
        "LOCAL_LINE": city["LOCAL_LINE"],
    })

read = lambda name: (SRC / name).read_text(encoding="utf-8")

css = read("design.css")
partials = {
    "FORM": read("form.html"),
    "STATS": read("stats.html"),
    "REVIEWS": read("reviews.html"),
    "ATTORNEY": read("attorney.html"),
    "RESULTS": read("results.html"),
}
header = read("header.html")
footer = read("footer.html")
script = read("script.html")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- PPC landing hub. Keep noindex so it never competes with the main site's
     organic pages. Remove this tag only if you want the hub indexed. -->
<meta name="robots" content="noindex, nofollow">
<title>{{TITLE}}</title>
<meta name="description" content="{{META_DESC}}">

<!-- Google Tag Manager — knoxlegal.com container.
     This hub pushes dataLayer events: lp_call_click, lp_form_submit (probate),
     lp_planning_submit, lp_planning_interest — wiring table in
     google-ads/conversion-tracking.md. -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W38VB5SN');</script>
<!-- End Google Tag Manager -->

<style>
{{CSS}}
</style>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W38VB5SN"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

TAIL = """
</body>
</html>
"""

for page in PAGES:
    tokens = dict(DEFAULTS)
    tokens.update({k: v for k, v in page.items() if k not in ("out", "body")})
    tokens.update(
        PHONE_DISPLAY=PHONE_DISPLAY, PHONE_TEL=PHONE_TEL,
        LOGO_URI=LOGO_URI, RACHEL_URI=RACHEL_URI, CSS=css,
    )

    html = HEAD + header + read(page["body"]) + footer + script + TAIL

    # Multiple passes: partials and token values may themselves carry tokens.
    for _ in range(6):
        if "{{" not in html:
            break
        for key, value in partials.items():
            html = html.replace("{{%s}}" % key, value)
        for key, value in tokens.items():
            html = html.replace("{{%s}}" % key, value)

    leftover = sorted({
        line.strip()[:90] for line in html.splitlines() if "{{" in line
    })
    if leftover:
        raise SystemExit(f"Unreplaced tokens in {page['out']}: {leftover}")

    out = HERE.parent / page["out"]
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.name}  ({len(html)//1024} KB)")
