# Diagnostic & Options Analysis

**Re:** Proposed structure for $1.9M hospitality/STR acquisition — JV LLC + TIC sidecar (Janet Ng, Ryan) + $575K SBA loan + $650K equity raise + ~$97K acquisition fee
**Prepared by:** Synthesis Agent A
**Date:** May 8, 2026
**Companion memo:** Synthesis Agent B (recommended structure & cap-table mechanics)

---

## 1. Executive Diagnosis

The structure as proposed by the user **does not work** under all four legal regimes simultaneously. Two of the four (TIC + JV-as-true-JV) fail outright; the other two (SBA + 1031) are conditional and only survive after the first two are fixed. The proposed economic table — in particular, allocating the **15% capital-raise bucket** to TIC partners (Janet 1.15%; Gideon 6.92%) and asserting that TIC partners will get the **"same economic outcome — no more, no less"** as JV partners — is structurally impossible inside Rev. Proc. 2002-22's safe-harbor envelope and structurally dangerous under Howey/Williamson.

Additionally, a hospitality/STR fact pattern injects two case-specific landmines that the user's plan does not address: (i) Rev. Rul. 75-374's "customary services" line, which excludes hotel-style services from the activities a TIC pool may perform, and (ii) *Hocking v. Dubois*, 885 F.2d 1449 (9th Cir. 1989) (en banc), which converts condo-hotel/rental-pool arrangements into investment contracts when the rental-management program is bundled with the real-estate sale.

### Compliance Grid

| Regime | Verdict | One-line reason |
|---|---|---|
| **True JV (no security)** | **FAIL as drafted** | The 15% capital-raise bucket is transaction-based compensation for soliciting passive money; the $97K (5.1% / 14.9%) acquisition fee looks like sponsor compensation; together these flip the JV into a Howey/Williamson investment contract regardless of "active member" labels. (See 04_JV_security_research.md §8 ¶6, ¶9; 04_JV_security_review.md ¶1.) |
| **TIC (Rev. Proc. 2002-22)** | **FAIL as drafted** | TIC partners cannot receive 15%-bucket "capital-raise" allocations (violates §6.08 proportionate-sharing); TIC partners cannot receive the "same economic outcome" as the JV waterfall (a static undivided % cannot replicate a curved waterfall — per 02_TIC_review.md §C); $97K acquisition fee at 5.1% must be defensible as FMV under §6.15 and almost certainly is not at that level; hospitality services would be "additional" not "customary" under Rev. Rul. 75-374. |
| **§1031** | **CONDITIONAL** | Inbound 1031 works only if the TIC arrangement is genuinely a co-ownership and not a partnership in fact. Every defect in the TIC compliance column above feeds back as a §1031 disqualifier (§1031(a)(1) treats partnership interests as non-real-property). Recharacterization = no deferral. |
| **SBA 7(a)** | **CONDITIONAL** | $575K cannot fund the $97K acquisition fee (use-of-proceeds rules); EPC/OC structure required only if there is a separate operating tenant — the deal does not currently identify one; lender-side reality is that most 7(a) lenders refuse a TIC + JV co-borrower and force a pre-closing rollup; every direct/indirect owner of EPC and OC must be a U.S. citizen under March 2025 Policy Notice (with material uncertainty about LPR/de minimis treatment per 03_SBA_review.md ¶4). |

**Bottom line.** As drafted, the structure breaks the TIC safe harbor, breaks the true-JV defense, and is unbankable to a typical SBA 7(a) lender. To recover, the user must pick exactly one of three real paths: (A) abandon the TIC sidecar and bring Janet/Ryan into the JV (they lose §1031); (B) keep a stripped-down TIC sidecar at the property level, with TIC partners limited to a pure pro-rata real-estate return (giving up the 15%-bucket and waterfall economics); or (C) accept that the deal is a securities offering and run it as Rule 506(b). Hybrid versions exist but introduce complexity disproportionate to a $1.9M deal.

---

## 2. Conflict Map

The conflicts below are listed roughly in order of severity. Each item identifies the source clause in the user's plan, the regime it breaks, the controlling rule, and a severity rating.

