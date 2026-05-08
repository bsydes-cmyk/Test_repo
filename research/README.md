# Real-Estate Structure Analysis — Index

**Branch:** `claude/real-estate-structure-analysis-fxMau`
**Deal:** $1.9M hospitality/STR/boutique-hotel acquisition, $575K SBA loan, $650K equity raise across seven principals, with proposed TIC sidecar (Janet Ng + Ryan) for §1031 exchange purposes.

This research was produced by a 12-agent multi-wave analysis: 5 parallel research agents, 5 parallel review agents auditing them, then 2 synthesis agents mapping all findings to the deal.

---

## Read-Order

For decision-makers, read in this order:

1. **`03_synthesis/A_diagnostic_and_options.md`** — what is broken and what your options are
2. **`03_synthesis/B_recommended_structure.md`** — the specific recommended structure with cap-table math, document checklist, and closing roadmap
3. The Wave 1 research and Wave 2 reviews are reference material; consult specific topics as needed.

The two synthesis memos are written to be read together — A diagnoses, B prescribes.

---

## File Inventory

### Wave 3 — Synthesis (read these first)

| File | Length | Purpose |
|---|---|---|
| `03_synthesis/A_diagnostic_and_options.md` | ~6,000 words | Diagnoses every conflict between the proposed structure and the four legal regimes (true JV / TIC / 1031 / SBA); presents 5 pathway options with pros/cons; decision tree; top 3 issues to resolve |
| `03_synthesis/B_recommended_structure.md` | ~7,700 words | Specific three-tier recommended structure (TIC at title / JV LLC at equity / OC at operating); restated cap table with math; $97K fee restructuring; sources & uses; OA/TIC/master-lease provisions checklist; SBA underwriting package; PG matrix; 18-step closing roadmap; residual risks |

### Wave 2 — Review (independent audit of research)

Each review agent independently verified citations against IRS, Treasury, federal court, SEC, and SBA primary sources, flagged errors, and noted gaps.

| File | Verdict | Headline finding |
|---|---|---|
| `02_review/01_1031_review.md` | YELLOW | *Chase v. Comm'r* citation wrong (correct: 92 T.C. 874 (1989)); T.D. 9935 effective date Dec 2 not Nov 23; Rev. Rul. 79-77 mischaracterized; §1031(a)(2)(D) doesn't exist post-TCJA. Missing §721 exit trap, §1250 recapture, basis divergence, debt-share boot. |
| `02_review/02_TIC_review.md` | YELLOW | Treas. Reg. §301.7701-1(a)(2) quote sequence inverted; UPHPA = 24 states + DC + USVI not "over 20"; "same economic outcome — no more, no less" is structurally unachievable inside a safe-harbor TIC; SBA "TIC = single EPC" rule should be added. |
| `02_review/03_SBA_review.md` | YELLOW | SOP 50 10 7.1 citations stale (now SOP 50 10 8); §120.160(c) hazard threshold wrong; Citizenship Notice (EO 14159) LPR claim overstated. $97K acquisition fee cannot come from SBA proceeds. Most lenders reject TIC + JV co-borrower deals — likely require rollup. |
| `02_review/04_JV_security_review.md` | YELLOW | Material legal error: Exchange Act §15(a) broker-dealer rule is **NOT Howey-independent** — it only applies if the underlying interest is a security. *Hocking v. Dubois* rental-pool risk named but unanalyzed (critical for hospitality deal). |
| `02_review/05_precedents_review.md` | GREEN-leaning-YELLOW | All citations real; no fabrications. Bluerock Ex. 10.3 may be Fox Hills not 23Hundred; *Robinson v. Glynn* "two of three" board seats is actually "two of seven." Bluerock $61M institutional REIT is a scale mismatch for a $1.9M deal — useful as form, not as commercial precedent. |

### Wave 1 — Research

| File | Length | Sources |
|---|---|---|
| `01_research/01_1031_research.md` | ~4,300 words | IRS Rev. Proc. 2002-22, Reg. §1.1031, IRC §1031, Treasury T.D. 9935, federal cases on drop-and-swap, related-party, identification, holding period |
| `01_research/02_TIC_research.md` | ~3,500 words | Treas. Reg. §301.7701-1(a)(2), Rev. Proc. 2002-22 §§6.01-6.15 quoted, Bergford / Madison Gas / Bussing partnership-recharacterization cases, SBA SOP, SEC Howey/investment-contract treatment of TICs |
| `01_research/03_SBA_research.md` | ~3,500 words | SBA SOP 50 10, 13 CFR Part 120 (especially §120.110, §120.111 EPC/OC, §120.160 PGs, §120.882 504, §121.103 affiliation), Citizenship Policy Notice 5000-865754 |
| `01_research/04_JV_security_research.md` | ~3,500 words | *Howey*, *Williamson v. Tucker*, *Robinson v. Glynn*, *Merchant Capital*, *Long v. Shultz*, *Shields*, *Arcturus*, *Hocking*, *Holden*, *Koch*; Securities Act §§2/4(a)(2)/18; Reg D 506(b)/(c); Form D; Exchange Act §15(a) |
| `01_research/05_precedents_research.md` | ~3,000 words | Bluerock Stonehenge 23Hundred TIC + JV (SEC EDGAR); PLRs 200513010, 200327003; CityCenter Boutique Hotel OA; Hospitality Investors Trust; SEC v. Sky Group; SEC CF Disclosure Topic No. 6 |

