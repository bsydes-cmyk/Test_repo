# SBA Loan Protocols — Research Memo

## Deal at a Glance
- $1.9M real estate acquisition; $575K SBA loan request
- Borrower: JV LLC + two TIC co-owners (Janet Ng, Ryan) holding fractional interests outside the LLC
- PG signers: Single Seed (Beau + Jonas), Gideon Spencer, Janet Ng, Ryan
- Both 7(a) and 504 are theoretically available

---

## Executive Summary (5 bullets)

1. **The deal almost certainly requires an EPC/OC (Eligible Passive Company / Operating Company) two-entity structure under 13 CFR 120.111.** A JV LLC + TIC owners holding real estate and leasing it to a tenant is the textbook fact pattern that 13 CFR 120.110(c) renders ineligible (passive landlord) — except when the strict 120.111 conditions are met.

2. **At $575K against a $1.9M purchase, the SBA portion is only ~30% LTV — well within either program's parameters,** but the structures differ dramatically. **504** typically requires a CDC second behind a third-party first lien (50/40/10). **7(a)** requires the lender to take a first lien on the financed real estate.

3. **Personal guarantees are mandatory for every 20%+ direct or indirect owner of the EPC and the OC** under 13 CFR 120.160(a) and 13 CFR 120.111(a)(4). Less-than-20% owners can be required to PG (full or limited Form 148/148L) at lender discretion.

4. **Blanket UCC-1 lien on all business assets is the default for 7(a) loans** that are not "fully secured" by the financed real estate alone. For 504, a real-estate-only mortgage is the standard structure.

5. **TIC co-borrowers are permissible under SBA but operationally awkward.** SBA does not prohibit multiple co-borrowers on one note, but every fractional owner must either be a co-borrower granting a mortgage on its undivided interest, or join in granting a mortgage covering the entire fee.

---

## 7(a) vs 504: Which Fits This Deal

| Feature | **7(a)** | **504** |
|---|---|---|
| Governing regs | 13 CFR Part 120, Subparts A & B | 13 CFR Part 120, **Subpart H** |
| Max loan | $5M | CDC portion typically up to $5M ($5.5M for manufacturing/energy) |
| Structure for $1.9M / $575K | One SBA-guaranteed note from the 7(a) lender; remainder from borrower equity + seller financing | 50% third-party bank first / 40% CDC debenture second / 10% borrower equity — **the $575K does not match the typical 504 50/40/10 split unless the bank first is also part of the deal** |
| Lien on real estate | Lender takes first mortgage on the acquired real estate | Third-party lender takes first; CDC takes second (13 CFR 120.920–.921) |
| Blanket UCC-1 on business assets | **Yes, default** — required if loan not "fully secured" by RE alone | Not required for the CDC; third-party lender may impose under its own policies |
| Equity injection | Lender's prudent practices | 10% / 15% / 20% per 13 CFR 120.910 |
| "Credit elsewhere" test | Required (13 CFR 120.101) | Required, but applied differently |
| Use of proceeds | Real estate, working capital, refinance, equipment (13 CFR 120.120) | Long-term fixed assets only; **no working capital** (13 CFR 120.882) |
| Occupancy rule | 51% existing / 60% new construction (13 CFR 120.131) | Same: 51% / 60% |
| EPC/OC permitted | Yes (13 CFR 120.111) | Yes (13 CFR 120.111 applies across Part 120) |
| Best fit here | **Likely 7(a)** if the $575K is the only SBA piece and there is no third-party bank first | **504** only fits if there is a separate third-party 50% first lien |

---

## Blanket Lien vs. Non-Blanket Lien Decision Table

Authority: SOP 50 10 7.1, Section A, Chapter 5 (collateral); 13 CFR 120.160(b).