### Conflict 1 — TIC partners receiving 15%-bucket capital-raise allocation while sitting outside the JV
- **What the user wants:** Janet Ng allocated 1.15% of total equity from the "raise" bucket (raised $50K of $650K → 7.69% of the 15% bucket = 1.15%); Gideon Spencer allocated 6.92% from the same bucket. Both treated as TIC partners (Janet) or non-TIC active member with PG (Gideon).
- **Which regime it breaks:** Rev. Proc. 2002-22 §6.08 (proportionate sharing of profits and losses) and §6.15 (sponsor payments must be FMV and not based on profits) for any TIC owner; Securities Act §2(a)(1) and Howey/Williamson for the JV.
- **Why:** §6.08 requires Janet's economic share strictly tracking her undivided fee percentage. A "raise bucket" allocation is by definition a special allocation tied to a service rendered (capital-raising), not an undivided ownership percentage — that is the bright-line marker of partnership characterization (Reg. §301.7701-1(a)(2)). On the JV side, paying equity for the act of bringing in passive capital is the textbook fact pattern courts use to prove a Howey "common enterprise" with "efforts of others" — and per the corrected position in 04_JV_security_review.md ¶1, the 15% bucket is actually a Howey/Williamson trigger (not, as the original research stated, a free-standing §15(a) trigger).
- **Severity:** **Showstopper** for TIC partners (Janet must not receive any 15%-bucket allocation). Severe for the JV true-JV defense generally — the 15% bucket needs to be redesigned for everyone, not just Janet.

### Conflict 2 — TIC partners receiving "same economic outcome" as JV waterfall
- **What the user wants:** Janet's total equity = 12.69%, Ryan's = 15.38%, achieved as "same as allocated in the table — no more, no less," matching the JV waterfall.
- **Which regime it breaks:** Rev. Proc. 2002-22 §6.08; Reg. §301.7701-1(a)(2); §1031(a)(1).
- **Why:** Per 02_TIC_review.md §C, a static undivided percentage matches a JV waterfall **only at one return scenario**. Above that point JV partners receive promote that TIC owners cannot mirror; below it, TIC owners absorb losses pro rata in ways that JV protective structures (preferred returns, manager loans, equity catch-ups) would prevent. Trying to engineer the TIC into the curved waterfall by side-letter or fee adjustments converts the cotenancy into a partnership in fact. The "no more, no less" mandate cannot be obeyed inside a Rev. Proc. 2002-22-compliant TIC.
- **Severity:** **Showstopper** unless the user accepts that the TIC partners will get a different (typically lower at upside, similar at base case) return profile than the JV partners.

### Conflict 3 — $97K acquisition fee — magnitude and §6.15 / Williamson concerns
- **What the user wants:** $97K acquisition fee included in the $650K capital raise (~14.9% of equity, ~5.1% of purchase price), paid presumably to the sponsor/active organizers.
- **Which regime it breaks:** Rev. Proc. 2002-22 §6.15 (sponsor fee must be FMV); Williamson v. Tucker, 645 F.2d 404 (5th Cir. 1981); SEC v. Merchant Capital, 483 F.3d 747 (11th Cir. 2007); Long v. Shultz Cattle Co., 881 F.2d 129 (5th Cir. 1989).
- **Why:** Per 04_JV_security_review.md, syndication-market norms run 1–3% of purchase price; 5.1% is **well above** market and reads as syndication-style sponsor compensation rather than reimbursement for arm's-length services. On the TIC side, Janet and Ryan's portion of that fee is a transfer to the sponsor not justified by FMV services rendered to the TIC owners specifically — §6.15 requires that any fee to the sponsor be FMV and not contingent on profits. On the JV side, *Long v. Shultz* and *Merchant Capital* both treat per-deal fees flowing to organizers as direct evidence the venture is a sponsor/investor (i.e., security) dynamic.
- **Severity:** **Fixable.** Two cures: (i) shrink the cash fee to ≤ 2% of purchase price ($38K) and document the work; or (ii) eliminate the cash fee and credit the same dollar amount to active members' capital accounts as sweat equity (treating the fee as additional implied capital contribution rather than cash out). Cure (ii) is materially safer.

### Conflict 4 — $97K acquisition fee funded from SBA proceeds
- **What the user wants:** Implicit in the user's sources/uses — the $97K is bundled inside the $650K capital raise, with $575K SBA + $650K equity + (gap) seller note covering the $1.9M.
- **Which regime it breaks:** 13 CFR §120.130 (and §120.110 for passive-investment prohibitions); SBA SOP 50 10 8 use-of-proceeds rules.
- **Why:** Per 03_SBA_research.md and 03_SBA_review.md Gap 1, SBA proceeds **cannot** fund sponsor, acquisition, promote, or finder/broker fees. Even though the user's structure may not literally route the $575K through the acquisition fee, the sources/uses must be set up so that SBA $575K hits the property purchase price and the $97K is paid exclusively from non-SBA equity. If the use-of-proceeds disclosure to the lender shows SBA dollars touching the fee, the loan is denied or recalled.
- **Severity:** **Fixable** if the closing statement is structured cleanly; **showstopper** if the user only has $650K of equity and is implicitly relying on the SBA loan to free up cash for the fee. Run the math on sources/uses now: $1.9M cost = $575K SBA + ~$1.325M needed from equity + seller note + working capital. If $650K equity is to cover the property gap **and** the $97K fee **and** working capital, the deal is short. Verify before structuring.

