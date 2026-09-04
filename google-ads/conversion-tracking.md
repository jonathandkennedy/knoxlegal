# Conversion tracking — stop training Google to find wills callers

This is the highest-leverage fix in the whole project, and neither the ads
nor the landing page can compensate if it's skipped.

## The feedback loop that's hurting the account

If the campaigns use Smart Bidding (Max Conversions / tCPA) and the
conversion action is "calls from ads over 30/60 seconds," then every
wills-and-trusts caller who chats for a minute is recorded as a **success**.
Google's bidding then goes looking for *more people like that caller*. The
account isn't just failing to filter wrong-intent leads — it's actively
optimizing toward them, and paying up to ~$106 a click to do it.

## Target state

**Primary conversions (bid toward these only):**

1. **Qualified form submit** — the hub fires `lp_form_submit` into
   `dataLayer` only for probate situations. The planning option submits as
   a separate `lp_planning_submit` event (the visitor is welcomed and
   captured as a planning lead, not rejected), so the probate event is
   clean by construction.
2. **Qualified call** — a call the intake screen confirmed was probate
   (see `intake-call-script.md`). Two ways to get this into Google Ads,
   in order of preference:
   - **Offline conversion import:** intake logs every call in the call sheet;
     once a week, upload the probate-qualified calls (by call time + caller
     number, or GCLID if using a tracking platform). CallRail / CTM /
     WhatConvert automate this and can tag calls right after hang-up.
   - **Crude fallback:** keep Google call reporting but raise the
     conversion-counting threshold to **120+ seconds**. Wills callers being
     turned away by the screen script hang up well before that.

**Secondary conversions (observe, never bid toward):**

- `lp_call_click` — every tap on a phone link (volume signal only).
- Raw "calls from ads" — demote the existing action to Secondary **today**.
  This one change stops the wrong-lead feedback loop immediately, before
  anything else launches.

## GTM wiring for the hub (real IDs)

The stack, confirmed live in the firm's Tag Manager account:

| What | ID |
|---|---|
| GTM container (knoxlegal.com) | `GTM-W38VB5SN` — **already embedded in every hub page** |
| GA4 property | `G-RTZXGQX46B` |
| Google Ads account (conversions) | `AW-16979216728` |
| Google tag aliases | `GT-P8Z43H9R`, `GT-TNH9N58S` (same tag — no action needed) |

⚠️ **Audit the two existing tags firing to `AW-16979216728` first.** The
container currently sends two destinations into that Ads account — one of
them is almost certainly the conversion action that's been counting
wills/trusts calls as wins. Identify which conversion actions they feed,
and demote the raw-call one to Secondary before launching anything else.

The hub pages already push the events — in GTM, create Custom Event
triggers matching each event name, then:

| dataLayer event          | GTM trigger (Custom Event) | Send to                                   |
|--------------------------|----------------------------|-------------------------------------------|
| `lp_form_submit`         | `lp_form_submit`           | New Ads conversion "Probate case review — form" under `AW-16979216728` **(Primary)** + GA4 `G-RTZXGQX46B` |
| `lp_call_click`          | `lp_call_click`            | New Ads conversion "LP call click" (Secondary) + GA4 |
| `lp_planning_submit`     | `lp_planning_submit`       | GA4 + (optional) Secondary Ads conversion — a real lead for the firm, **never Primary** |
| `lp_planning_interest`   | `lp_planning_interest`     | GA4 only — someone picked "planning" in the dropdown |

Also make sure a **Conversion Linker** tag exists in the container (fires on
all pages) so click IDs survive to the conversion tags.

Each event carries `lp_page`, and probate submits carry `lead_type`
(open-probate / personal-rep / dispute / beneficiary / trust-admin), so
reports can split lead quality by campaign, page, and situation.

`lp_planning_interest` is the scoreboard for this whole effort: watch it
fall week over week as the negatives and new ad copy take hold — while
`lp_planning_submit` quietly hands the firm planning clients it would
otherwise have scared off.

## What "working" looks like

Within 2–3 weeks of (negatives + new RSAs + fenced pages + clean conversions):

- Cost per **qualified** lead becomes visible for the first time — expect it
  to look worse than the old $256/conversion number at first. That's honesty,
  not regression: the old number was counting wills callers as wins.
- Once ~15–20 qualified conversions accumulate, switch bidding to tCPA
  against the real number.