| Scenario | Blanket UCC-1 on all business assets? | Real estate mortgage? | Other |
|---|---|---|---|
| 7(a) loan ≤ $50,000 | Not required | Lender's prudent practice | Most relaxed tier |
| 7(a) loan $50,001 – $500,000 | Lender follows its own policy for similarly sized non-SBA loans | First lien on financed RE required | Personal RE not required if lender doesn't take it on similar conventional loans |
| 7(a) loan > $500,000 (this deal at $575K) | **Required** — lender must take a lien on all fixed assets and a blanket UCC-1; if not "fully secured," must take a lien on personal RE of every 20%+ owner where LTV ≤ 75% (residential) | First lien on financed RE required | Hazard insurance required on all collateral > $500,000 (13 CFR 120.160(c)) |
| 7(a) EPC/OC, working-capital portion | Lien on OC's business assets (it is a co-borrower under 120.111(a)(5)) | First mortgage on EPC's RE | Assignment of rents from EPC to lender (120.111(a)(3)) |
| 504 — third-party first | Not blanket; first mortgage on Project Property (13 CFR 120.920) | First lien | Third-party lender's normal lien practices |
| 504 — CDC debenture second | No blanket; second lien on Project Property (13 CFR 120.921) | Second lien | CDC may require additional collateral if Project is under-collateralized |
| Cross-collateralization with another entity | Permitted but disfavored | Allowed where the other entity has a guarantor relationship | Watch §121.103 affiliation effects |
| Junior lien acceptability | Junior lien on third-party real estate is acceptable for 7(a) collateral coverage when senior lien is from non-related party | Yes, on outside collateral | Lender must verify equity at the junior position |

**Why the rule exists:** 13 CFR 120.150 requires the loan be "so sound as to reasonably assure repayment," and 120.160(b) authorizes SBA to require collateral as a loan condition.

---

## EPC/OC Two-Entity Structure (13 CFR 120.111)

**Why it applies here:** 13 CFR 120.110(c) makes ineligible "passive businesses owned by developers and landlords that do not actively use or occupy the assets acquired or improved with the loan proceeds." A JV LLC plus TIC co-owners that owns real estate and leases it to a tenant operator is a textbook passive landlord — **ineligible** unless every 120.111 condition is met.

### Diagram (described)

```
                              SBA / 7(a) Lender (or CDC)
                                       |
                          ___________ Loan ___________
                         |                            |
                         v                            v
        EPC = JV LLC + Janet (TIC) + Ryan (TIC)   Operating Company (OC)
        — Owns the real estate                    — Tenant of the EPC
        — Borrower of record                      — Co-borrower under 120.111(a)(5)
        — Grants first mortgage to lender         — Grants UCC-1 on its
        — Assigns rents to lender                   business assets
                         ^                            |
                         |     written subordinated   |
                         |--------- LEASE ------------|
                                                      |
                                                      v
                                        Owners of OC (PG'd if ≥20%)
```

### Step-by-step requirements (with citations)

1. **Use of proceeds limited (120.111(a)(1)):** EPC may only use loan proceeds to "acquire or lease, and/or improve or renovate, real or personal property … that it leases to one or more Operating Companies for conducting the Operating Company's business."

2. **Lease in writing & subordinated (120.111(a)(2) and (a)(3)):** The EPC-OC lease must be in writing; its remaining term must be at least the loan term; and the lease must be **subordinate to SBA's mortgage**. Rent cannot exceed the amount necessary to cover the loan payment plus EPC's direct holding costs.

3. **Assignment of rents (120.111(a)(3)):** EPC must assign all rents under the lease to the lender as collateral.

4. **Guarantor net (120.111(a)(4) — "20% rule applied to BOTH entities"):** **Each holder of an ownership interest constituting at least 20 percent of either the EPC or the OC must guarantee the loan.**

5. **OC must be co-borrower or guarantor (120.111(a)(5)):** "The Operating Company must be a guarantor or, in the case of a 7(a) loan, a co-borrower."

6. **No subsidiaries / parents (120.111(b)):** Neither the EPC nor the OC may itself be the same as or a subsidiary/parent of the other.

7. **Active operating use (120.110(c) by inference):** The OC must actually occupy and use the property (51%/60% occupancy rule).

### Practical takeaways for this deal

- The JV LLC + Janet Ng + Ryan together comprise the **EPC**. Each TIC must sign as co-borrower or co-grantor of the mortgage.
- An identifiable **OC** must exist — there must be an operating tenant.
- Every 20%-or-greater owner of either the EPC (looking through the JV LLC to Single Seed / Gideon Spencer, plus the direct TIC owners) **and** every 20%-or-greater owner of the OC must sign a personal guarantee.

---

## Personal Guarantee Matrix

Authorities: 13 CFR 120.160(a), 13 CFR 120.111(a)(4), SOP 50 10 7.1; SBA Forms 148/148L.

