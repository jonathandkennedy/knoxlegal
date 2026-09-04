# Intake call script — 10-second screen for the PPC line

Mobile PPC callers tap the number before reading the page. The receptionist
is therefore the last, most reliable qualification layer — and the source of
the "qualified call" conversions in `conversion-tracking.md`. Print this.

## The screen (first 10 seconds)

> "Thank you for calling Knox Law. So I get you to the right person —
> are you calling about the **estate of someone who has passed away**, or
> about **setting up a will or trust for yourself**?"

Every caller gets this question before anything else. It sorts everyone.

## Branch A — someone has passed (QUALIFIED · probate)

> "I'm so sorry for your loss. Let me take a few details so the attorney can
> review your situation before you speak."

Capture:

1. Caller's name, callback number, email
2. Relationship to the person who passed
3. Decedent's name and **date of passing**
4. **County/city where they lived** (routes Miami-Dade vs. Broward)
5. Was there a will? (either answer is fine — "no will" is still our case)
6. Rough picture of assets: home/condo? bank or investment accounts?
   Anything already saying "beneficiary" on it?
7. Has anything been filed with a court yet?

Close:

> "Thank you. [Attorney] reviews these personally — you'll hear from us by
> [today/tomorrow]. If a bank or title company gave you paperwork or asked
> for 'letters of administration,' have that handy for the call."

Log the call as **PROBATE — QUALIFIED** in the call sheet.

## Branch B — wills / trusts / estate planning (welcome them — separate lane)

The firm does help families plan ahead (customized wills, trusts, and
guardianship arrangements), so treat this caller as a real prospective
client — just not a probate one. Warm, no rejection:

> "Wonderful — planning ahead is exactly what Rachel recommends. Let me
> take your name and number and the firm will reach out about wills and
> trusts. You can also read about it at knoxlegal.com."

Capture: name, callback number, email, what they're interested in
(will / trust / guardianship / not sure). Route to the firm's planning
callback list — **not** the probate case-review pipeline.

Log the call as **PLANNING — NOT AN ADS CONVERSION**. These calls are real
leads for the firm, but they are never uploaded to Google Ads: uploading
them would re-teach Smart Bidding to hunt for planning callers, which is
the exact problem this whole system fixes.

## Branch C — everything else (records lookups, DIY form help, agents/investors, jobs)

> "That's outside what this line handles — I'd check [county probate court /
> knoxlegal.com] for that."

Log as **OTHER — NOT QUALIFIED**.

## The call sheet (feeds the weekly conversion upload)

| Date/time | Caller | Number | Branch (A/B/C) | County | Notes | Uploaded to Ads? |
|-----------|--------|--------|----------------|--------|-------|------------------|

Weekly: Branch A rows → offline conversion import (or tag in CallRail).
Branch B/C rows → never. The Branch B count per week is also your live
measure of how much wrong-intent traffic the ads are still buying.
