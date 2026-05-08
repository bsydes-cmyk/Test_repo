# Review: JV vs. Reg D Security Research Memo

**Verdict: YELLOW** (substantively sound, with one material legal error, several overstatements, and notable gaps for a hospitality deal)

---

## Verified accurate

- Howey verbatim quote (matches *SEC v. W.J. Howey Co.*, 328 U.S. 293, 298–99)
- Williamson three-factor test verbatim
- Robinson v. Glynn — Fourth Circuit, NOT a security; Treasurer; Board of Managers seat; veto over indebtedness; "antithetical to the notion of member passivity" attributed correctly
- SEC v. Merchant Capital — RLLP held to be securities; "expectations of control at the time the interest is sold" formulation real
- Long v. Shultz Cattle Co. — correctly cited; consulting agreement / fee evidence
- SEC v. Shields, Arcturus Corp. — correctly cited
- Hocking v. Dubois — citation correct
- Rule 506(b)/506(c) — 35-non-accredited cap, no general solicitation under (b), accredited verification under (c)
- Form D 15-day rule (Rule 503)
- NSMIA / §18 preemption (Rule 506 = covered securities)
- Math: $97K/$1.9M = 5.10%; $97K/$650K = 14.92% — verified accurate
- Horizontal vs. vertical commonality framing — accurate at high level

---

## Errors found

### 1. **MATERIAL LEGAL ERROR — §15(a) is NOT Howey-independent** (HIGH PRIORITY)
- Memo claim: "the intermediary may need to be a registered broker-dealer under Securities Exchange Act § 15(a). … This risk is independent of the Howey analysis."
- Actual law: §15(a) only prohibits unregistered persons from effecting transactions in **any security**. A "broker" is defined at 15 U.S.C. § 78c(a)(4)(A) as one who effects transactions in **securities** for the account of others. **If the JV interest is not a security, there is no "security" being sold, and §15(a) is not triggered.**
- The broker-dealer registration risk is therefore **derivative of**, not "independent of," the Howey/Williamson analysis. The user's instinct on this is correct.
- Practical caveat: transaction-based compensation tied to capital-raising IS a classic Howey-Williamson red flag (it implies the recipient is selling something to passive investors). So eliminating/restructuring the 15% bucket is still wise — but the rationale is "this fact pattern tends to flip the JV into a security, and *if it is a security* then §15(a) bites," not "§15(a) bites independently."

### 2. SMALL QUOTE INACCURACY — Robinson v. Glynn
- The "antithetical to the notion of member passivity" phrase is real, but the memo's surrounding "required to find an investment contract" clause is the memo's gloss, not the court's words. Convert entire sentence to paraphrase.

### 3. CITATION GAP — *Long v. Shultz Cattle*
- *Long* is not a "fee = security" case; it is a "rubber-stamp delegation" case in which fees were corroborative. Memo gloss is slightly overstated.

### 4. POTENTIAL CITATION DRIFT — *Great Lakes Chem. Corp. v. Monsanto*
- Cited at §4 with no parenthetical. Concerns sale of 100% LLC interest as sale of business, not JV-formation analysis. Tangentially relevant. Drop or add limiting parenthetical.

---

## Overstatements / hedges

1. **Exec Summary "presumptively NOT a security … is followed nationwide"** — followed by **most circuits**, but Tenth (Shields), Ninth (Arcturus-style), Eleventh (Merchant Capital) apply with skepticism. Some state courts have rejected/weakened the Williamson presumption.
2. **"Solely... softened to 'predominantly'"** — widespread but not universal. Supreme Court has never adopted the softened test; it remains a circuit-level gloss originating in *Glenn W. Turner*.
3. **§3 Factor 3 — "if there is one person with non-replaceable expertise, the others 'depend solely on his efforts' and the interest is a security"** — overstated. *Williamson* says satisfying any factor "**can**" make it a security; courts apply totality-of-circumstances Howey.
4. **§5 — Section 4(a)(2)** — note *Ralston Purina*-derived sophistication/access standard; 4(a)(2) is statutory exemption with no safe harbor (Rule 506 is the safe harbor).
5. **"$97K (~5.1%) is at the high end of market for syndication"** — math right but market-color claim. Most syndication acquisition fees run 1–3% of purchase price; 5.1% is **well above market**. Soften or supply market-data citation.
6. **"Most states track federal Howey/Williamson"** — true broadly, but Hawaii, California, Massachusetts apply a **risk-capital test** broader than Howey. Particularly relevant since Hawaii is the leading hospitality-rental jurisdiction (*Hocking*).

---

## Gaps that matter (prioritized)

### 1. (HIGH) Hocking v. Dubois hospitality-rental-pool risk is NAMED but NOT ANALYZED
The memo lists *Hocking* in §8 and SOURCES but never explains it. **Given the user's deal is a hospitality acquisition, this is the single most directly applicable case.** *Hocking* held that condo + voluntary rental-pool option could be a security where the rental-pool program was bundled with the real estate sale. **If the hospitality JV will pool revenue from rooms or operate any units as a managed rental program, *Hocking* and progeny (*Salameh*, *Wals v. Fox Hills*) are directly on point.**

