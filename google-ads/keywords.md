# Keyword & campaign structure plan — probate campaigns

## Restructure (one-time, ~20 minutes)

**Merge the duplicate ad groups.** Each campaign currently splits "Probate -
Attorney" and "Probate - Lawyer." Same intent, same page, same searcher — the
split just divides an already-small budget and slows learning. Merge into one
**Probate — Core** ad group per campaign, and add a second ad group only for
the personal-representative/executor theme:

```
Search - Probate - Miami Beach        (geo: Miami Beach + surrounds)
├── Probate — Core                    → pages/miami-beach-probate-lawyer.html
└── Probate — Personal Rep/Executor   → same page (RSA leads with "Named Personal Rep?")

Search - Probate - Pompano Beach      (geo: Pompano Beach + surrounds)
├── Probate — Core                    → pages/pompano-beach-probate-lawyer.html
└── Probate — Personal Rep/Executor   → same page
```

**Every campaign's final URL goes to its own city page.** Pompano clicks were
landing on the Miami Beach URL — that costs Quality Score and trust.

**Campaign settings to verify while you're in there:**

- Location targeting: **"Presence: in or regularly in"** — not "interest in."
  ("Interest" is how a New Yorker planning their own estate ends up clicking a
  Miami Beach ad. Note: genuine out-of-state heirs will search the city name
  and still match fine via the keyword.)
- **Search partners: off. Display Network expansion: off.** Both are junk-call
  sources at this budget.
- One ad shows a **~$106 average CPC** (13 clicks, ~$1,381). If bidding is Max
  Conversions with today's polluted conversion data, the machine is paying
  premium prices for wrong-intent calls. Until conversions are cleaned up
  (see `conversion-tracking.md`), run **Maximize Clicks with a CPC cap**
  (start ~$40–50 for this niche in South FL) or manual CPC.

## Keywords — Probate — Core (phrase + exact)

```
[probate lawyer]
[probate attorney]
[probate lawyer near me]
[probate attorney near me]
"probate lawyer miami beach"          ← city per campaign
"probate attorney miami beach"        ← city per campaign
"probate law firm"
"open probate florida"
"how to open probate in florida"
"file probate florida"
"filing probate in florida"
"estate administration attorney"
"estate administration lawyer"
"probate process florida"
"summary administration florida"
"formal administration florida"
"letters of administration florida"
"ancillary probate florida"
"probate court attorney"
"attorney for estate after death"
"lawyer to settle an estate"
"died without a will florida"
"no will probate florida"
```

## Keywords — Probate — Personal Rep/Executor

```
"personal representative attorney"
"personal representative florida"
"executor attorney"
"executor of estate attorney"
"attorney for executor florida"
"duties of personal representative florida"
"personal representative lawyer near me"
```

Skip broad match entirely until (a) the negative list has two clean weeks of
search terms behind it and (b) conversion tracking counts only qualified
leads. Broad + polluted conversions = paying Google to find more wills
callers.

## The weekly 10-minute ritual (this is where ROAS is actually won)

1. Campaigns → Insights & reports → **Search terms**, last 7 days.
2. Sort by cost. For each term ask one question: *"Has someone died in this
   query?"*
3. No → add the offending word/phrase to the shared negative list.
4. Yes but irrelevant (another state, DIY, records lookup) → negative it too.
5. Note any strong converting term → promote it to exact match in the ad group.

Expect the first two weeks to be ugly. At roughly $50 a click, every negative
added is real money saved on the next click that never happens.