### Conflict 5 — Hospitality/STR services + Hocking rental-pool conversion risk
- **What the user wants:** Member roles include "Guest Experience" and "Public Relations" — fact pattern is a boutique hotel or STR with active hospitality operations.
- **Which regime it breaks:** Rev. Rul. 75-374 (additional hospitality services convert co-ownership to partnership); *Hocking v. Dubois*, 885 F.2d 1449 (9th Cir. 1989) (en banc); *Salameh v. Tarsadia Hotel*, 726 F.3d 1124 (9th Cir. 2013).
- **Why:** Customary landlord services (maintenance, common-area cleaning, utilities) preserve TIC characterization. Hotel-style services (housekeeping, concierge, F&B, daily turnover, marketing pooled rental income) push the arrangement into partnership territory. *Hocking* held that condo + rental-pool option could be an investment contract: the package — real estate plus pooled-income management program — is the security. If the JV LLC pitches Janet and Ryan on "buy a TIC interest and we'll run the hotel," that pitch is *Hocking* on its face. Per 05_precedents_review.md ¶6, *Salameh* is the modern application directly on point for STR/condo-hotel structures.
- **Severity:** **Showstopper** if structured naively. Cure is structural: TIC pool must own only real estate; an Operating Company (separate from the JV LLC and from the TIC pool) must run the hospitality operations as the master tenant or sub-operator. Janet and Ryan's TIC return must not be tied in any way to hotel revenue beyond a fixed FMV master-lease rent (or a fixed % of gross under §6.13).

### Conflict 6 — TIC + JV co-borrower SBA structure / lender willingness reality
- **What the user wants:** A single $575K SBA 7(a) loan with the JV LLC + Janet + Ryan all on the note as TIC co-borrowers.
- **Which regime it breaks:** No regulation prohibits this, but per 03_SBA_review.md Gap 4, **most 7(a) lenders will refuse** the structure as too operationally awkward (separate UCC-1 attachments to undivided interests, joint-and-several enforcement headaches, PG attribution complexity). They require pre-closing rollup into a single LLC.
- **Severity:** **Fixable** by shopping aggressively for a TIC-friendly SBLC, but expect higher fees and one or two lender rejections. If no willing lender, the only option is rollup — which destroys the TIC and §1031.

### Conflict 7 — EPC/OC requirement (§120.110(c)) — does this deal even have a separate OC?
- **What the user wants:** Single JV LLC owning real estate and operating the property (members include "Guest Experience" and "PM/operations"). No identified separate OC.
- **Which regime it breaks:** 13 CFR §120.110(c); 13 CFR §120.111.
- **Why:** Per 03_SBA_review.md Gap 2, this is a binary question. (a) If the JV LLC itself operates the hospitality business (i.e., owns + operates), it is a single OC that happens to own its real estate — eligible directly under §120.131; **§120.111 does not apply at all**. (b) If the JV LLC is purely a landlord and a separate operating tenant runs the hotel, the JV LLC is an EPC and must satisfy §120.111 (lease, rent cap, assignment of rents, OC as co-borrower, every 20%+ owner of both EPC and OC must PG). The user has not specified which world the deal lives in. The TIC sidecar is what forces this question — if Janet/Ryan are real-estate co-owners and the JV LLC is the hospitality operator, then the TIC pool (Janet + Ryan + JV LLC) is the EPC and the JV LLC is also the OC. Per §120.111(b), the EPC and OC may not be parent/subsidiary of each other, but a JV LLC that is both a TIC member of the EPC and the OC creates an awkward overlap that requires careful separation.
- **Severity:** **Fixable** but unresolved. The user must answer: "is there a separate operating tenant, yes or no?" before structuring can advance. **This is one of the top 3 issues to resolve.**

### Conflict 8 — Citizenship / EO 14159 due diligence on every member
- **What the user wants:** The plan does not address citizenship of any member.
- **Which regime it breaks:** SBA Policy Notice 5000-865754 (March 2025), implementing Executive Order 14159.
- **Why:** Per 03_SBA_research.md and 03_SBA_review.md ¶4, SBA tightened citizenship/residency requirements in March 2025. The exact treatment of LPRs and the existence/scope of any de minimis exception is currently in flux and must be verified against the operative notice and any superseding SOP language. Conservative read: every direct and indirect owner of the EPC and OC must be a U.S. citizen or U.S. national with U.S. principal residence. If any member is an LPR, foreign national, or non-resident, the loan is ineligible and the deal must restructure to remove that owner from any 20%+ position (and possibly from any position).
- **Severity:** **Fixable diligence item**; **showstopper** if any member is non-citizen and refuses to exit. Run citizenship questionnaires on all 6–8 members today.

