# Review: SBA Research Memo

**Verdict: YELLOW**

The memo is structurally strong and gets the conceptual architecture (EPC/OC, 7(a) vs. 504, blanket-lien tiers, PG matrix, TIC mortgage mechanics) substantially right. However, it contains at least three factual errors that need correcting before this memo drives any deal decisions, plus several overstatements and meaningful gaps relative to the user's actual fact pattern.

---

## Verified accurate

- §120.110(c) passive-landlord ineligibility framing
- §120.111(a)(1) use-of-proceeds limitation
- §120.111(a)(3) assignment of rents
- §120.111(a)(5) OC must be co-borrower (7(a)) or guarantor
- §120.111(b) EPC and OC cannot be parent/subsidiary of each other
- §120.160(a) 20% PG threshold
- §120.111(a)(4) 20% PG rule applied across BOTH EPC and OC
- 7(a) blanket UCC-1 default for larger loans (directional concept)
- 504 50/40/10 baseline split
- 504 equity-injection escalators (10/15/20%)
- §120.882 prohibition on working capital under 504
- TIC mortgage mechanics
- Form 148 / 148L distinction
- §121.103 affiliation analysis applies

---

## Errors found

### 1. §120.111(a)(2) lease-term claim conflates regulation and SOP
- Memo: lease term "must be at least the loan term" cited to §120.111(a)(2)
- Actual: §120.111(a)(2) requires the EPC to lease 100% of the property to the OC. The lease-term-≥-loan-term and rent-cap rules come from **SOP 50 10**, not §120.111(a)(2).
- Fix: separate citations.

### 2. §120.160(c) hazard-insurance citation
- Memo: "Hazard insurance required on all collateral > $500,000 (13 CFR 120.160(c))"
- Actual: §120.160(c) requires hazard insurance on **all** collateral — no $500,000 threshold. The threshold concept is the SBA flood/appraisal threshold, not hazard.
- Fix: strike the "> $500,000" qualifier.

### 3. Blanket-lien threshold dollar figure
- Memo: "7(a) loan > $500,000" triggers blanket lien / personal-RE rule
- Actual: Current SOP 50 10 thresholds may be **$50K / $350K / above $350K** rather than $500K. Re-verify against current SOP.
- Practical conclusion correct (a $575K loan is above either threshold) but cited number is likely wrong.

### 4. Citizenship Policy Notice 5000-865754 — overstated
- Memo: flat statement that LPRs cannot own any percentage; cites "5% de minimis exception"
- Actual: notice tightened citizenship/residency requirements in March 2025, but:
  - The "5% de minimis exception" claim is not, to reviewer's knowledge, in the policy notice text itself
  - Treatment of LPRs went through revision; subsequent guidance/FAQs softened in some scenarios
- Fix: hedge — "The current operative rule on LPR ownership and any de minimis exception **must be confirmed by reviewing the latest version of the Policy Notice and any superseding SOP language**."

### 5. SOP version stale
- Memo: cites "SOP 50 10 7.1" multiple times
- Actual: **SOP 50 10 8** is current (effective June 1, 2025); SOP 50 10 7.1 was effective August 2023 and superseded.
- Fix: replace all references; re-verify pinpoints.

### 6. §120.130 prohibited-uses list
- Memo lists "Investments in real/personal property held for sale, lease, or investment (subject to EPC exception)" under §120.130
- Actual: passive-investment prohibition lives at §120.110, not §120.130. §120.130 lists prohibitions on uses of proceeds (refinancing, distributions to associates, etc.).

### 7. "TIC ownership = ownership of the EPC"
- Memo: "TIC ownership of the real estate **is** ownership of the EPC."
- Actual: not strictly true. TIC ownership is ownership of the **property**; the EPC is the entity. If the JV LLC alone is the EPC, a TIC co-owner who is not a JV LLC member is not an EPC owner — they are a co-owner of underlying real estate alongside the EPC.
- Memo elsewhere correctly says EPC = JV LLC + Janet + Ryan collectively. Need to reconcile.

---

## Overstatements / hedges needed

| # | Memo | Suggested rewording |
|---|---|---|
| 1 | "PGs mandatory for every 20%+ direct/indirect owner" | "...20%+ direct **or attributed** owner; SBA's look-through and spousal-aggregation rules can pull in <20% owners" |
| 2 | "Likely 7(a)" | "7(a) is the cleaner fit at this loan size **assuming no third-party first-lien lender**" |
| 3 | "TIC co-borrowers are operationally awkward" | Understates reality — most 7(a) lenders will not write a TIC co-borrower deal and require the TICs to roll into a single LLC pre-closing |
| 4 | "SBA prefers single note with joint-and-several" | Reword: "Practitioners typically structure as single note with J&S; SBA does not require it but lenders strongly prefer it" |
| 5 | "Sponsor 'promote' fees should be paid from equity, not from SBA proceeds" | Strengthen: "SBA proceeds **cannot** fund sponsor, acquisition, promote, or finder/broker fees regardless of program. These must be funded from equity raised outside the SBA loan." |
| 6 | "7(a)... standard 10%... 15% for special-purpose or new businesses" | 7(a) does not have a regulatory equity-injection floor for real-estate acquisition; SOP requires it for change-of-ownership and start-ups |