---

## Key Bottom-Line Findings (synthesizer's summary)

1. **The structure as proposed fails three of four regimes.** True JV defense fails (15% capital-raise bucket + 5.1% acquisition fee = Howey/Williamson trigger); TIC fails (Janet's 1.15% raise allocation violates §6.08 proportionate-sharing; "same economic outcome — no more, no less" is structurally impossible alongside §1031 deferral); §1031 conditional on TIC compliance; SBA conditional on resolving the EPC/OC question and lender willingness.

2. **The single biggest structural impossibility is the "same economic outcome — no more, no less" mandate.** A static-percentage TIC cannot replicate a curved JV waterfall across return scenarios. Above the waterfall preference, JV partners get the promote that TICs cannot mirror. The user must choose between (a) §1031 deferral OR (b) economic equivalence with the JV — not both.

3. **The hospitality fact pattern injects two case-specific risks** the user's plan doesn't address: Rev. Rul. 75-374 (TIC pool can only do "customary" services, not hotel-style services like daily housekeeping, F&B, concierge) and *Hocking v. Dubois* / *Salameh v. Tarsadia Hotel* (rental-pool conversion to security). Cure: a separate Operating Company runs hospitality; the TIC pool is purely a real-estate landlord.

4. **The recommended structure (Memo B) is three-tier:**
   - **Title layer (EPC):** TIC pool — JV LLC ~73%, Janet ~12.7%, Ryan ~14.3%
   - **Equity layer:** JV LLC member-managed by 5 active principals (Single Seed, Gideon, Tiffany, York, plus sweat reserve); Janet and Ryan are NOT JV members
   - **Operating layer:** Separate HotelCo LLC as master tenant under Rev. Proc. 2002-22 §6.13-compliant master lease (FMV rent + fixed gross-receipts %)

5. **Three structural cures embedded in the recommendation:**
   - $97K acquisition fee → JV-LLC capital-account credit to Single Seed (cures SBA prohibition + Williamson red flag + §6.15 FMV concern)
   - 15% capital-raise bucket → reframed as pre-closing structuring sweat-equity for active members only (neutralizes Howey/Williamson passivity risk)
   - JV LLC separated from HotelCo (cures §6.12 manager-as-lessee tension; allows hospitality services to live in OC, not TIC)

6. **Top 3 unanswered facts that gate any structuring decision:**
   - Is there a separate Operating Company tenant, or does the JV LLC itself operate the hotel?
   - Are all 6-8 owners U.S. citizens? (EO 14159 / SBA Policy Notice 5000-865754, current operative version)
   - Has the deal been pitched to anyone as a bundled rental-management program? (*Hocking* / *Salameh* risk)

7. **Funding gap.** Sources & uses analysis (Memo B §5): $1.9M deal cost requires $575K SBA + $650K equity + ~$675K still uncovered. The user must either raise more equity (above the $650K), arrange seller financing on full standby, or close at a lower acquisition price.

---

## Important Caveats

- **This is research, not legal or tax advice.** Three opinions are needed before close: tax counsel on TIC/§1031 compliance, securities counsel on JV-vs-security, and SBA-experienced counsel on the loan structure.
- **Web access was constrained** in the agent sandbox during some research, so several primary-source URLs were verified via secondary search rather than direct fetch. Reviews flagged anywhere this matters.
- **SBA SOP 50 10 8 effective date and current operative Citizenship Policy Notice** should be re-verified before closing — the agents flagged these as live items where SBA has revised guidance more than once in the past 18 months.
- **The "Beau + Jonas" Single Seed look-through math** for personal-guarantee threshold purposes (20%+) needs to be done explicitly with their actual sub-percentages before the lender file is built.

---

## Agent Map (for transparency)

- **Wave 1 (parallel research):** 1031, TIC, SBA, JV/security, precedents
- **Wave 2 (parallel review):** independent audit of each Wave 1 memo against primary sources
- **Wave 3 (parallel synthesis):** A diagnoses; B prescribes

Total: 12 agents, ~50,000 words of analysis, all citations to IRS/Treasury/federal court/SEC/SBA primary sources except where the agents explicitly flagged secondary verification.