### 2. (HIGH) 1031-TIC sidecar
The memo doesn't address the possibility that part of the equity may come in via a TIC. **A TIC offered as part of a packaged investment with bundled management is itself a security** (SEC has issued multiple no-action and enforcement positions). Cross-reference to TIC research is glaring gap.

### 3. (HIGH) The "15% bucket" structural fix
Memo says "restructure or eliminate" but doesn't explain how. Practical alternatives:
- Treat the 15% as a sweat-equity allocation for acquisition and underwriting work performed before closing (documented hours and deliverables)
- Limit the 15% recipients to people who themselves are taking active roles
- Avoid characterizing it as "raised capital" compensation in any document

### 4. (MEDIUM) State Blue Sky exemptions for non-securities
Practical reality: if JV is genuinely not a security under federal law, most state regulators follow federal characterization. Counter: a few states (HI, CA, MA risk-capital states) could disagree.

### 5. (MEDIUM) Circuit-split awareness
Fifth Circuit (Williamson, Arcturus, Long) and Eleventh (Merchant Capital) use **broad vertical commonality** — more SEC-friendly. Third, Sixth, Seventh require horizontal. Ninth and Tenth in between. User's domicile and deal situs determine which framework.

### 6. (MEDIUM) Integration doctrine
Reg D Rule 152 (post-2021) governs integration of multiple offerings. Worth one sentence given JV-vs-Reg-D fall-back posture.

### 7. (MEDIUM) Bad-actor disqualification (Rule 506(d))
Mentioned in table but not explained. Even fall-back to 506(b) requires bad-actor diligence on every member with 20%+ equity, every officer, every promoter.

---

## Specific edits

1. **§8 ¶6 / §11 broker-dealer paragraph**: Rewrite to make §15(a) risk derivative of security characterization. Suggested:
   > "**Broker-Dealer Registration**: §15(a) applies only when the instrument being sold *is* a security. If the JV interest is correctly characterized as a non-security, no §15(a) issue arises. However, the *facts* that would trigger broker-dealer registration concerns — transaction-based compensation paid to a person soliciting passive capital — are themselves the strongest Howey/Williamson red flags pointing toward security characterization. Eliminating or restructuring the 15% capital-raise slice solves both problems at once."
2. **§4 Robinson quote**: Rewrite as paraphrase
3. **NEW §4A "Hospitality-Specific Risk: Hocking and Rental-Pool Doctrine"**: 1–2 paragraphs analyzing *Hocking* and explaining when bundled hospitality management converts a real-estate interest into a security. **Single most important addition.**
4. **NEW §11A "1031-TIC Sidecar Analysis"**: cross-reference to TIC memo; note SEC's longstanding position
5. **§2 prong 4**: Replace "softened to 'predominantly'" with more precise: "Most circuits, following *Glenn W. Turner*, ask whether 'the efforts made by those other than the investor are the undeniably significant ones, those essential managerial efforts which affect the failure or success of the enterprise.' Supreme Court has not formally endorsed the softened standard."
6. **§7 Checklist**: Add row "**No bundled rental-pool, hospitality-management, or revenue-sharing program offered with the JV interest** — Avoids *Hocking*-style conversion"
7. **§9**: Add market-data context (1–3% typical syndication norm; 5.1% meaningfully above market)
8. **§4 "Other relevant authority"**: Drop *Great Lakes Chem.* or limit
9. **CLOSING RECOMMENDATION**: Add fourth bullet — "Confirm there is no bundled hospitality-management or rental-pool program offered alongside the JV interest. If there is, treat the offering as presumptively a security and run the Reg D track."

---

## Bottom line for synthesis (5 bullets)

1. **The doctrinal core of the memo is sound.** Howey, Williamson, Robinson, Merchant Capital, Long, Shields, Arcturus, Reg D / Form D / NSMIA all accurately stated.
2. **One material legal error must be corrected**: Exchange Act §15(a) broker-dealer registration is **NOT Howey-independent**. It applies only if the underlying JV interest is itself a security. The 15% bucket is still risky, but as a Howey/Williamson red flag, not as a separate §15(a) trigger.
3. **The single biggest substantive gap is hospitality-specific: *Hocking v. Dubois* and the rental-pool doctrine.** If the deal contemplates any pooled revenue or bundled rental-management program, security characterization risk increases sharply.
4. **The 1031-TIC interaction is unaddressed.** TIC interests offered with packaged management are typically securities under SEC's longstanding position.
5. **Practical recommendations remain valid**: kill or restructure the 15% capital-raise slice; convert the 5.1% acquisition fee into capital-account credit; document active member participation through meetings/votes/minutes/time logs; structure offering to also satisfy Rule 506(b) as belt-and-suspenders.
