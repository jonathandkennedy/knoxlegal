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

## Branch B — wills / trusts / estate planning (NOT this campaign)

Stay warm — this person may be a probate client in the future, and their
review of the firm matters. But do not book them into the probate pipeline:

> "Thank you — this particular line is reserved for families handling an
> estate after a loss, so I can't book that here. For wills and trusts, the
> best way to reach the firm is through knoxlegal.com [or the firm's
> planning intake email/number]. They'll take great care of you."

Log the call as **PLANNING — NOT QUALIFIED**. Never uploaded as an ads
conversion.

> Decision for the firm: if she *wants* planning work at normal (non-PPC)
> acquisition cost, give Branch B a real handoff (transfer or callback list)
> — just keep it out of the ads conversion upload either way.

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