### Conflict 9 — Master lease — JV LLC cannot be both cotenant AND lessee
- **What the user wants:** Implicit. The cleanest cure for hospitality services is a master lease from the TIC pool to the JV LLC (or an operating affiliate). But the JV LLC is itself a TIC cotenant in the proposed structure.
- **Which regime it breaks:** Rev. Proc. 2002-22 §6.13 (bona fide lease at FMV, not based on net income) and the bright-line rule that a manager may not be a lessee under §6.12. The literal text of §6.13 doesn't prohibit a cotenant from also being lessee, but related-party leasing among cotenants creates §6.13 self-dealing tension and undermines the bona fide-lease defense.
- **Why:** Per 02_TIC_review.md §B and 01_1031_review.md gap 8, if the JV LLC sits on both sides of the master lease, the rent paid is a wash (the JV pays its own pro-rata share back to itself), and the lease serves no economic purpose other than to insulate the TIC owners — which the IRS will see through. Better practice: a separate operating LLC (not the JV LLC) is the master tenant.
- **Severity:** **Fixable.** Form a separate OperatingCo (call it "Hospitality OC LLC") owned by the active members. The JV LLC owns its TIC interest in the property only; OperatingCo is the master tenant; OperatingCo runs the hotel. This separation also resolves Conflict 7 cleanly.

### Conflict 10 — Multiple EPCs not allowed under SBA
- **What the user wants:** The TIC pool is treated by SBA as a single EPC (per 02_TIC_review.md ¶4 and 05_precedents_review.md ¶15). Not directly violated, but worth flagging.
- **Which regime it breaks:** None directly, but §120.111 frames "the EPC" as a single entity for compliance purposes.
- **Why:** SBA practitioner guidance treats a TIC arrangement holding the real estate as one EPC. Multiple separate EPCs are not allowed. The implication: every TIC owner must be on the loan as part of the unified EPC structure, with ownership look-through to all 20%+ direct or indirect owners — which means Janet (12.69%), Ryan (15.38%), and any JV LLC member crossing 20% indirectly. Single Seed (Beau + Jonas) at 33.62% indirect via the JV LLC will PG. Gideon Spencer at 15.77% indirect probably will not, unless the lender chooses to require it (lender discretion permitted).
- **Severity:** **Minor / informational**, but informs the PG matrix.

### Conflict 11 — 35-co-owner cap (§6.02) — not binding
Three TIC owners (JV LLC + Janet + Ryan), well under the cap. Verify and move on.

### Summary of severity counts
- **Showstoppers:** 1, 2, 5 (with 4, 7, 8 conditional)
- **Fixable:** 3, 4 (with care), 6, 9
- **Minor:** 10, 11

(Conflict 12 — static-percentage TIC cannot replicate curved JV waterfall across return scenarios — is the corollary of Conflicts 1 and 2 and is treated under Conflict 2.)

---

## 3. Pathway Options

Five distinct structural pathways. Each is a coherent, internally consistent legal architecture. Each requires the user to give up something they currently want.

### Option A — Pure True JV (Eliminate the TIC Sidecar)

**Structure:** A single JV LLC owns the real estate and operates the property. Janet Ng and Ryan are full members of the JV LLC, on the same operating agreement as the other partners, with active operational roles ("Guest Experience" and "Public Relations" as already proposed). No TIC. Janet and Ryan's $50K and $200K capital contributions go straight into the JV LLC. 1031 funds for Janet/Ryan are **disqualified** because IRC §1031(a)(1) excludes partnership/LLC interests from like-kind treatment. They pay tax on their relinquished-property gain in the year of relinquishment.

**How it satisfies/fails each regime:**
- **True JV:** PASS, provided the 15% capital-raise bucket is restructured (see economics below) and the $97K fee is converted to capital-account credit.
- **TIC:** N/A.
- **§1031:** FAILS for Janet and Ryan — they lose all 1031 deferral. They write the IRS a check.
- **SBA:** PASS, cleanly. JV LLC is a single 7(a) borrower; if it operates the property, no §120.111 EPC/OC structure required. PGs from all 20%+ direct owners.

**Who wins / who loses:**
- **Wins:** Operating simplicity, lender-friendliness, true-JV defense is at its strongest, exit flexibility (sale and §721 contributions both available without TIC drag).
- **Loses:** Janet (foregone §1031 deferral on her relinquished property — potentially tens or hundreds of thousands of dollars in current-year tax depending on her gain). Ryan same. They will need to be made whole some other way (additional equity %, reduced PG exposure, sponsor-cost coverage). Or they must accept the tax hit as the price of joining a true JV.

