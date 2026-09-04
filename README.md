# Knox Law — probate PPC funnel rebuild

Rebuild of the paid-search funnel for the probate campaigns. The problem
being solved: the campaigns buy expensive clicks (up to ~$106 CPC) but the
phone rings with **wills-and-trusts shoppers**, not probate cases. Every
layer of the old funnel — keywords, ad copy with `{KeyWord:}` insertion, a
"Protect Valuable Estate Assets" landing page, an unqualified form, and a
bare tap-to-call number — spoke estate-planning language, and the conversion
tracking then counted those wrong calls as wins, teaching Smart Bidding to
find more of them.

The fix is one idea applied at every layer: **say "after a death" before the
click, after the click, and at hello.**

## What's in this repo

```
pages/
  _template-city-probate.html    Master landing page template ({{TOKEN}}s)
  build.py                       Stamps city pages from the template
  assets/knox-legal-logo.png     Firm logo, full resolution (white-text variant)
  assets/knox-legal-logo-embed.png   Optimized ~10 KB version build.py embeds
  miami-beach-probate-lawyer.html    Generated — ready to deploy
  pompano-beach-probate-lawyer.html  Generated — ready to deploy
google-ads/
  rsa-copy.md                    Paste-ready RSA headlines/descriptions/assets
  check_lengths.py               Verifies every asset fits Google's limits
  negative-keywords.txt          Tiered negative list (read the DO-NOT-ADD note)
  keywords.md                    Keyword plan + campaign restructure + weekly ritual
  conversion-tracking.md         Stop counting wills callers as conversions
  intake-call-script.md          10-second phone screen for the PPC line
```

## The landing pages

Mobile-first, self-contained single files (no external CSS/JS/fonts, and the
Knox Law logo is embedded inline — each page is ~58 KB total and loads
instantly on cellular, which most of this traffic is). Each page:

- **Qualifies in the first screen:** H1 "Miami Beach Probate Lawyer" +
  "A loved one has passed away…" — no "protect your assets" language anywhere.
- **Fences the phone number:** every call button carries "Probate after a
  death only," including the sticky mobile bar.
- **Fences the form:** a required "Which best describes your situation?"
  dropdown. The "I need a will or living trust written" option politely
  routes the visitor to knoxlegal.com and **never reaches probate intake**
  (and fires a `lp_planning_deflected` analytics event so wrong-intent
  volume is measurable).
- **Sells the actual service:** summary vs. formal administration, letters
  of administration, the 3-month creditor window, ancillary probate for
  out-of-state families — the things a real probate client recognizes.
- Pushes `lp_form_submit` / `lp_call_click` / `lp_planning_deflected` to
  `dataLayer` for GTM (wiring table in `google-ads/conversion-tracking.md`).

### Deploying next to the WordPress site

Easiest: upload the two generated HTML files via hosting file manager (or
SFTP) into a folder like `/lp/`, giving URLs such as
`knoxlegal.com/lp/miami-beach-probate-lawyer.html`, and point each
campaign's final URL at its own city page. They're standalone files — no
WordPress theme, plugins, or header/footer involved (that's deliberate: no
nav menu = no leak paths off the page).

Alternative: rebuild inside Elementor using these files as the exact spec
(section order, copy, and the form logic must survive the port — especially
the dropdown-first form and the deflection behavior).

To add more cities (Fort Lauderdale, Boca Raton…): add an entry to `CITIES`
in `pages/build.py` and run `python3 pages/build.py`.

### Fill in before launch (search the files for these)

| Item | Where |
|------|-------|
| `[ATTORNEY NAME]`, `[ATTORNEY PHOTO]`, bio line | trust section of each page |
| `[FIRM STREET ADDRESS…]` (FL Bar ad rules want an office location) | footer |
| `FORM_ENDPOINT` — where the form POSTs (WPForms webhook, Formspree, Zapier → Clio Grow/Lawmatics…) | `<script>` at the bottom of each page |
| GTM container snippet | marked comment in `<head>` and after `<body>` |
| Fee copy — "fees paid from the estate" and "Fees Often Estate-Paid" | pages + `rsa-copy.md`; **attorney must confirm** |

**Have the attorney review the pages before launch** — they're written to
general Florida probate practice (Fla. Stat. chs. 733/735) and standard
advertising disclaimers, but she owns Bar compliance (Rule 4-7) and every
factual claim made in her name.

## Launch order (by ROI, not by effort)

1. **Today, 15 min — negatives + demote the call conversion.** Paste Tier 1
   of `negative-keywords.txt` as a shared list on both campaigns; demote raw
   "calls from ads" to a Secondary conversion. These two moves stop the
   bleeding before anything else ships.
2. **This week — swap the ad copy.** `rsa-copy.md`, including removing
   `{KeyWord:}` insertion and fixing the Pompano→Miami URL mismatch.
3. **Launch the two landing pages** with GTM + form endpoint wired, final
   URLs updated per campaign.
4. **Brief whoever answers (954) 738-4883** on `intake-call-script.md` and
   start the call sheet.
5. **Weekly, 10 min — search-terms review** (`keywords.md`) and the
   qualified-call upload (`conversion-tracking.md`).