| Person / entity | Mandatory PG? | Form | Notes |
|---|---|---|---|
| Direct ≥20% owner of EPC | **Yes — full unconditional PG** | 148 | 120.160(a) and 120.111(a)(4) |
| Indirect ≥20% owner via JV LLC (look-through) | **Yes if look-through reaches ≥20%** | 148 | SBA looks through holding entities |
| <20% owner with PG marked in cap table | Permissive | 148 or 148L | Voluntary PGs are generally valid |
| Operating Company (entity) | **Yes, as co-borrower or guarantor** (120.111(a)(5)) | Co-borrower in note, or 148 | For 7(a) with working capital, OC must be co-borrower |
| Spouse with no ownership but joint personal RE collateral | Limited "collateral pledge" PG via 148L | 148L | Equal Credit Opportunity Act, Reg B 12 CFR 1002.7 |
| Spouse owning <20% individually but combined household ≥20% | **Yes — full PG of the spouse** | 148 | SOP 50 10 7.1 aggregates spouse + minor children |
| Trusts holding ownership | Trust + trustee both PG; if revocable, grantor also PGs | 148 | SOP 50 10 7.1 §A Ch. 5 |
| ESOP | Not eligible to PG | n/a | SOP 50 10 7.1 §A Ch. 5 |
| Limited PG amount | Optional under 148L, must specify "Balance Reduction" or "Principal Reduction" cap | 148L | Used for partial change-of-ownership sellers retaining <20% |

---

## Can a TIC Co-Owner Be on an SBA Loan? (Q&A)

**Q1: Can multiple TIC owners be co-borrowers on one SBA note?**
**A:** Yes. SBA does not prohibit multiple co-borrowers, and SOP 50 10 7.1 §A Ch. 5 expressly contemplates multi-borrower structures.

**Q2: Or do they need separate notes?**
**A:** Separate notes are not required and would unnecessarily fragment the SBA guarantee. SBA prefers a single note with joint-and-several liability.

**Q3: How is collateral/lien handled when one co-owner is in an LLC and another is an individual TIC?**
**A:** The mortgage must cover **100% of the fee simple title**. The JV LLC mortgages its undivided interest; Janet and Ryan each mortgage their individual TIC undivided interests; collectively the recorded mortgage encumbers the entire property.

**Q4: Can a 1031 TIC investor be a PG without being part of the operating entity?**
**A:** Yes — and likely **must** be a PG if their TIC % gives them ≥20% of the EPC. Under 13 CFR 120.111(a)(4) the 20% trigger looks at ownership in the EPC, the OC, or both — TIC ownership of the real estate is ownership of the EPC.

**Citizenship caveat:** Per the March 2025 SBA Policy Notice (5000-865754) implementing Executive Order 14159, **100% of the EPC's and OC's direct and indirect ownership must be U.S. citizens or U.S. nationals with U.S. principal residence**. LPRs (green-card holders) are not eligible to own any percentage. A 5% de minimis exception exists.

---

## Use of Proceeds, Equity Injection, Affiliation

### Permissible uses (13 CFR 120.120 — 7(a); 13 CFR 120.882 — 504)
- **7(a):** real estate acquisition, building improvements, equipment, working capital, debt refinancing.
- **504:** real estate acquisition, ground-up construction, building renovation, heavy machinery with ≥10-year useful life. **No working capital.** No broker fees (13 CFR 120.884).

### Prohibited uses (13 CFR 120.130 — 7(a))
- Distributions to Associates (except ordinary compensation)
- Refinance debt to an SBIC or NMVCC
- Investments in real/personal property held for sale, lease, or investment (subject to EPC exception)
- Speculative activities

### Sponsor / acquisition fees
SBA generally **disallows** sponsor or promoter fees from loan proceeds. Reasonable third-party professional fees (appraisal, environmental, legal, title) are allowable. Broker/finder fees on the financing itself are prohibited from 504 proceeds (13 CFR 120.884) and disfavored from 7(a) proceeds. Sponsor "promote" fees should be paid from equity, not from SBA proceeds.

### Equity injection
- **7(a):** Lender follows prudent commercial practice — standard 10% on real estate; 15% for special-purpose properties or new businesses.
- **504:** 13 CFR 120.910 — minimum 10%; **15%** if new business or special-purpose property; **20%** if both.

