# Recommended Structure & Implementation Plan

**Re:** $1.9M hospitality/STR/boutique-hotel acquisition; $575K SBA loan; $650K equity raise across seven principals (Single Seed [Beau + Jonas], Gideon Spencer, Tiffany Zhou, Janet Ng, York, Ryan); 50% / 15% / 35% (capital / capital-raise / sweat) economics
**Companion to:** Synthesis Memo A — Diagnostic & Options
**Date:** May 8, 2026

Memo A diagnoses the four-regime puzzle. This memo states the recommended structure, restates the cap table, restructures the $97K acquisition fee and 15% capital-raise allocation, provides sources & uses, and lays out the closing roadmap. Built to satisfy IRC §1031 + Rev. Proc. 2002-22, true-JV (Williamson/Howey), and SBA EPC/OC rules under 13 CFR 120.111 + SOP 50 10 8 (eff. June 1, 2025), corrected per the Wave 2 reviews.

---

## 1. Recommended Structural Decision

**Recommendation: Three-Tier Structure — TIC Pool at the Title Layer, JV LLC at the Equity Layer, Operating Company at the Operating Layer.**

The deal is structured as three discrete layers, each playing exactly one legal role:

1. **Title layer (the EPC):** A three-cotenant TIC pool holds undivided fee title. The cotenants are (a) **Beau & Jonas Single Seed JV LLC** ("JV LLC") as one cotenant, holding ~73.0%; (b) **Janet Ng** (or her single-member LLC) as a second cotenant, holding ~12.7%; (c) **Ryan** (or his single-member LLC) as a third cotenant, holding ~14.3%. Three cotenants. None is a partnership for federal tax purposes. Counts as one EPC under SBA SOP 50 10 8 (per 03_SBA_review.md, Error #7 / Bottom-line bullet 5; 05_precedents_research.md §4A; 05_precedents_review.md §74).

2. **Equity layer (the JV LLC):** The JV LLC is member-managed by the five **active** principals — Single Seed (Beau + Jonas), Gideon Spencer, Tiffany Zhou, and York — under an operating agreement that gives every member real, exercisable, documented power. Janet and Ryan are NOT members of the JV LLC. (TIC partners cannot be members of any partnership owning the same property; per 01_1031_research.md Exec Summary bullet 2 and §10; 02_TIC_research.md §6.6.)

3. **Operating layer (the OC):** A separately formed, operationally distinct **Operating Company LLC** ("HotelCo") is the master tenant under a Rev. Proc. 2002-22 §6.13-compliant master lease from the TIC pool. HotelCo runs the hospitality business (front desk, housekeeping, F&B, OTA listings, concierge, daily turnover). HotelCo is owned by the same five active principals in the same percentages as the JV LLC, but it is a distinct entity for SBA §120.111(a)(5) co-borrower purposes and a distinct lessee for Rev. Proc. 2002-22 §6.12/§6.13 purposes (the JV LLC cannot be both a cotenant *and* the lessee/manager — per 02_TIC_review.md §B and 04_JV_security_review.md gap-analysis; Rev. Proc. 2002-22 §6.12 expressly bars the manager from also being the lessee).

The single most important structural decision in this memo is **separating the JV LLC (which is a *cotenant*) from HotelCo (which is the *lessee/operator*)**. That separation cures the §6.12 manager-as-lessee problem identified in 01_1031_research.md §7 and 02_TIC_review.md "B. Master-lease cure has real complications," lets HotelCo absorb all hospitality services (the *Hocking v. Dubois*, 885 F.2d 1449 (9th Cir. 1989) (en banc) risk that 04_JV_security_review.md flagged for STR/boutique-hotel deals), and gives the SBA lender a textbook EPC/OC fact pattern for §120.111.

### Entity Diagram

```
                     +------------------------------------------------+
                     |             SBA 7(a) PREFERRED LENDER          |
                     |   (unrelated to any cotenant, sponsor, mgr,    |
                     |    or lessee — Rev. Proc. 2002-22 §6.14)       |
                     +------------------------------------------------+
                                          |
                                $575,000 — single 7(a) note
                                joint & several across EPC
                                          |
        +---------------------------------+----------------------------------+
        | First mortgage on entire fee    | Co-borrower / blanket UCC-1     |
        | (signed by all 3 cotenants)     | on operating assets              |
        | Assignment of all rents         | (13 CFR §120.111(a)(5))          |
        v                                 v
  ============== EPC = TIC POOL ===============         ====== OC =======
  (3 undivided cotenants — Rev. Proc. 2002-22)          HOTELCO LLC
                                                        (5 active members)
  +-------------------------+   +---------+   +--------+
  |   JV LLC (cotenant 1)   |   | Janet   |   | Ryan   |       Members:
  |   ~73.04% undivided     |   | (or SM- |   | (or    |       Single Seed  39.51%
  |                         |   | LLC)    |   | SMLLC) |       Gideon       18.54%
  | Member-managed; only    |   |         |   |        |       Tiffany      11.58%
  | the FIVE active members |   | ~12.69% |   |~14.27% |       York          9.04%
  | (no Janet, no Ryan)     |   | undiv.  |   | undiv. |       Unallocated    5.88%
  |                         |   |         |   |        |        (sweat slot)
  | Members & internal %:   |   | 100%    |   | 100%   |       Manager:     Beau (MM)
  |   Single Seed   54.10%  |   | active  |   | active |
  |   Gideon        25.39%  |   | role:   |   | role:  |       PG: every 20%+
  |   Tiffany       15.86%  |   | Guest   |   | PR     |       owner of OC
  |   York          12.38%  |   | Exper.  |   |        |
  |   Unallocated    8.05%  |   | + PG    |   | + PG   |
  |   (rounds to 100%)      |   +----+----+   +---+----+
  +-------------+-----------+        |            |
                |                    |            |
                +-----+--------------+------+-----+
                      |                     |
                      |  Single deed,       |
                      |  3 cotenants,       |
                      |  X+Y+Z = 100%       |
                      |  TIC AGREEMENT      |
                      |  (recorded against  |
                      |   title; §6.04-6.15)|
                      v                     v
                  +-----------------------------+
                  |    THE REAL PROPERTY        |
                  |    (boutique hotel / STR)   |
                  +-----------------------------+
                              ^
                              | Master lease
                              | FMV rent + fixed % gross receipts
                              | Term ≥ SBA loan term
                              | Subordinated to SBA mortgage
                              | (Rev. Proc. 2002-22 §6.13;
                              |  13 CFR §120.111(a)(2)/(a)(3))
                              |
                              +---- HOTELCO LLC pays rent ----
                                    HOTELCO LLC operates the hotel
                                    HOTELCO LLC employs/contracts staff
                                    HOTELCO LLC takes all hospitality risk

  Management: each cotenant separately reports rent income on Schedule E
  (no Form 1065; no common EIN; no common bank account beyond §6.12
  3-month sweep). Manager (if any, separate from HotelCo) is annually
  renewable, FMV fee not contingent on profits — Rev. Proc. 2002-22 §6.12.
```

**Flows summarized:**
- **Debt:** SBA → TIC pool (joint & several) and HotelCo (co-borrower); first mortgage on entire fee; UCC-1 on HotelCo assets; assignment of HotelCo rents to lender.
- **Rent:** HotelCo → TIC cotenants pro-rata under master lease; cotenants distribute the rent to their own owners on Schedule E.
- **Hospitality revenue:** Guests → HotelCo → operating expenses → master lease rent → cotenants. The JV LLC's members capture the bulk of "deal upside" via HotelCo profits, not via the TIC cotenancy.
- **Fees:** No syndication-style acquisition fee paid in cash. The legacy $97K is converted to JV-LLC capital-account credit (Section 3 below). Any management fee paid by the TIC pool to a manager must satisfy §6.12 (annual, FMV, not contingent).

---

## 2. Restated Cap Table — How the Math Works

### 2.1 The structural conflict to resolve first

The user's target table allocates Janet 1.15% of the deal as "capital-raise" (and zero raise to Ryan). But under Rev. Proc. 2002-22 §6.08 every cotenant must "share in all revenues … in proportion to the co-owner's undivided interest." A TIC cotenant cannot get a special-purpose 1.15% bump for raising capital while still being a TIC. (See 02_TIC_review.md "C. Same economic outcome — no more, no less is structurally unachievable" and 02_TIC_research.md §6.3.)

There are three legitimate ways to handle this:

| Option | What it does | Net result for Janet | Verdict |
|---|---|---|---|
| (a) Reallocate Janet's 1.15% raise to her undivided fee % | Increase Janet's TIC % from 12.69% → 12.69% (already factored into UI %) | Achieves target by raising her undivided fee interest | **RECOMMENDED** |
| (b) Accept that Janet's economic outcome is slightly below 12.69% | Drop the raise allocation entirely | Janet ends at ~11.54% — below target | Disfavored; user said "no more, no less" but allowed slight deviation |
| (c) Pay Janet a separate one-time consulting fee at FMV before closing | Treat 1.15% × $1.9M ≈ $21,850 as a pre-closing services fee | Outside the TIC entirely; avoids §6.08 problem | Workable but introduces sponsor-fee disclosure risk under §6.15 |

**We recommend Option (a):** roll Janet's 1.15% capital-raise allocation into a higher undivided fee percentage so that her *total* economic share through the TIC equals her 12.69% target. Ryan is unaffected because his target carried no raise allocation. The math is shown below.

### 2.2 Recomputing Janet's and Ryan's undivided percentages

The user's target: Janet 12.69% of the deal; Ryan 15.38% of the deal.

But these percentages are stated as a percentage of *equity contribution-equivalent value*, not of *fee title*. The deal is funded $575K (debt) + $650K (equity) = $1,225K of the $1.9M. To translate user-stated equity-percentage targets into undivided fee percentages of the property as a whole, a TIC cotenant's % of fee should equal that cotenant's % of the *total project capital* (debt + equity), because under §6.09 each cotenant carries pro-rata SBA debt service.

Janet's project-cost contribution = $150K equity contribution. Ryan's = $200K. If we hold the JV LLC's contribution at $300K equity and assume the TIC pool collectively bears the $575K SBA debt pro-rata to the equity split (debt allocated by undivided %), then to hit the user-stated *equity* outcome targets we set undivided % of fee equal to (member's share of $1.9M total project cost):

