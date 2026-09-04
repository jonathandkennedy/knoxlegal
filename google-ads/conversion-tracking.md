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

1. **Qualified form submit** — the landing page fires `lp_form_submit` into
   `dataLayer` only for probate situations. The planning option never
   submits (those visitors see a polite redirect and fire
   `lp_planning_deflected` instead), so this event is clean by construction.
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

## GTM wiring for the new landing pages

The pages already push these events — just add the GTM container snippet
(marked spot in the `<head>`) and create:

| dataLayer event          | GTM trigger (Custom Event) | Send to                                   |
|--------------------------|----------------------------|-------------------------------------------|
| `lp_form_submit`         | `lp_form_submit`           | Google Ads conversion **(Primary)** + GA4 |
| `lp_call_click`          | `lp_call_click`            | Google Ads conversion (Secondary) + GA4   |
| `lp_planning_deflected`  | `lp_planning_deflected`    | GA4 only — measures wrong-intent volume   |

Each event carries `lp_city`, and form submits carry `lead_type`
(open-probate / personal-rep / dispute / trust-admin), so reports can split
lead quality by campaign and by situation.

`lp_planning_deflected` doubles as the scoreboard for this whole effort:
watch it fall week over week as the negatives and new ad copy take hold.

## What "working" looks like

Within 2–3 weeks of (negatives + new RSAs + fenced pages + clean conversions):

- Cost per **qualified** lead becomes visible for the first time — expect it
  to look worse than the old $256/conversion number at first. That's honesty,
  not regression: the old number was counting wills callers as wins.
- Once ~15–20 qualified conversions accumulate, switch bidding to tCPA
  against the real number.