---

## Gaps that matter (prioritized)

### Gap 1 (HIGHEST) — The $97K acquisition fee
The memo never explicitly says: **The $575K SBA loan cannot include the $97K acquisition fee in its use-of-proceeds. The $97K must be funded entirely from the equity raise.** Sources/uses must show: SBA $575K (RE only), equity covers the $97K fee + 10% RE injection + closing costs, seller financing or other debt for the gap.

### Gap 2 (HIGHEST) — "What if no separate OC?"
If JV is itself the operator (no separate operating tenant), the EPC/OC structure does not apply at all. The borrower is simply an Operating Company that happens to own its real estate — eligible as a single-entity 7(a) borrower; §120.111 is irrelevant. The memo never diagnoses which world the deal lives in.

### Gap 3 (HIGH) — Affiliation depth
Memo flags §121.103 but doesn't run analysis. With Single Seed (Beau + Jonas), Gideon Spencer, Janet, Ryan, JV LLC, and possible OC, affiliation is a real risk. Should at minimum address §121.103(d) identity of interest, (f) common management, (h) JVs.

### Gap 4 (HIGH) — Lender willingness reality
**Most 7(a) lenders will refuse a TIC + JV co-borrower structure** and require pre-closing rollup into a single LLC. The realistic path is restructuring, not "find a lender who will do TIC."

### Gap 5 (MEDIUM) — "Credit elsewhere" test (§120.101)
Mentioned but not explained. A clean $575K against $1.9M with strong sponsors might fail this test.

### Gap 6 (MEDIUM) — Construction/improvement scope
60% (new construction) vs. 51% (existing) occupancy threshold; tenant-subleasing rules under §120.131.

### Gap 7 (LOWER) — Flood, environmental, appraisal
§120.170 flood; environmental investigation per SOP; SBA-compliant appraisal at $500K+.

### Gap 8 (LOWER) — Standby/seller-note rules
Full-standby (24-month no-payment) for full equity-injection credit; partial standby treatment otherwise.

---

## Specific edits

1. Strike "(13 CFR 120.160(c))" hazard insurance > $500K threshold
2. Re-verify $500K blanket-lien trigger; current may be $350K
3. Replace all "SOP 50 10 7.1" with "SOP 50 10 8"
4. Rewrite §120.111(a)(2) paragraph to separate reg from SOP
5. Reword "TIC ownership of the real estate is ownership of the EPC" to be precise
6. Hedge LPR claim in Citizenship paragraph
7. **Add new section** for $575K + $97K sources/uses analysis
8. **Add new "Lender-Reality" section** noting TIC + JV co-borrower structures commonly rejected
9. **Add §121.103 affiliation walk-through** with subsections (d)(f)(h)
10. **Add credit-elsewhere (§120.101) commentary**
11. Move "investments in real/personal property" citation from §120.130 to §120.110
12. Clarify 7(a) equity injection is principally a change-of-ownership / start-up rule

---

## Bottom line for synthesis (5 bullets)

1. **Architecture sound** — EPC/OC framework, blanket-lien tiering, 7(a)-vs-504 differentiation, PG matrix, TIC mortgage mechanics all substantially right.
2. **Three factual errors to correct**: §120.111(a)(2) lease-term claim conflates reg and SOP; §120.160(c) hazard threshold wrong; SOP 50 10 7.1 citations stale (should be 50 10 8).
3. **Citizenship Policy Notice paragraph is high-risk and overstated.** "5% de minimis" claim and absolute "LPRs not eligible to own any percentage" framing should not be relied on without pulling current operative notice text.
4. **Two critical user-specific questions unaddressed**: (a) $97K acquisition fee cannot come from SBA proceeds — must be sourced from equity; (b) if JV is itself the operator with no separate OC, §120.111 doesn't apply at all.
5. **The practical ceiling is lender-side.** Most 7(a) lenders refuse a TIC + JV co-borrower structure and require pre-closing rollup into a single LLC. Cleanest path: roll TIC interests into JV LLC (or sister NewCo), identify or form OC tenant, run citizenship/affiliation diligence, then approach lenders.