| Cotenant | Equity in | Pro-rata share of $575K debt | Total project cost burden | Undivided fee % |
|---|---|---|---|---|
| JV LLC | $300,000 | $441,346 | $741,346 | **39.02%** |
| Janet Ng | $150,000 | $220,673 | $370,673 | **19.51%** |
| Ryan | $200,000 | $294,231 | $494,231 | **26.01%** |
| Acquisition costs covered from JV LLC sweat (Section 3) | — | — | $293,750 | **15.46%** within JV LLC |
| **Total** | $650,000 | $956,250 (excl. SBA) | $1,900,000 | 100% |

This produces a clean cap table where each cotenant's pro-rata cash flow approximates the user's targets without a special allocation. **However**, the user's table actually states the targets as a % of total deal economics (not as % of equity), so the simpler implementation is:

| Cotenant | User target % | Implementation: undivided fee % | Comment |
|---|---|---|---|
| JV LLC (5 members + sweat) | 71.93% (50% + 35% sweat − 15% raise + Janet's 1.15% reallocated to her) − the cotenant slices Janet/Ryan = (100% − 12.69% − 15.38%) | **71.93%** | Includes all sweat + Single Seed's 6.92% raise + Gideon's 6.92% raise (recharacterized — see Section 4) |
| Janet Ng | 12.69% | **12.69%** | 1.15% raise rolled into her undivided fee % |
| Ryan | 15.38% | **15.38%** | Identical to user target |
| **Total** | **100.00%** | **100.00%** | |

We use these latter percentages throughout this memo.

### 2.3 Two cap tables, side by side

#### TABLE A — TIC TABLE (fee title — what is on the deed)

| Cotenant | Undivided fee % | Capital "in" | Pro-rata share of $575K SBA | Notes |
|---|---|---|---|---|
| **JV LLC** (Beau & Jonas Single Seed JV LLC) | **71.93%** | $300,000 equity + $97,000 deemed sweat for acquisition (see Section 3) | $413,599 | Five active members behind it |
| **Janet Ng** (or SMLLC for asset protection) | **12.69%** | $150,000 (1031 proceeds) | $72,968 | TIC partner; PG required (Janet's look-through into EPC ≥ 20%? No — 12.69% < 20%. PG voluntary unless lender demands.) |
| **Ryan** (or SMLLC) | **15.38%** | $200,000 (1031 proceeds) | $88,433 | TIC partner; **Ryan's 15.38% triggers mandatory 20% rule? Just below. Verify look-through. PG voluntary unless lender demands. But user table flags Ryan as PG, so include him on Form 148.** |
| **Total** | **100.00%** | $747,000 | $575,000 | |

#### TABLE B — JV LLC INTERNAL TABLE (members of JV LLC)

The JV LLC's 71.93% slice of fee title is then allocated among its five members. We translate the user's table targets into JV-LLC-internal percentages by dividing each member's "deal %" by the JV LLC's 71.93%:

| Member | User table "total %" of deal | JV-LLC-internal % (= deal % ÷ 71.93%) | Role | PG? |
|---|---|---|---|---|
| Single Seed (Beau + Jonas) | 33.62% | **46.74%** | Operator / managing member / PG | YES — Form 148 |
| Gideon Spencer | 15.77% | **21.93%** | Asset management / PG | YES — Form 148 |
| Tiffany Zhou | 9.85% | **13.69%** | Design + GC | At lender option |
| York | 7.69% | **10.69%** | Controller | At lender option |
| Unallocated sweat | 5.00% | **6.95%** | Reserve for future operator hire / extra contributions | n/a |
| **Total** | **71.93%** | **100.00%** | | |

**Reconciliation:** Janet's 12.69% + Ryan's 15.38% + JV LLC's 71.93% = 100.00%. Within the JV LLC, the five members + sweat reserve sum to 100.00%. The user's stated 50/15/35 capital/raise/sweat split is preserved in *aggregate* across the deal, but it lives inside the JV LLC's 71.93%; the TIC partners' shares are pure capital + pure pro-rata, no special allocation, fully Rev. Proc. 2002-22 §6.08 compliant.

### 2.4 What Janet and Ryan actually get vs. the JV LLC

This is the irreducible tradeoff that 02_TIC_review.md "C. Same-economic-outcome unachievable" identifies and that the user has agreed to accept:

- **Janet and Ryan's 12.69% and 15.38%** translate to pro-rata cash distributions from the master-lease rent paid by HotelCo, net of pro-rata SBA debt service, pro-rata real-estate taxes, pro-rata insurance, and pro-rata structural maintenance. They receive sale proceeds at exit pro-rata to undivided %.
- **The JV LLC's 71.93%** of the cotenant rent is captured by the five active members, AND those same five members capture 100% of HotelCo's profits. The "deal upside" — the difference between what HotelCo earns from operations and what HotelCo pays in master-lease rent — is wholly inside the JV/HotelCo layer. Janet and Ryan see none of it.
- This is the price of §1031 deferral. Per 02_TIC_review.md, a static-percentage TIC cannot replicate a curved JV waterfall across return scenarios. The user has explicitly accepted this tradeoff.

---

## 3. Restructure the $97K Acquisition Fee

### 3.1 Why the fee as stated cannot stand

Per 03_SBA_review.md (Gap 1, HIGHEST) and 04_JV_security_review.md §9, the proposed $97K acquisition fee fails on three independent grounds:

1. **SBA — cannot be funded from loan proceeds.** SBA SOP 50 10 8 prohibits using 7(a) proceeds for sponsor, acquisition, broker, finder, or promote fees. (See 03_SBA_research.md "Sponsor / acquisition fees" and 03_SBA_review.md Gap 1.) The $97K must be sourced entirely from equity.
2. **Williamson — sponsor-fee evidence of security.** Per 04_JV_security_research.md §9 and §8 red-flag #4, $97K = 5.10% of purchase price and 14.92% of equity raised. Typical syndication norm is 1–3% (per 04_JV_security_review.md §5 market-color correction). At 5.10% paid as cash to organizers, the fee is a Williamson Factor 3 / Long v. Shultz Cattle indicator that flips the JV into a security.
3. **Rev. Proc. 2002-22 §6.15 — sponsor fee must be FMV.** The fee paid for arranging cotenant interests must be defensibly FMV and not contingent on income or profits. A $97K fee on a $1.9M deal exceeds typical FMV norms for the underlying acquisition work.

### 3.2 Recommended treatment — convert to JV-LLC capital-account credit

The $97K is converted from a cash fee at closing into a **capital-account credit** allocated within the JV LLC, recognizing the pre-closing acquisition and underwriting work performed by Single Seed (and to a lesser extent Gideon). No cash leaves the closing table for "acquisition fee." The JV LLC's $300,000 of equity contribution is funded by the JV members (cash or sweat), and Single Seed's capital account is credited with an additional $97,000 of sweat-equity for the documented acquisition work. (See 04_JV_security_research.md §9 "defensible alternative.")

### 3.3 Math impact on cap table

The recharacterization actually *strengthens* the cap-table targets:

- Single Seed's 19% sweat allocation in the user table is partly funded by this $97K credit. The total economic share remains 33.62%.
- The $97K is documented as Single Seed's "acquisition and structuring sweat work" with time-stamps, deliverables (financial model, market study, term-sheet negotiation), and a fairness memo. (See 04_JV_security_research.md §10 "How to document active participation.")
- No 1099 or W-2 issued for the $97K (which would be an active-services payment subject to FICA/SE tax). It flows to capital-account through a written sweat-equity contribution agreement.
- A recital in the JV LLC operating agreement discloses the $97K crediting and obtains member consent — required by 04_JV_security_research.md §7 "Acquisition fee disclosed in OA."
- A separate fairness memo from a third-party valuation firm ("the work performed had FMV of $X, of which $97,000 is recognized as Single Seed's contribution") backstops Rev. Proc. 2002-22 §6.15 for the cotenant TIC partners.

### 3.4 Where $97K appears in the cash sources & uses

It does not. The $97K is sweat. Sources & uses (Section 5) shows only cash flows. The capital-account credit appears only in the JV LLC's books and the OA's recital.

---

## 4. Restructure the 15% Capital-Raise Bucket

### 4.1 Why the 15% bucket as described carries security risk

Per 04_JV_security_review.md (corrected from the research memo's overbroad §15(a) framing) and 04_JV_security_research.md §8 red flag #6 and §11:

- A member who receives equity *for raising capital from third parties* looks exactly like an unregistered broker-dealer's commission. If the JV interest is a security (or becomes one because of these facts), §15(a) applies.
- Even if not a security under §15(a), transaction-based capital-raise compensation is the strongest single Williamson Factor 1 / Howey prong-4 red flag.
- Two of the three "raise" recipients in the user's table are Single Seed (6.92%) and Gideon (6.92%). Janet's 1.15% has already been reallocated to her undivided fee % under Section 2.

### 4.2 Recommended treatment — reframe and limit

We restructure the 13.85% capital-raise allocation (after Janet's 1.15% has been moved out) along three principles, all per 04_JV_security_review.md Gap #3:

1. **Reframe as pre-closing acquisition-and-due-diligence sweat equity.** Single Seed and Gideon are awarded equity not "for raising capital" but for their *operational pre-closing work*: market study, financial modeling, term sheet, lender introductions, environmental and appraisal management, TIC and master-lease drafting oversight, citizenship and affiliation diligence on every owner. The 6.92% to each is documented as a fixed dollar value of pre-closing labor, not a commission on capital raised.

2. **Limit recipients to active operational members.** The cap-table targets confirm this is already true — Single Seed and Gideon are both active operational principals (per the user's table, they hold "Operator/MM/PG" and "Asset Mgmt/PG" roles). No allocation of the 15% bucket goes to a passive "capital-raiser."

3. **Recharacterize in OA recitals.** The JV LLC OA includes a recital that "Single Seed and Gideon performed material pre-closing acquisition, underwriting, structuring, and lender-introduction work, the FMV of which is $X, recognized as additional capital contribution credit." This is the mirror image of Section 3's $97K recharacterization.

### 4.3 Single Seed's 6.92% and Gideon's 6.92% — old framing vs. new framing

| Old framing (user's intuition) | New framing (this memo) |
|---|---|
| "Raised capital from their personal networks" | "Performed pre-closing structuring, underwriting, financial modeling, lender introductions, and term-sheet negotiation; their personal networks were the *channel* through which capital was found, but the *work* compensated is structuring work, not commission" |
| Looks like a syndication commission | Looks like an arm's-length consulting / structuring fee credited to capital account |
| Williamson red flag | Williamson green flag — they are active members performing essential managerial efforts |

### 4.4 Math impact

The 15% bucket within the JV LLC stays in place as documented work credit. The cap table is not recomputed. The effect is purely documentary — but documentary in a way that builds the contemporaneous record needed to defeat a Williamson/Howey challenge later. (Per 04_JV_security_research.md §10, "Pre-closing — engagement letters, resumes/bios, underwriting model with each member's input.")

---

## 5. Sources & Uses Table

The deal as described does not balance. We must surface the gap and lay out the user's options to fill it.

### 5.1 Stated sources & uses

| SOURCES | AMOUNT | NOTES |
|---|---|---|
| SBA 7(a) loan | $575,000 | Cannot fund acquisition fee, sponsor fees, or working capital deemed sponsor compensation |
| Janet's 1031 equity | $150,000 | Direct to TIC interest |
| Ryan's 1031 equity | $200,000 | Direct to TIC interest |
| JV LLC member equity (5 active) | $300,000 | Includes the slice formerly called "raised capital" — now recharacterized |
| **TOTAL CASH SOURCES** | **$1,225,000** | |
| Sweat-equity credit (Single Seed / Gideon, non-cash) | $97,000 deemed | Capital-account only; not cash to closing |

| USES | AMOUNT | NOTES |
|---|---|---|
| Property purchase | $1,803,000 | $1,900,000 stated price minus $97,000 acquisition fee that is no longer paid in cash; if the seller's price is firm at $1,900,000, this line is $1,900,000 and we must find the gap |
| Acquisition fee (sweat) | $0 cash; $97,000 capital credit | Per Section 3 — non-cash |
| SBA-loan closing costs (1.5–3.5% of loan) | ~$15,000 | SBA guaranty fee + lender fees |
| Title, recording, legal, appraisal, environmental | $35,000–55,000 | Real-estate closing costs |
| Working capital reserves / OS&E (boutique-hotel furniture, fixtures) | $50,000–100,000 | Cannot use 504 proceeds; can use 7(a) working capital, but must come out of $575K |
| **TOTAL USES** | **~$1,900,000–$2,055,000** | |

### 5.2 The funding gap

If the seller's price is firm at $1,900,000 (and not negotiable down by $97K), the deal funds:
- **Sources:** $575K SBA + $650K equity = **$1,225,000** of cash
- **Uses:** $1,900,000 (purchase) + ~$50,000 (closing costs) + ~$75,000 (FF&E) = **$2,025,000**
- **Gap:** **~$800,000** of cash needed beyond what is in the stack today

This gap is not a small issue. The user's options to fill it:

| Option | Mechanism | Comment |
|---|---|---|
| (a) Increase total equity raise to ~$1.45M | More equity from Single Seed / Gideon / Tiffany / York | Cleanest. Restores cash sources to ~$2.025M. Requires renegotiating user's percentages because the same fixed $-amounts now buy smaller % of fee. |
| (b) Seller financing on full standby (24 months no payment) | Per SBA SOP 50 10 8, full-standby seller note can count toward equity injection; a 5% second-position seller note ~$95K is common | SBA may permit the seller note to count toward the 10% injection requirement only with full standby; if partial standby, treats as outside debt and may stress lender's debt-service-coverage calculation |
| (c) Larger SBA loan | Re-underwrite at higher LTV — the SBA can lend up to $5M; $575K is well below limit | Requires lender's appraisal to support; user must absorb additional debt service |
| (d) Negotiate purchase price to $1.5–1.6M | Requires market support | Outside this memo's scope |
| (e) Mezzanine / preferred equity from a specialty hospitality fund | Re-introduces securities risk and adds a new partner | Disfavored — defeats true-JV posture |

**Our recommendation:** combination of (a) and (b) — increase equity to fill ~$650K of the gap and add a $150K seller note on full standby for the rest. Maintain the user's % targets within the larger equity number by scaling each member's $-contribution proportionally.

### 5.3 SBA equity injection

SBA SOP 50 10 8 typically requires 10% borrower equity injection on real-estate acquisitions (15% on special-purpose properties — boutique hotels often qualify as "special purpose"). At $1,900,000, 10% = $190,000; 15% = $285,000. Either threshold is comfortably met by the cash equity in this stack ($650K, increasing to ~$1.3M under recommendation (a)).

---

## 6. Operating Agreement & TIC Agreement Provisions Checklist

### 6.1 JV LLC Operating Agreement — must include

Drawn from 04_JV_security_research.md §7 "Operating Agreement Provisions That Anchor JV Status" and 02_TIC_research.md §6.2:

- **Member-managed structure** OR manager-managed with Beau as managing member subject to extensive reserved-matters list
- **Reserved matters requiring unanimous member consent:** any sale or refinance of the property; admission of new members; any debt > $50K outside SBA loan; capital calls; budget approval; change in business strategy; hiring or firing of HotelCo's GM; change in master-lease terms; entry into any contract with a related party
- **Reserved matters requiring supermajority (75%):** annual budget; capital expenditure > $25K; entry into any new master lease; selection or replacement of accountant, attorney, insurance broker
- **Defined operational duties for each member, with quarterly deliverables:**
  - Single Seed (Beau): Managing member of JV LLC, Manager of HotelCo, day-to-day operations, weekly P&L review, lender liaison
  - Single Seed (Jonas): Co-operator, marketing/STR listings, OTA management, guest experience oversight
  - Gideon Spencer: Quarterly asset-management reports, capital-budget oversight, exit-strategy planning
  - Tiffany Zhou: Design oversight, GC contractor relationships, FF&E procurement
  - York: Quarterly financial reports, monthly cash management, tax filings, SBA compliance reporting
- **Information rights:** real-time access to JV LLC and HotelCo bank accounts, books, contracts; quarterly written financials; annual K-1s
- **Member meeting schedule:** monthly during first 12 months, quarterly thereafter; documented minutes and votes
- **Removal rights:** majority of non-affected members can remove the managing member for cause; supermajority without cause
- **Acquisition-fee disclosure:** explicit recital that the $97,000 has been recharacterized as Single Seed sweat-equity capital-account credit and that all members consent (per 04_JV_security_research.md §9)
- **15% bucket disclosure:** explicit recital that Single Seed's and Gideon's allocations recognize their pre-closing structuring and underwriting work, not capital-raising commissions
- **Capital-call mechanics:** unanimous member approval for any call; pro-rata to existing membership %; 30-day funding window; dilution mechanics for non-funders
- **Transfer restrictions / ROFR:** members cannot transfer without offering to other members at FMV first
- **Buy-sell mechanics:** fair-market-value buyout on death, disability, or material breach
- **Right to dissolve** under state LLC act
- **Member representations:** each member represents (i) they have reviewed the OA, (ii) they have business experience appropriate to their role, (iii) they intend to actively participate, (iv) the interest is not intended to be a security, (v) they are accredited or sophisticated (belt-and-suspenders for Reg D fall-back per 04_JV_security_research.md "Closing Recommendation" #3)
- **PG acknowledgment:** each member acknowledges PG status and personal exposure
- **Citizenship reps:** each member represents U.S. citizenship/national status (per 03_SBA_research.md citizenship caveat — but soften per 03_SBA_review.md Error #4: "consistent with the latest operative SBA Policy Notice")
- **No general solicitation:** representation that no member was solicited via general advertising
- **Indemnification of members for actions in good faith**
- **Tax allocations:** §704(b)-compliant; targeted allocations to capital accounts

### 6.2 TIC Agreement — must include (between JV LLC, Janet, Ryan)

Drawn from 01_1031_research.md §1 (Rev. Proc. 2002-22 §§6.04–6.15 line-by-line) and 02_TIC_research.md §5:

- **Recital of each cotenant's exact undivided %:** JV LLC 71.93%; Janet 12.69%; Ryan 15.38%; total 100.00% (§6.01)
- **Cap on number of cotenants ≤ 3** (well within §6.02's 35-cap)
- **No partnership treatment:** explicit recital that the cotenants will not file a partnership return, conduct business under a common name, or hold themselves out as partners (§6.03)
- **Five Big Things requiring unanimous consent:** sale or other disposition of the property; any lease or re-lease; any negotiation or renegotiation of indebtedness secured by a blanket lien (i.e., any SBA refi); hiring of any manager; negotiation, extension, or renewal of any management contract (§6.05)
- **All other actions:** ≥50% vote (§6.05)
- **Pro-rata sharing of revenue and cost:** every dollar in and every dollar out shared strictly in proportion to undivided % (§6.08)
- **Pro-rata sharing of debt:** §575K SBA debt service allocated 71.93% / 12.69% / 15.38% (§6.09)
- **Right of first offer at FMV before partition:** any cotenant intending to sell first offers to the others at FMV (§6.06; corrected from 01_1031_review.md Error #6 — this provision lives in §6.06, not §6.04)
- **Right to transfer / partition / encumber preserved:** each cotenant may sell or partition without consent, subject only to lender restrictions consistent with customary commercial lending (§6.06)
- **Sale proceeds:** at sale, SBA loan paid off; remaining proceeds distributed pro-rata (§6.07)
- **No put options to sponsor / lessee / other cotenant / lender** (§6.10)
- **Customary services only** at the cotenant level (§6.11) — all hospitality services are HotelCo's, not the TIC pool's
- **Management agreement (if any) terms:** annually renewable; FMV fee; not contingent on income or profits; manager not also a lessee (§6.12)
- **Master-lease recital cross-reference:** the TIC pool leases 100% of the property to HotelCo at FMV rent + fixed % of gross receipts (per §6.13)
- **Lender independence:** representation that the SBA-approved lender is not a related person to any cotenant, sponsor, manager, or lessee (§6.14; §267(b)/§707(b))
- **Sponsor-fee FMV recital:** any payment to a sponsor is at FMV and not contingent (§6.15)
- **No drag-along, no tag-along, no waterfall**
- **No common bank account** beyond the §6.12 manager's collection account swept within 3 months
- **State-law overlay:** confirm compliance with the property's state's TIC, partition, recording, homestead, community-property, and UPHPA rules (per 02_TIC_research.md §9; updated per 02_TIC_review.md Error #2 to "24 states + D.C. + U.S. Virgin Islands have adopted UPHPA")
- **Recordation:** TIC Agreement recorded against title (§6.04 "may run with the land")
- **Tax reporting:** each cotenant reports on Schedule E; no Form 1065; no common EIN

### 6.3 Master Lease (TIC Pool ↔ HotelCo) — must include

Drawn from 01_1031_research.md §7A and 02_TIC_research.md §6.3:

- **Lessor:** the TIC pool (JV LLC, Janet, Ryan as tenants in common)
- **Lessee:** HotelCo LLC (separate from JV LLC — this is the structural fix)
- **Term:** ≥ SBA loan term (per SBA SOP 50 10 8, even though 03_SBA_review.md Error #1 corrected the citation away from §120.111(a)(2))
- **Rent:** **FMV base rent plus a fixed percentage of gross receipts** (NOT net income / NOT cash flow / NOT contingent on profits). Per §6.13, percentage of gross receipts is permitted; net is not.
- **Subordination:** lease is subordinate to SBA mortgage (per 13 CFR §120.111 framework; consult lender's specific requirements)
- **Rent cap:** rent cannot exceed loan payment + EPC's direct holding costs (per SBA SOP 50 10 8)
- **Assignment of rents:** lessor (TIC pool) assigns all rents to SBA lender as collateral (13 CFR §120.111(a)(3))
- **Use:** hospitality / boutique hotel / STR consistent with zoning
- **Operations:** HotelCo provides all hospitality services (front desk, housekeeping, concierge, F&B, OTA listings, etc.) — these services live in HotelCo, NOT in the TIC pool, to avoid the Rev. Rul. 75-374 / *Hocking* services line (per 05_precedents_research.md §1D and §5A)
- **Termination:** mirror SBA loan term; renewable at FMV
- **Default:** standard commercial-lease defaults; cure periods; SBA-mandated lender step-in rights
- **No put / no buyout from lessor by lessee** (cotenant-level §6.10 protection)
- **FMV documentation:** third-party rent comparables / appraisal at signing

---

## 7. SBA Underwriting Package Outline

Per 03_SBA_research.md and 03_SBA_review.md, the SBA-preferred lender will need:

| Item | Source | Notes |
|---|---|---|
| EPC/OC structure documentation | 13 CFR §120.111 | Show TIC pool = single EPC; HotelCo = OC; written master lease |
| 20%+ owner identification, both EPC and OC | §120.160(a), §120.111(a)(4) | Look-through into JV LLC: Single Seed = Beau & Jonas; if Beau and Jonas each hold ≥ 50% of Single Seed, look further. Single Seed's 46.74% of JV LLC × 71.93% of EPC = 33.62% of EPC — well over 20%. Gideon: 21.93% × 71.93% = 15.78% — below 20% for EPC, but PG required separately if ≥ 20% of OC. |
| Personal guarantees | Form 148 (full) for ≥ 20% owners; Form 148L for limited or spousal pledge | See Section 8 PG matrix |
| Citizenship verification on every direct and indirect owner | SBA Policy Notice consistent with EO 14159 (March 2025) | **Must verify current operative version per 03_SBA_review.md Error #4 — the LPR exclusion and 5% de minimis claims should be confirmed against the most recent SBA policy notice and SOP 50 10 8 language at the time of underwriting** |
| Affiliation analysis under 13 CFR §121.103 | §121.103(d), (f), (h) | All JV LLC members + JV LLC + HotelCo + any other entities they own. Special focus on (h) JVs and (f) common management. (Per 03_SBA_review.md Gap 3.) |
| "Credit elsewhere" justification under §120.101 | SOP 50 10 8 | Why borrower cannot get this loan on similar terms in the conventional market. (Per 03_SBA_review.md Gap 5.) |
| Sources & uses showing $97K from equity, NOT loan proceeds | SOP 50 10 8 | The acquisition-fee recharacterization (Section 3) makes this trivial — there is no $97K cash item. |
| Hazard insurance on all collateral | 13 CFR §120.160(c) (the "> $500K" threshold mentioned in the research memo is wrong — see 03_SBA_review.md Error #2) | Required regardless of amount |
| Environmental investigation | SOP 50 10 8 | Phase I ESA standard; Phase II if Phase I flags |
| SBA-compliant appraisal | SOP 50 10 8 | Real-estate appraisal at $500K+ |
| Standby agreement for any seller financing | SOP 50 10 8 | Full standby (24 months, no payments) for full equity-injection credit |
| Subordination of lease to mortgage | §120.111 framework | Per Section 6.3 |
| Assignment of rents to lender | §120.111(a)(3) | Per Section 6.3 |
| Form 1919 from each owner; Form 1920 from lender | SOP 50 10 8 | Standard package |
| OC operating cash-flow projections | Lender underwriting | DSCR ≥ 1.25x typically |
| Lender independence representation | Rev. Proc. 2002-22 §6.14 | Lender unrelated to any cotenant, sponsor, manager, or lessee under §267(b)/§707(b) — this is a TIC requirement, not an SBA requirement, but document it |
| Form 148 / 148L PGs | SOP 50 10 8; §120.160(a) | See Section 8 |

---

## 8. Personal Guarantee Matrix (Final)

Per 03_SBA_research.md "Personal Guarantee Matrix" and 13 CFR §120.111(a)(4) "20% rule applied to BOTH entities":

| Person / entity | Direct % of JV LLC | Effective % of EPC (= JV LLC's 71.93% × member %) | Direct % of OC (HotelCo) | PG? | Form |
|---|---|---|---|---|---|
| Single Seed JV LLC (Beau + Jonas, jointly) | 46.74% | 33.62% of EPC | 39.51% of OC | **Yes — full unconditional PG** | **Form 148** |
| – Beau (if 50% of Single Seed) | 23.37% of JV LLC | 16.81% of EPC | 19.76% of OC | **Look-through ≥ 20% of OC? Borderline. Lender will require.** | Form 148 |
| – Jonas (if 50% of Single Seed) | 23.37% of JV LLC | 16.81% of EPC | 19.76% of OC | **Same — borderline; lender will require.** | Form 148 |
| Gideon Spencer | 21.93% | 15.78% of EPC | 18.54% of OC | **Below 20% in both; lender's option. User table flags him for PG.** | Form 148 (voluntary at lender's request) |
| Tiffany Zhou | 13.69% | 9.85% of EPC | 11.58% of OC | Below 20% in all; user table does not flag | Form 148L (limited) at lender option |
| York | 10.69% | 7.69% of EPC | 9.04% of OC | Below 20% in all; user table does not flag | Form 148L (limited) at lender option |
| Janet Ng (cotenant — direct EPC owner) | 0% (not in JV LLC) | 12.69% of EPC | 0% of OC | **Below 20% of EPC; lender's option. User table flags her for PG.** | Form 148 (voluntary; but user wants her on it) |
| Ryan (cotenant — direct EPC owner) | 0% (not in JV LLC) | 15.38% of EPC | 0% of OC | **Below 20% of EPC; lender's option. User table flags him for PG.** | Form 148 (voluntary; but user wants him on it) |
| HotelCo (OC) | n/a | n/a | the entity itself | **Yes — co-borrower under §120.111(a)(5)** | Co-borrower in note |
| Spouses of Beau, Jonas, Gideon | n/a | n/a | n/a | If joint personal RE pledged or household ownership ≥ 20%, **yes, full PG**; otherwise spousal-collateral consent only | 148 or 148L per ECOA Reg B (12 CFR §1002.7) |

**Critical points:**

1. **Beau and Jonas's individual percentages depend on how Single Seed is owned internally.** Their look-through into the EPC is ~16.8% each at 50/50. SBA will likely require both to PG anyway because (a) Single Seed itself must PG as a 20%+ owner, and SBA looks through to the Single Seed members per SOP 50 10 8, and (b) lender practice is to require PG from anyone whose look-through approaches the threshold.
2. **Janet's and Ryan's direct EPC ownership is 12.69% and 15.38%, respectively.** Both are below 20%. SBA does NOT mandatorily require their PG. However, the user has flagged both as PG signers, so they will sign Form 148 voluntarily.
3. **Gideon at 15.78% of EPC** is below the 20% mandatory PG threshold in the EPC. He IS at 18.54% of OC, also below threshold. Lender will likely require PG anyway because of his cap-table prominence and operating role.
4. **Spousal aggregation:** SOP 50 10 8 aggregates spouse + minor children. If Beau's spouse owns any % of Single Seed (or any related entity), they may be aggregated with Beau, pushing him over the 20% threshold mandatorily.
5. **Citizenship:** every PG signer must be U.S. citizen/national per the operative SBA Policy Notice — verify each person's current status before signing.

---

## 9. Closing Roadmap (Gantt-Style Timeline)

**Assumptions:** Today = May 8, 2026. Target close = roughly 90–120 days, depending on lender pace and Janet's/Ryan's 1031 timing windows. Items in **bold** are sequential gates; non-bold items run in parallel.

| # | Task | Lead | Earliest start | Earliest end | Sequential? |
|---|---|---|---|---|---|
| 1 | **Engage tax counsel for TIC opinion letter** | Sponsor | Day 1 (May 8) | Day 21 | YES — opinion gates closing |
| 2 | **Engage securities counsel for JV-vs-security analysis** | Sponsor | Day 1 | Day 21 | YES — opinion gates closing |
| 3 | Engage SBA-preferred lender; preliminary term sheet | Sponsor + Beau | Day 1 | Day 21 | Parallel to 1 and 2 |
| 4 | Identify QI for Janet and Ryan | Janet/Ryan | Day 1 (must be in place BEFORE Janet/Ryan close their relinquished sales) | Day 14 | YES for each of Janet/Ryan independently |
| 5 | Citizenship & affiliation verification on all members | Counsel | Day 7 | Day 28 | Parallel |
| 6 | Property appraisal + Phase I environmental | Lender / sponsor | Day 14 | Day 60 | Parallel |
| 7 | Form HotelCo LLC (the OC) | Sponsor + counsel | Day 14 | Day 21 | Sequential before lender's commitment |
| 8 | Draft TIC Agreement | TIC counsel | Day 21 | Day 60 | Parallel — but must be in final form before closing |
| 9 | Draft JV LLC Operating Agreement | Securities counsel | Day 21 | Day 60 | Parallel |
| 10 | Draft master lease (TIC pool ↔ HotelCo) | Real estate counsel | Day 28 | Day 60 | Parallel |
| 11 | Draft management agreement (if separate from master lease) | Real estate counsel | Day 28 | Day 60 | Parallel |
| 12 | Member meetings to ratify structure, OA, PG, contributions | All members | Day 60 | Day 75 | Sequential — must precede final docs |
| 13 | Lender final underwriting + commitment letter | Lender | Day 60 | Day 90 | Sequential |
| 14 | SBA Forms 148 / 148L / 1919 / 1920 signing | Members + lender | Day 75 | Day 90 | Sequential |
| 15 | Final closing: deed, mortgage, TIC Agreement, OA, master lease, assignment of rents | All parties | Day 90 | Day 105 | Sequential |
| 16 | Recording of deed and TIC Agreement | Title company | Day 105 | Day 110 | Sequential |
| 17 | Member-meeting minutes; Form D analysis (in case fall-back to 506(b)) | Securities counsel | Day 90 | Day 110 | Parallel |
| 18 | Janet's and Ryan's Form 8824 prepared with each cotenant's tax preparer | Tax preparers | Year-end after closing | Tax-year filing | Sequential to closing |

**Critical-path constraints:**

- Janet's and Ryan's 45-day identification window starts the day each sells her relinquished property. Closing must fit within her 180-day exchange window. If Janet's relinquished property is already in escrow today, the user has 180 days to close. Coordinate this with item #15.
- The SBA lender's appraisal and environmental can take 30–60 days. Start at Day 14.
- The opinion letters (items 1 and 2) are non-negotiable gating items.

---

## 10. Risks That Survive Even The Recommended Structure

The user must accept these residual risks:

1. **§721 contribution-on-exit trap.** If, post-closing, Janet or Ryan ever contributes her TIC to the JV LLC in exchange for a JV LLC membership interest, the IRS can apply substance-over-form to recharacterize the original §1031 (per *Chase v. Commissioner*, 92 T.C. 874 (1989), as corrected in 01_1031_review.md Error #1). The two-year rule of §1031(f) and the *Magneson* line provide some cover, but a clean exit requires Janet and Ryan to sell their TIC interests separately at exit (each conducting her own §1031 if rolling forward).

2. **§1250 depreciation recapture on exit.** Per 01_1031_review.md Gap 2, depreciation recapture is triggered on any boot received. Janet's and Ryan's boot exposure depends on debt-share mismatch and cash boot at closing.

3. **Basis divergence among cotenants.** Janet's and Ryan's bases (carried over from their relinquished property under §1031) will be very different from the JV LLC's basis (= cash + sweat). Each cotenant has its own depreciation schedule. (Per 01_1031_review.md Gap 3.)

4. **Debt-share-mismatch boot at closing.** If Janet's or Ryan's relinquished property carried more debt than her share of the new $575K SBA, the difference is debt relief = boot under §1031(b) and Reg. §1.1031(d)-2. This must be modeled BEFORE the §1031 identification deadline. (Per 01_1031_review.md Gap 4.)

5. **TIC partners cannot match JV waterfall in upside scenarios.** Per 02_TIC_review.md "C. Same-economic-outcome unachievable," a static-percentage TIC cannot replicate a curved JV waterfall across return scenarios. Janet and Ryan ride pro-rata in good outcomes and pro-rata in bad; the JV LLC members capture all hospitality-operations alpha through HotelCo. The user has accepted this tradeoff.

6. **Hocking-style securities risk re-emerges if rental-pool features added later.** Per 04_JV_security_review.md gap #1 and 05_precedents_research.md §5A, if the deal ever evolves to offer outside investors a packaged condo + rental-pool product (or markets bookable units to retail investors), the entire offering can flip into an investment contract. The recommended structure expressly avoids this — but the user must commit to keeping it that way.

7. **SBA lender refusal.** Per 03_SBA_review.md Gap 4, most 7(a) lenders will refuse a TIC + JV co-borrower structure outright and require pre-closing rollup into a single LLC. The user may need to call multiple lenders. Identify a lender with EPC/OC experience early.

8. **Citizenship policy volatility.** Per 03_SBA_review.md Error #4, the March 2025 SBA Policy Notice on citizenship/EO 14159 has been a moving target. The current operative rule on LPR ownership and any de minimis exception must be confirmed with the lender's SBA contact at the time of application.

9. **Affiliation issues under §121.103.** If any member of Single Seed, Gideon, Tiffany, York, Janet, or Ryan has other operating businesses, the SBA size standard is tested on a combined basis (per 03_SBA_research.md "Affiliation"). Run §121.103(d), (f), (h) analysis early.

10. **State-law overlay risks.** Partition rights, homestead, community-property, transfer tax, Prop 13/19-style reassessment in California, and UPHPA in 24+ states (per 02_TIC_review.md Error #2). Confirm with state counsel in the property's state.

11. **No PLR available.** Per 05_precedents_review.md gap #2, the IRS stopped issuing affirmative TIC PLRs in 2009 (Rev. Proc. 2009-3). The user cannot get IRS comfort. Tax counsel's opinion at "should" or "more likely than not" level is the maximum comfort obtainable.

12. **Master-lease related-party tension.** Per 02_TIC_review.md "B. Master-lease cure has real complications," even with HotelCo separated from JV LLC, the JV LLC's ownership of HotelCo creates §6.13 "bona fide lease" tension if rent is too soft. The mitigation is rigorous FMV documentation at closing AND annual rent reviews.

---

## 11. Hand-Off Note (back to user)

**This week:**
- Engage tax counsel for the TIC opinion letter (Items 1 of the closing roadmap). Engage securities counsel for the JV-vs-security analysis memo (Item 2). Both engagements are gating items and have 21-day turnaround.
- Janet and Ryan should each engage a Qualified Intermediary (independent of you and each other; not your accountant, attorney, or real-estate agent — the §1.1031(k)-1(k) disqualified-person rules) and confirm their relinquished-property timelines.

**This month:**
- Form HotelCo LLC. Sign the SBA-preferred lender's term sheet. Run citizenship and §121.103 affiliation diligence on every direct and indirect owner. Begin §1031 boot analysis for Janet and Ryan based on their relinquished-property debt — this is the single biggest item that can kill the deal silently.
- Convert the $97K acquisition-fee item into capital-account credit at the JV LLC level (Section 3) and the 15% capital-raise allocation into pre-closing structuring sweat-equity recitals (Section 4). Get the OA recitals right because they are the contemporaneous record that defeats a future Williamson challenge.

**Before close:**
- Final tax opinion (TIC structure) and final securities opinion (JV non-security) in hand.
- Sources & uses balanced — confirm the ~$800K gap is filled (additional equity OR seller-financing on full standby OR larger SBA loan; we recommend a combination of (a) more equity and (b) seller note on full standby).
- TIC Agreement, JV LLC OA, and master lease all execution-ready and reviewed by every signer.
- Member meeting minutes documenting the structure and consents in place. PG forms (148 / 148L) signed by every required member and spouse.
- File Form D within 15 days of first equity sale as belt-and-suspenders backup, even if the JV is treated as a non-security under Williamson — costs nothing and provides litigation insurance if recharacterized later (per 04_JV_security_research.md "Closing Recommendation").

---

*This memo is the constructive companion to Synthesis Memo A's Diagnostic & Options analysis. It assumes the user wants to proceed with the deal and structures it to fit all four legal regimes — IRC §1031 + Rev. Proc. 2002-22; Williamson/Howey true-JV; SBA SOP 50 10 8 EPC/OC; and the practical lender-side reality. It accepts the user's stipulated tradeoff that Janet and Ryan will not match the JV LLC's upside in best-case scenarios — that tradeoff is the price of §1031 deferral and is structurally unavoidable under any compliant TIC. This is structuring guidance, not legal or tax advice; the tax-opinion and securities-opinion letters at Items 1 and 2 of the closing roadmap are gating.*