### Affiliation (13 CFR 121.103)
The JV LLC + TIC structure raises affiliation across the EPC owners and the OC. Affiliation matters because **size standards are tested on a combined basis**. A JV is generally treated as an affiliate of all of its members (121.103(h)).

---

## Default and Recourse Implications

- **Blanket lien (7(a)):** On default, lender's foreclosure reaches all OC business assets via UCC-1, plus the real estate first mortgage, plus any personal-RE liens, plus all guarantors' personal assets.
- **Non-blanket lien (504 CDC second / RE-only):** Recovery is limited to real estate value after first-lien payoff plus PG recovery.
- **TIC nuance:** If the mortgage covers the entire fee (signed by all TICs), foreclosure is clean. If the mortgage covers only one TIC's undivided interest, the lender ends up as a TIC with the non-defaulting owners — a difficult and disfavored outcome.

---

## What This Means for the Deal

1. **Entity restructuring is required.** The JV LLC + TIC structure cannot itself be the SBA borrower without (a) qualifying as an EPC and (b) identifying a real OC tenant.

2. **All TIC owners must be on the loan.** Janet Ng and Ryan must each be co-borrowers (or co-mortgagors) so the lender's first mortgage covers the entire fee.

3. **Personal guarantees as listed are likely correct, but verify each PG's look-through %.**

4. **Choose 7(a) unless there is also a third-party first.** A $575K SBA loan against a $1.9M purchase is a clean 7(a) deal.

5. **Confirm citizenship for every owner (direct and indirect).** Post-March 2025, LPRs are excluded entirely.

6. **Document the lease.** A written, subordinated, SBA-compliant lease between the EPC and OC, with assignment of rents, must be executed at or before closing.

7. **Equity injection.** Plan on 10% of project cost as equity (15% if new OC). For a $1.9M purchase, 10% is $190K.

8. **Affiliation review.** Run a 13 CFR 121.103 analysis on every member of Single Seed, on Gideon Spencer's other holdings, and on Janet's and Ryan's other businesses.

---

## Sources (Official Government / Federal)

- [SBA SOP 50 10](https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs)
- [13 CFR Part 120](https://www.ecfr.gov/current/title-13/chapter-I/part-120)
- [13 CFR §120.110 — Ineligible Businesses](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFR6d9c2c4fd6e44c1/section-120.110)
- [13 CFR §120.111 — EPC Conditions](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFR6d9c2c4fd6e44c1/section-120.111)
- [13 CFR §120.120 — Eligible uses](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFRf4e36c83c2b40a5/section-120.120)
- [13 CFR §120.130 — Restrictions on uses](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFRf4e36c83c2b40a5/section-120.130)
- [13 CFR §120.150](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFRa096ec067b9c6cf/section-120.150)
- [13 CFR §120.160 — Loan conditions](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-A/subject-group-ECFRa096ec067b9c6cf/section-120.160)
- [13 CFR Part 120 Subpart H — 504 Program](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-H)
- [13 CFR §120.882](https://www.ecfr.gov/current/title-13/chapter-I/part-120/subpart-H/subject-group-ECFRb53f5f70dbe22e4/section-120.882)
- [13 CFR §120.934](https://www.law.cornell.edu/cfr/text/13/120.934)
- [13 CFR §121.103](https://www.ecfr.gov/current/title-13/chapter-I/part-121/subpart-A/subject-group-ECFRd133f03f6d8398b/section-121.103)
- [SBA Form 148](https://www.sba.gov/document/sba-form-148-unconditional-guarantee)
- [SBA Form 148L](https://www.sba.gov/document/sba-form-148-l-limited-guarantee)
- [SBA SOP 50 57 — 7(a) Servicing & Liquidation](https://www.sba.gov/document/sop-50-57-7a-loan-servicing-liquidation)
- [SBA Policy Notice 5000-865754 — Citizenship (EO 14159)](https://www.sba.gov/document/policy-notice-5000-865754-policy-updates-comply-executive-order-14159-regarding-citizenship-requirements-obtaining-7a-504)
- [SBA — 504 loans](https://www.sba.gov/funding-programs/loans/504-loans)
- [SBA — 7(a) loans](https://www.sba.gov/funding-programs/loans/7a-loans)
