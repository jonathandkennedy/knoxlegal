# RSA copy — probate campaigns (paste-ready)

Copy for the responsive search ads in **Search - Probate - Miami Beach** and
**Search - Probate - Pompano Beach**. Every asset here fits Google's limits
(headlines ≤ 30 chars, descriptions ≤ 90) — verified by `check_lengths.py`.

**Before pasting, two changes to the existing ads:**

1. **Remove `{KeyWord:…}` insertion.** It mirrors whatever the searcher typed,
   so a "living trust attorney" query gets an ad that looks hand-written for
   living trusts. With wrong-intent queries still leaking in, DKI is a
   wrong-lead magnet. Static headlines below replace it.
2. **Expect Ad Strength to drop from "Excellent."** Pinning qualifier
   headlines lowers that score. Ignore it — Ad Strength is a variety
   suggestion, not Quality Score, and the current "Excellent" ads are
   excellently attracting the wrong callers.

## Headlines (pick up to 15 per ad)

Pin position 1 → the city headline. Pin position 2 → rotate only the
"after a death" qualifier set, so **every impression** says both where and
what. Leave the rest unpinned.

**Position 1 (city — use the campaign's own city):**

```
H| Miami Beach Probate Lawyer
H| Pompano Beach Probate Lawyer
```

**Position 2 (the qualifier set — pin all of these to position 2):**

```
H| Probate Help After a Death
H| Open a Florida Estate
H| Settle a Loved One's Estate
H| Estate Administration Help
```

**Unpinned (audience, service, CTA):**

```
H| For Executors & Heirs
H| Help for Personal Reps
H| Named Personal Rep? Call Us
H| Out-of-State Heirs Welcome
H| Summary & Formal Probate
H| We Handle the Court Filings
H| Letters of Administration
H| Florida Ancillary Probate
H| Free Probate Case Review
H| Probate Cases — Not Wills
```

## Descriptions (pick 4)

```
D| A loved one passed? We help heirs & personal reps open & settle the Florida estate.
D| Probate after a death — not will drafting. Filings, creditors & distributions handled.
D| Named executor? Clear next steps with costs quoted upfront. Free review, no obligation.
D| Out of state? We settle Florida estates without you traveling. Talk to a probate lawyer.
```

Pin the first description to position 1 if you want the qualifier guaranteed;
otherwise leave descriptions unpinned.

## Callout assets

```
C| Probate Cases Only
C| Free Case Review
C| Handled Without Travel
C| Direct Attorney Access
C| Court Deadlines Managed
C| Fees Often Estate-Paid
```

> "Fees Often Estate-Paid" — confirm the fee language with the attorney
> before enabling (same flag as the landing page fee copy).

## Structured snippet — header "Services"

```
SN| Formal Administration
SN| Summary Administration
SN| Ancillary Probate
SN| Creditor Claims
SN| Estate Distribution
```

## Sitelinks (point at landing page anchors)

```
SL| Start a Case Review
SLD| 2-minute qualifying form
SLD| No cost, no obligation
```
→ `…/miami-beach-probate-lawyer/#case-review`

```
SL| The FL Probate Process
SLD| Summary vs. formal, explained
SLD| Timelines and key deadlines
```
→ main page, facts section

```
SL| Fees & Who Pays
SLD| Costs quoted before filing
SLD| Often paid from the estate
```
→ FAQ section

```
SL| Out-of-State Families
SLD| Settle a FL estate remotely
SLD| Ancillary probate handled
```
→ facts section

## Growth campaign: Estate Disputes (→ probate-litigation.html / beneficiary-representation.html)

Headlines (pin a "dispute" headline to position 1):

```
H| FL Estate Dispute Lawyer
H| Contest a Will in Florida
H| Will Contest? Deadlines Run
H| Executor Not Cooperating?
H| Protect Your Inheritance
H| Undue Influence Claims
H| Remove a Bad Executor
H| We Trace Missing Assets
H| Nearly 30 Yrs in Probate
H| Confidential Case Review
```

Descriptions:

```
D| Will contests, undue influence & fiduciary misconduct. Deadlines can be 90 days — act now.
D| An executor who won't communicate is a warning sign. Know your heir rights. Free review.
D| Nearly 30 years fighting for fairness in Florida estates. Confidential case assessment.
D| Suspicious will? Vanishing assets? We investigate, freeze, and recover. Talk to us first.
```

## Growth campaign: Out-of-State Families (→ out-of-state-probate.html)

Headlines (pin "Florida Probate, From Afar" or "No Travel to Florida Needed" to position 2):

```
H| Florida Probate Lawyer
H| Florida Probate, From Afar
H| Settle a FL Estate Remotely
H| No Travel to Florida Needed
H| FL Ancillary Probate Help
H| Sell the FL Property Remotely
H| Out-of-State Heirs Welcome
H| We Handle It From Here
```

Descriptions:

```
D| Mom's condo in Florida? We open, administer & close the estate — you never board a plane.
D| Florida probate & ancillary administration handled remotely for out-of-state families.
D| E-filing, remote hearings, signatures near you. Florida probate without the travel.
D| Working with your home-state lawyer, we handle the Florida side. Free case review.
```

## Display path

Replace `{location(city)}` in the path with static, per-campaign paths that
match the final URL: `/probate/miami-beach` and `/probate/pompano-beach`.
Cosmetic, but it keeps message match tight and stops path/query mismatches.

## Call assets — important

Calls placed from a **call asset never see the landing page**, so none of the
page's qualification applies to them. If wills/trusts calls persist after the
copy swap, pause call assets on these campaigns for two weeks and force every
click through the fenced page — then re-add them with the intake screen
(`intake-call-script.md`) firmly in place.
