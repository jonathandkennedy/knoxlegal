# Knox Law — probate PPC funnel & landing hub

Rebuild of the paid-search funnel for Attorney Rachel Knox's Florida probate
practice. The original problem: campaigns bought expensive clicks (up to
~$106 CPC) but the phone rang with **wills-and-trusts shoppers**, and the
conversion tracking counted those wrong calls as wins — teaching Smart
Bidding to find more of them.

The fix is applied at every layer — **say "after a death" before the click,
after the click, and at hello** — and the landing side is now a full hub
(matching the `results.*` hub pattern) aimed at the firm's bigger matters:
contested estates, beneficiary representation, out-of-state/ancillary
probate, and complex administrations.

Wills/trusts visitors are no longer turned away: the firm genuinely offers
planning, so they get a warm hand-off (on-page note + a dedicated Planning
Ahead page) and are captured as **separately-tagged planning leads** that
never pollute probate ad conversions.

## What's in this repo

```
pages/
  build.py                     Assembles the hub from src/ (run: python3 pages/build.py)
  src/                         Design system, chrome, and page bodies
  assets/knox-legal-logo.png       Firm logo, full resolution (white-text variant)
  assets/knox-legal-logo-embed.png Optimized ~10 KB version embedded in every page

  — generated, ready to deploy —
  index.html                       Hub home: "What's happening in your family?" router
  probate-administration.html      Core service page
  probate-litigation.html          Estate disputes (bigger clients)
  beneficiary-representation.html  Heirs left in the dark (bigger clients)
  out-of-state-probate.html        Remote + ancillary probate (bigger clients)
  trust-administration.html        Trustees & trust beneficiaries
  estate-planning.html             Warm soft-lander for wills/trusts visitors
  miami-beach-probate-lawyer.html  City PPC page
  pompano-beach-probate-lawyer.html City PPC page

google-ads/
  rsa-copy.md                  Paste-ready RSA copy per ad group (limits verified)
  check_lengths.py             Verifies every asset fits Google's limits
  negative-keywords.txt        Tiered negative list (read the DO-NOT-ADD note)
  keywords.md                  Keywords, campaign structure, page↔ad-group mapping
  conversion-tracking.md       Count only qualified probate leads as conversions
  intake-call-script.md        10-second phone screen for the PPC line
```

## The hub

Mobile-first, self-contained files (~55–61 KB each, logo embedded, no
external CSS/JS/fonts — instant on cellular). Shared design system in
`pages/src/design.css`: navy/gold Knox brand, serif display type, the
logo's gold divider-with-dot motif, proof band, review cards, attorney
feature.

Every page carries:

- **Qualification without fear.** Probate pages open with "A loved one has
  passed away…" and call buttons say "For probate after a death" — while the
  wayfinder strip and the form's planning option warmly route planning
  visitors instead of rejecting them.
- **The situation form.** A required "Which best describes your situation?"
  dropdown. Probate answers submit as probate leads (`lp_form_submit`);
  the planning answer shows a friendly note and submits as a planning lead
  (`lp_planning_submit`) — captured, but never a probate conversion.
- **Bigger-client positioning** built on Rachel's real profile: practicing
  since 1997, UM School of Law, all Florida state & federal courts, known
  for hidden assets, title defects, creditor negotiations, probate
  litigation, and fully remote administration for out-of-state families.
- `dataLayer` events for GTM: `lp_call_click`, `lp_form_submit`,
  `lp_planning_interest`, `lp_planning_submit` (wiring table in
  `google-ads/conversion-tracking.md`).

The planning page (`estate-planning.html`) deliberately shows **no phone
number** — its header button and CTAs go to the form and knoxlegal.com, so
the PPC call line stays reserved for probate matters.

### Deploying

Mirror the other builds: host the hub on a subdomain such as
**results.knoxlegal.com** (CNAME the subdomain to the hosting, upload the
generated HTML files + nothing else — every page is self-contained), or a
folder like `knoxlegal.com/lp/`. All internal links are relative, so any
host path works. `index.html` is the hub root.

To add a city page (Fort Lauderdale, Boca Raton, Key Biscayne…): add an
entry to `CITIES` in `pages/build.py` and run `python3 pages/build.py`.

### Fill in before launch (search the files for these)

| Item | Where |
|------|-------|
| `[ATTORNEY PHOTO]` — Rachel's professional photo | `pages/src/attorney.html` |
| `[★ 5.0]` / review-count stat | `pages/src/stats.html` |
| Real Google reviews, quoted verbatim | `pages/src/reviews.html` |
| `[FIRM STREET ADDRESS…]` (FL Bar ad rules want an office location) | `pages/src/footer.html` |
| `FORM_ENDPOINT` — where forms POST (WPForms webhook, Formspree, Zapier → Clio Grow/Lawmatics…) | `pages/src/script.html` |
| ~~GTM container snippet~~ **Done** — `GTM-W38VB5SN` is embedded in every page (GA4 `G-RTZXGQX46B`, Ads `AW-16979216728`) | wire the triggers per `google-ads/conversion-tracking.md` |
| Fee copy — "fees paid from the estate", "fees from the estate or recovery" | page bodies + `rsa-copy.md`; **attorney must confirm** |

Then rebuild: `python3 pages/build.py`.

**Rachel must review before launch** — the pages are written to general
Florida probate practice (Fla. Stat. chs. 733/735) and standard advertising
disclaimers, and her bio facts come from knoxlegal.com — but she owns Bar
compliance (Rule 4-7) and every claim made in her name.

## Launch order (by ROI, not by effort)

1. **Today, 15 min — negatives + demote the call conversion.** Paste Tier 1
   of `negative-keywords.txt` on both campaigns; demote raw "calls from
   ads" to Secondary. These two moves stop the bleeding first.
2. **This week — swap the ad copy.** `rsa-copy.md`, including removing
   `{KeyWord:}` insertion and pointing Pompano ads at the Pompano page.
3. **Launch the hub** with GTM + `FORM_ENDPOINT` wired; set each ad group's
   final URL per the mapping in `keywords.md`.
4. **Brief whoever answers (954) 738-4883** on `intake-call-script.md` and
   start the call sheet.
5. **Weekly, 10 min** — search-terms review (`keywords.md`) and the
   qualified-call upload (`conversion-tracking.md`).
6. **When ready to grow** — turn on the Estate Disputes and Out-of-State
   campaigns (`keywords.md`): the highest-value cases in this practice.