**Document set required:** JV LLC Operating Agreement, capitalization table, subscription agreements, PG documents (SBA Form 148), SBA loan documents, member acknowledgments of active participation. No TIC agreement. No master lease. No EPC/OC cross-documents.

**Time/cost to close:** **Fastest and cheapest** of the five options. Estimated 60–90 days from term sheet to close. Legal cost: $25–50K.

**Risk profile:** Lowest legal risk. Highest *individual tax* risk for Janet and Ryan unless they've already accepted that they'll pay current-year capital gains.

---

### Option B — Stripped TIC Sidecar (TIC for Property Only; JV Operates Separately)

**Structure:** Three-way TIC at the deed level: JV LLC + Janet + Ryan, with undivided percentages set so Janet and Ryan get *approximately* their target %s **as a pure pro-rata real-estate return**. Separate Hospitality OC LLC (owned by active partners; not the JV LLC and not a TIC member) is the master tenant under a Rev. Proc. 2002-22 §6.13-compliant lease at FMV. OC runs the hotel, takes the operating risk, makes the rent payments. TIC pool receives only rent and pro-rata sale proceeds.

**Critical concession:** Janet and Ryan **do not** receive any 15%-bucket capital-raise allocation. Their economics are limited to their TIC undivided percentage. Their target % must be set by **undivided fee interest**, not by waterfall logic. If the user's target was 12.69% for Janet and 15.38% for Ryan, the deed sets Janet at 12.69% and Ryan at 15.38% of the fee, full stop. The remaining 71.93% goes to the JV LLC as TIC owner.

**How it satisfies/fails each regime:**
- **True JV:** PASS for the JV LLC and its non-TIC members, conditional on (i) eliminating the 15% capital-raise bucket *for everyone* (or restructuring it as sweat-equity for pre-closing acquisition work performed by active members), (ii) converting the $97K fee to capital-account credit, (iii) Hocking-proofing the offering by ensuring no rental-pool/management-program pitch was made to Janet/Ryan.
- **TIC:** PASS, conditional on §6.01–§6.15 strict compliance — recorded TIC Agreement, unanimous voting on the Big 5 (sale, lease, refi, manager hiring, management contract), each TIC freely transferable, pro-rata sharing of all revenue and debt, FMV master-lease rent not based on net profits, sponsor fees at FMV, lender unrelated.
- **§1031:** PASS for Janet and Ryan. They each file their own Form 8824. Each holds a direct undivided fee interest in real property — the inbound qualifies as real property for §1031 purposes per Reg. §1.1031(a)-3.
- **SBA:** CONDITIONAL — depends on lender willingness (Conflict 6). EPC/OC framework applies: TIC pool = EPC; OperatingCo LLC = OC. Every 20%+ owner of either must PG. Mortgage covers 100% of fee. Master lease must be in writing, subordinated to SBA mortgage, rents assigned to lender, lease term ≥ loan term, rent capped at "loan payment + holding costs" per §120.111(a) and SOP 50 10 8.

**Who wins / who loses:**
- **Wins:** Janet and Ryan (full §1031 deferral preserved, both at intended equity %s as undivided fee interest). The JV LLC retains the upside above the base case (the entire promote sits inside the JV LLC's operating side because the operating economics flow through the OperatingCo, not through the TIC).
- **Loses:** Janet and Ryan (no upside above base case — they're real-estate landlords, not operating partners). At-the-base-case returns approximately match the proposed table; at upside, JV partners outearn TIC partners. The user cannot honor the "no more, no less" mandate and instead must concede that "no more, no less at the base case; less than the JV at upside" is the most §1031 can deliver.

**Document set required:** TIC Agreement (recorded, runs with the land), JV LLC Operating Agreement, OperatingCo LLC Operating Agreement, Master Lease (TIC pool ↔ OC), Management Agreement (if any — TIC pool ↔ third party; OC must not be the manager), QI agreements for Janet and Ryan, SBA loan and PG documents, citizenship certifications for all, FMV opinions for the master-lease rent and the $97K fee.

**Time/cost to close:** **Slowest and most expensive** of the five options. 4–6 months minimum from term sheet. Legal cost $80–150K (TIC drafting + master lease + EPC/OC + multiple QI engagements + multiple FMV opinions).

**Risk profile:** Moderate. Audit risk for Janet/Ryan is real (Rev. Proc. 2002-22 is not a true safe harbor — IRS halted PLRs in 2009 per Rev. Proc. 2009-3). Hocking risk if any rental-pool pitch was made. Lender risk per Conflict 6.

---

### Option C — Reg D 506(b) Syndication (Drop the True-JV Goal)

**Structure:** A single JV LLC, manager-managed by Single Seed (Beau + Jonas) as managing member. All other partners (including Janet and Ryan) are passive investors. Standard PPM, subscription docs, accreditation/sophistication questionnaires, Form D filed within 15 days of first sale. Fee/promote structure freely permitted (acquisition fee, asset-management fee, disposition fee, promote — all market-rate and disclosed). Janet and Ryan still lose §1031 because the LLC interest is not real property.

**How it satisfies/fails each regime:**
- **True JV:** N/A — concedes the issue. The interest is a security; the offering is exempt from registration under Rule 506(b).
- **TIC:** N/A — no TIC.
- **§1031:** FAILS for Janet and Ryan (LLC interest not like-kind to real property).
- **SBA:** PASS. Single LLC borrower. Standard PG matrix. Operationally the cleanest of all five options on the SBA side.

**Who wins / who loses:**
- **Wins:** The active operating partners, who can run a real syndication-style waterfall, take a real promote, charge real fees, and grow this into a repeatable platform (Deal 2, Deal 3, etc., all on the same playbook).
- **Loses:** Janet and Ryan again on §1031. The user's "active members only / no passive members" mandate is overtly abandoned.

**Document set required:** PPM, Subscription Agreement, Accredited Investor Questionnaire, JV LLC Operating Agreement (manager-managed), Form D, Bad-Actor Diligence on every covered person under Rule 506(d), state notice filings in each state of purchaser residence.

**Time/cost to close:** Moderate. 90–120 days. Legal cost $40–70K (PPM is the main cost driver).

**Risk profile:** Low legal risk if executed correctly — Reg D 506(b) is well-trodden and federal preemption (NSMIA / §18) handles state issues. Higher operational risk if general solicitation slips in (most common failure mode).

---

### Option D — Hybrid: Most Partners as True JV; Side-by-Side Reg D 506(b) Sub-Fund for Passive Capital

**Structure:** Two-tier. Tier 1: JV LLC, member-managed by 4–5 active operating partners only (Single Seed, Gideon, Tiffany, Janet, Ryan as active members with operational roles). Tier 2: a separate Sub-Fund LLC, organized as a Reg D 506(b) issuer, raises additional passive capital from a small group of accredited investors and itself becomes a member of the JV LLC. Janet and Ryan can elect into either tier (TIC sidecar attached to the deed if they need 1031, or membership in Sub-Fund if not).

**How it satisfies/fails each regime:**
- **True JV:** PASS for Tier 1 if all 4–5 active members are operationally active (defined roles, voting, removal rights, no broker-dealer-style 15% raise bucket).
- **TIC:** OPTIONAL — only if Janet/Ryan keep the TIC sidecar (then Option B's analysis applies).
- **§1031:** Available only via the TIC path (Option B).
- **SBA:** CONDITIONAL — additional complexity in §121.103 affiliation analysis (Sub-Fund as a JV member with its own owners requires look-through and may aggregate at the SBA level). Lender will scrutinize.

**Who wins / who loses:**
- **Wins:** Operational flexibility — the JV LLC can be a true JV at Tier 1, while still raising capital from people who don't want active roles via Tier 2.
- **Loses:** Complexity. Two issuers, two sets of documents, two regulatory tracks (true JV + Reg D), two layers of affiliation analysis at SBA. Disproportionate to a $1.9M deal.

**Document set required:** All of Option B + all of Option C + a Sub-Fund Operating Agreement + intercreditor / intermember provisions.

**Time/cost to close:** Slowest. 5–7 months. Legal cost $100–200K.

**Risk profile:** Moderate. Doubles the documentation surface area; doubles audit/diligence exposure. Hybrid options are usually a sign that the deal is trying to do too many things at once.

---

### Option E — Single-LLC Operating Company (No TIC, No Sidecar)

**Structure:** Simplest possible. A single LLC ("OpCo LLC"). Owns the real estate. Operates the hotel. All members (including Janet and Ryan) are direct active members. Roles assigned. PGs collected from 20%+ owners. SBA 7(a) loan against the property; LLC itself is the borrower. Acquisition fee converted to capital-account credit for active members who did pre-closing work. No 15% capital-raise bucket — that bucket is absorbed into the 35% sweat-equity bucket and re-allocated to the people who actually performed pre-closing work.

**How it satisfies/fails each regime:**
- **True JV:** PASS. Clean Williamson/Robinson defense — every member has a defined role, exercises voting rights, and has PG'd. No fee/promote dynamic. No general solicitation.
- **TIC:** N/A.
- **§1031:** FAILS for Janet and Ryan.
- **SBA:** PASS. Single 7(a) borrower. No EPC/OC issue (OpCo owns + operates; passive-landlord rule doesn't bite). PGs collected. Citizenship verified.

**Who wins / who loses:**
- **Wins:** The deal closes on time and on budget. Operations are uncomplicated. The structure is repeatable.
- **Loses:** Janet and Ryan on §1031 (same as Options A and C).

**Document set required:** OpCo Operating Agreement, capitalization table, subscription agreements, PG documents, SBA loan docs.

**Time/cost to close:** Fastest. 60–75 days. Legal cost $20–40K.

**Risk profile:** Lowest. This is the structure that survives every challenge.

---

### Comparative Summary

| Option | TIC | True JV | §1031 OK for Janet/Ryan | SBA-clean | Time | Cost | User's "no more, no less" honored? |
|---|---|---|---|---|---|---|---|
| **A. Pure JV** | No | Yes | No | Yes | Fast | Low | Yes (everyone in JV; full waterfall) |
| **B. Stripped TIC Sidecar** | Yes | Yes (with fixes) | Yes | Conditional | Slow | High | No (TIC ≠ JV waterfall) |
| **C. Reg D 506(b)** | No | No (concedes) | No | Yes | Medium | Medium | Yes (full waterfall, but a security) |
| **D. Hybrid** | Optional | Tier 1 only | Optional via TIC | Conditional | Slowest | Highest | Partial |
| **E. Single-LLC OpCo** | No | Yes | No | Yes | Fastest | Lowest | Yes (full waterfall) |

---

## 4. Decision Tree

```
Q1: Is preserving §1031 deferral for Janet and Ryan a hard requirement?
├── NO  → Q2: Do you want a true JV defense (no security)?
│         ├── YES → Q3: Is the deal a single operator (no separate OC tenant)?
│         │         ├── YES → OPTION E (Single-LLC OpCo)  ← simplest, fastest
│         │         └── NO  → OPTION A (Pure JV with EPC/OC if needed)
│         └── NO  → OPTION C (Reg D 506(b))
└── YES → Q4: Are you willing to accept that Janet/Ryan's TIC return
              cannot equal the JV waterfall above the base case?
          ├── YES → OPTION B (Stripped TIC Sidecar)
          └── NO  → No legally compliant option exists.
                    Re-engage Q1: §1031 vs. equal-waterfall is a binary choice.

Side question (always run): Are all owners U.S. citizens?
├── YES → continue
└── NO  → SBA path is closed unless non-citizens are removed
          from any 20%+ position (and possibly all positions)
          per March 2025 Policy Notice 5000-865754.
```

**Short version.**
- If §1031 doesn't matter for Janet/Ryan → **Option E** (or Option A if you need EPC/OC separation).
- If §1031 matters AND you accept TIC partners get less than JV partners on upside → **Option B**.
- If you want maximum operational flexibility and are willing to be a security → **Option C**.
- **Option D is rarely worth the complexity at $1.9M.**

---

## 5. Top 3 Issues to Resolve Before Close

These are the questions where the entire structure pivots. The user must answer them in writing before any deal counsel begins drafting.

### Issue 1 — Is there a separate Operating Company, or does the JV LLC operate the hotel directly?

This determines whether §120.111 EPC/OC framework applies at all. Two completely different structural worlds:

- **No separate OC:** JV LLC owns + operates. Single 7(a) borrower. No EPC/OC documents. No master lease. Hospitality services come from the JV LLC. No TIC sidecar (or, if TIC sidecar, the JV LLC is one TIC and operates by virtue of leasing its own pro-rata share — awkward).
- **Yes separate OC:** TIC pool (or JV LLC alone) is the EPC, leasing 100% to OperatingCo OC. OC runs the hotel. EPC/OC compliance under §120.111 is mandatory: written lease, subordinated to SBA mortgage, assignment of rents, OC as co-borrower under 7(a), every 20%+ owner of EPC and OC must PG, citizenship verified for all.

The user said the structure is "likely" hospitality based on member roles. The user must declare which world the deal lives in before any structuring document can be drafted. This is the most important unanswered question on the table.

### Issue 2 — Are all owners U.S. citizens (or U.S. nationals with U.S. principal residence)?

Every direct and indirect owner of every entity that touches the SBA loan must be vetted under SBA Policy Notice 5000-865754 (March 2025). The treatment of LPRs and any de minimis exception is currently in flux per 03_SBA_review.md ¶4 — pull current operative notice text before relying on any old summary. If any partner is a non-citizen, a foreign national, or a non-resident, three immediate consequences:

- Cannot hold ≥20% ownership without disqualifying the loan.
- May not be allowed to hold any percentage at all under conservative current guidance.
- The PG matrix changes — non-citizens may not be allowed to PG.

Run citizenship questionnaires today on Single Seed (Beau + Jonas), Gideon Spencer, Tiffany Zhou, Janet Ng, York, Ryan, and any other partner. The names alone don't tell you. Ask.

### Issue 3 — What is the precise property type and operating model — and specifically, has any of the partners' equity or the TIC partners' interest been pitched as part of a rental-pool or hospitality-management program?

This determines (a) whether *Hocking v. Dubois* / *Salameh v. Tarsadia Hotel* applies (rental-pool security risk) and (b) whether the TIC pool can satisfy Rev. Rul. 75-374's "customary services only" line. Three sub-questions:

1. Is the property a boutique hotel, an STR, a multifamily building with rental-pool, or something else?
2. Were Janet and Ryan pitched on the deal in any way that bundled the real estate purchase with the JV LLC's hospitality-management capability or projected operating income? If yes → security characterization is presumed.
3. Will the TIC pool itself perform any hospitality services (housekeeping, concierge, F&B) directly, or will all such services be performed by a separate OperatingCo? If TIC pool performs them → partnership recharacterization is presumed.

If the answer to (2) is yes, the deal is presumptively a security, and Option C (Reg D 506(b)) becomes the only legally clean path.

---

## 6. Hand-off to Synthesis Agent B

Synthesis Agent B should pick up where this memo leaves off: **assume the user will choose Option B (Stripped TIC Sidecar) if §1031 deferral is preserved, or Option E (Single-LLC OpCo) if §1031 is conceded.** Build out the recommended structure detail for **both** of these endpoints, since the user has not yet answered Issue 1 above.

Specifically, Agent B should produce:

1. **Entity diagram for Option B** (TIC pool ↔ JV LLC ↔ OperatingCo LLC ↔ SBA lender) with labeled cash flows: equity in, rent up, debt service, distributions out. Identify which entity holds title, which entity holds the lease, which entity holds the operating P&L, which entity is the SBA borrower, which entity is the OC, and which entity each member sits inside.

2. **Entity diagram for Option E** (Single OpCo) — much simpler; one entity diagram and one cap table.

3. **Recommended cap-table modifications to hit the target percentages within each option.** For Option B specifically, work out the math: if Janet's target total equity is 12.69% and her TIC must deliver that purely as undivided fee, what is her actual undivided %, and what does she give up in upside? Show the trade-off in dollars at base/upside/downside scenarios.

4. **Treatment of the 15% capital-raise bucket.** Synthesis A's recommendation: convert the 15% bucket into pre-closing sweat-equity for documented acquisition/underwriting work performed by active members; eliminate any allocation tied to dollars raised from third parties. Agent B should propose specific language and a re-allocated cap table that achieves the user's totals without the broker-dealer/Williamson trigger. Note: Janet's 1.15% raise allocation and Gideon's 6.92% raise allocation must be re-derived as either (a) sweat-equity for documented work, or (b) eliminated and absorbed into other buckets.

5. **Treatment of the $97K acquisition fee.** Recommendation: convert to capital-account credit for active members who did pre-closing acquisition/diligence work, with documented hours and deliverables. No cash fee at closing. Agent B should propose the capital-account math and the specific OA language.

6. **PG matrix** with named persons and look-through %s for both Option B and Option E. Identify whether Gideon (15.77%) is a mandatory PG or discretionary. Identify whether Tiffany (9.85%) requires a PG. Confirm Single Seed's combined % requires PG.

7. **A short closing-checklist** of every document, every diligence item, and every signature required to get to close, ordered by sequence.

8. **The "what ifs"** — what happens at exit (sale, refi, partner buyout) under each option. The §721 contribution risk on Option B exit is real (per 01_1031_review.md gap 1) and Agent B should walk through what happens if Janet/Ryan later want to roll into the JV LLC after holding the TIC for 24+ months.

Agent B should NOT re-diagnose the conflicts identified here. Take the conflict map as given, take the recommended fixes (no 15% raise bucket; convert acquisition fee to capital-account credit; require separate OperatingCo if hospitality services exist; verify citizenship for all) as preconditions, and build the structure on that foundation.

---

**Sources cited:**
01_1031_research.md; 01_1031_review.md; 02_TIC_research.md; 02_TIC_review.md; 03_SBA_research.md; 03_SBA_review.md; 04_JV_security_research.md; 04_JV_security_review.md; 05_precedents_research.md; 05_precedents_review.md.

**This memo is research synthesis; it is not legal or tax advice. The user must engage qualified tax, securities, and SBA counsel before executing any of the structures described.**
