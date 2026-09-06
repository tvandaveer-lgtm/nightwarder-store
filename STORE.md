# NightWarder store — 2026-09-06

**Status:** live sample screenshots. Catalog date 2026-09-06. Count is 29. Voice: volunteer / small-department fire / EMS first.

**Live URL:** https://nightwarder.com/

**Repo:** GitHub Pages on `nightwarder-store` (`index.html` + `assets/`). CNAME remains `nightwarder.com`.

**Storefront aisles:** Gear (`#gear`) · Permits (`#permits`) · Ops (`#ops`) · Admin (`#admin`). Nav / footer: Gear · Permits · Ops · Admin · Support · X (`https://x.com/NightWarder`). No “Word kits” aisle. No Core category pack.

**Category map (cards only — not Stripe packs):**

| Aisle | Anchor | SKUs |
|---|---|---|
| Gear & Inspection | `#gear` | ROPE, TURN, CYL, LADDER, EXT, GEN, APP (apparatus), PPE |
| Permits / Energy | `#permits` | PTW, HWP, CSE, LOTO (Safety Pack A stays with permits; LOTO with permits) |
| Ops Readiness | `#ops` | HEAT, COLD, EXP, AAR, TRAIN, ELEV, WATER, RESP, DRILL |
| Admin / Treasurer | `#admin` | TR, BUD, DON, MTG, APP (SKU-NW-APP-01 membership), REIMB, LEDGER |

BUNDLE-01 (TR+AAR+HEAT, $49) is a leftover mix listed last under Admin. It is not a category pack. Do not expand it. Do not wrap permits into it. Hero does not sell a Core / category pack.

**Checkout:** existing live Stripe Payment Links only. Do not invent, rotate, or recreate buy URLs. Do not change prices.

**Fulfillment / support:** File by email after Stripe checkout from `nightwarder@agentmail.to` only. Not an instant download. Published refund line: Digital delivery · contact nightwarder@ within 7 days of purchase for refund requests.

**Audience copy:** volunteer and small-department fire / EMS first. Keep the firehouse niche. Do not write facility EM / house-or-site drift. Do not write as if OSHA is the product.

**Disclaimer (on page):** blank templates for the department to adopt. Not completed reports, not legal advice, and not an audit. Heat and cold weather SOPs are templates only — not OSHA law. Permits are blank templates — not completed authorizations, not AHJ approval, and not OSHA law. PTW card: blank work-authorization cover template; not OSHA law; not a completed authorization; not AHJ approval; does not replace hot work / CSE permits. LOTO card: blank authorization + isolation checklist + device log; not OSHA law; not a completed lockout; not a written energy-control program. RESP card: checklist only — not a full respiratory program, not a medical evaluation, not a fit-test certificate, and not OSHA 1910.134 compliance. ELEV: not OSHA certification / not a completed permit. WATER: not USCG certification / not a completed rescue report. DRILL: not HSEEP certification / not a completed graded exercise filing.

**Thumbnails:** EXAMPLE / Station 99 demo screenshots of the live kits (fake 2099 figures). Not abstract kit-cover art. Catalog cards use the PNG samples; click opens a lightbox.

## Asset map (SKU → screenshot)

| SKU | Screenshot |
|---|---|
| Core bundle (TR+AAR+HEAT) | `assets/thumbs/core-bundle.png` |
| Treasurer report | `assets/thumbs/treasurer-report.png` |
| Incident AAR | `assets/thumbs/incident-aar.png` |
| Heat illness SOP | `assets/thumbs/heat-illness-sop.png` |
| Training cert tracker | `assets/thumbs/training-cert-tracker.png` |
| Annual budget builder | `assets/thumbs/annual-budget-builder.png` |
| Apparatus inspection log | `assets/thumbs/apparatus-inspection-log.png` |
| PPE / SCBA tracker | `assets/thumbs/ppe-scba-tracker.png` |
| Donation register | `assets/thumbs/donation-register.png` |
| Exposure / near-miss log | `assets/thumbs/exposure-near-miss-log.png` |
| Cold weather SOP | `assets/thumbs/cold-weather-sop.png` |
| Member meeting packet | `assets/thumbs/member-meeting-packet.png` |
| Hot work permit | `assets/thumbs/hot-work-permit.png` |
| Confined space entry permit | `assets/thumbs/confined-space-entry-permit.png` |
| Permit-to-work | `assets/thumbs/permit-to-work.png` |
| SKU-NW-LOTO-01 Lockout-Tagout pack | `assets/thumbs/lockout-tagout-pack.png` |
| SKU-NW-ROPE-01 Life-safety rope log | Text card (no Station 99 sample PNG yet) |
| SKU-NW-TURN-01 Turnout advanced inspect + clean log | Text card (no Station 99 sample PNG yet) |
| SKU-NW-CYL-01 SCBA cylinder due calendar | Text card (no Station 99 sample PNG yet) |
| SKU-NW-LADDER-01 Ladder inspection log (ground + aerial) | Text card (no Station 99 sample PNG yet) |
| SKU-NW-EXT-01 Extinguisher inspection log | Text card (no Station 99 sample PNG yet) |
| SKU-NW-GEN-01 Generator / fuel / station utilities log | Text card (no Station 99 sample PNG yet) |
| SKU-NW-APP-01 Volunteer membership application | `assets/thumbs/volunteer-membership-application.png` |
| SKU-NW-REIMB-01 Expense reimbursement request | `assets/thumbs/expense-reimbursement-request.png` |
| SKU-NW-LEDGER-01 Simple cash / petty ledger | `assets/thumbs/simple-cash-petty-ledger.png` |
| SKU-NW-ELEV-01 Elevated work / fall protection checklist | `assets/thumbs/elevated-work-fall-protection-checklist.png` |
| SKU-NW-WATER-01 Working over water checklist | `assets/thumbs/working-over-water-checklist.png` |
| SKU-NW-RESP-01 Respiratory protection checklist | `assets/thumbs/respiratory-protection-checklist.png` |
| SKU-NW-DRILL-01 EM drill / exercise assessment | `assets/thumbs/em-drill-exercise-assessment.png` |

Also: lantern brand mark (`assets/logo.png` header 256, `assets/logo-512.png`, `assets/favicon-32.png`, `assets/favicon-16.png`, `assets/apple-touch-icon.png`, root `favicon.ico`). Legacy `assets/mark.svg` unused. `assets/store.css`. Sample pages: `scripts/sample-pages/`. Rebuild: `scripts/generate_samples.py`. SEO guide pages: `seo/`.

Hot work card copy is finished buyer language (“for your department”). Do not leave `[Department]` tokens on live buy cards. Kit gold fields may still use fillable department blanks.

## Catalog (29) — buy URLs frozen

Checkout table below is frozen (same products, prices, and `buy.stripe.com` URLs). Headings in this table are the old checkout groups, not storefront aisles. Storefront aisles are Gear / Permits / Ops / Admin above.

### Core

| Product | Price | Buy |
|---|---|---|
| Core bundle (TR+AAR+HEAT) | $49 | https://buy.stripe.com/fZubJ270Y3Asazi3z91Jm02 |
| Treasurer report | $29 | https://buy.stripe.com/9B614ofxu0ogfTCfhR1Jm00 |
| Incident AAR | $19 | https://buy.stripe.com/28E9AUada9YQ5eY9Xx1Jm01 |
| Heat illness SOP | $19 | https://buy.stripe.com/fZudRa5WU5IA36Q2v51Jm03 |

### Ops trackers

| Product | Price | Buy |
|---|---|---|
| Training cert tracker | $29 | https://buy.stripe.com/00w14o2KI2wo4aU8Tt1Jm04 |
| Annual budget builder | $24 | https://buy.stripe.com/28EdRaetqdb2ePyb1B1Jm05 |
| Apparatus inspection log | $19 | https://buy.stripe.com/9B6cN61GE4Ew0YI8Tt1Jm06 |
| PPE / SCBA tracker | $19 | https://buy.stripe.com/3cI4gAcli2wobDmc5F1Jm07 |
| Donation register | $19 | https://buy.stripe.com/cNi8wQfxu6ME22MedN1Jm08 |
| SKU-NW-ROPE-01 Life-safety rope log | $19 | https://buy.stripe.com/5kQcN6852gneazi2v51Jm0g |
| SKU-NW-TURN-01 Turnout advanced inspect + clean log | $19 | https://buy.stripe.com/aFa8wQ8521sk7n6glV1Jm0i |
| SKU-NW-CYL-01 SCBA cylinder due calendar | $19 | https://buy.stripe.com/cNi3cw2KI0ogfTCfhR1Jm0h |
| SKU-NW-LADDER-01 Ladder inspection log (ground + aerial) | $19 | https://buy.stripe.com/7sYcN670Y0ogfTCedN1Jm0j |
| SKU-NW-EXT-01 Extinguisher inspection log | $19 | https://buy.stripe.com/fZu3cwgBydb28ra0mX1Jm0k |
| SKU-NW-GEN-01 Generator / fuel / station utilities log | $19 | https://buy.stripe.com/5kQbJ2cli7QI36Q0mX1Jm0l |

### Word kits

| Product | Price | Buy |
|---|---|---|
| Exposure / near-miss log | $19 | https://buy.stripe.com/8x2eVe70Yc6Y5eY7Pp1Jm09 |
| Cold weather SOP | $19 | https://buy.stripe.com/cNi7sM8524EwgXGfhR1Jm0b |
| Member meeting packet | $19 | https://buy.stripe.com/3cI3cw0CA9YQ22M9Xx1Jm0a |

### Safety aisle (Safety Pack A + LOTO)

| Product | Price | Buy |
|---|---|---|
| Hot work permit | $19 | https://buy.stripe.com/eVq3cwbhe8UMfTC7Pp1Jm0c |
| Confined space entry permit | $24 | https://buy.stripe.com/aFadRadpmc6Y6j2d9J1Jm0d |
| Permit-to-work | $19 | https://buy.stripe.com/dRm5kE3OM5IAgXGfhR1Jm0e |
| SKU-NW-LOTO-01 Lockout-Tagout pack | $19 | https://buy.stripe.com/dRmfZietq3AsfTC7Pp1Jm0f |

### End-cap seven (Admin + Ops)

SKU-NW-APP-01 is the volunteer membership application (Admin). Do not confuse it with Gear APP (apparatus inspection log).

| Product | Price | Buy |
|---|---|---|
| SKU-NW-APP-01 Volunteer Membership Application | $7 | https://buy.stripe.com/9B65kE4SQc6YgXG9Xx1Jm0m |
| SKU-NW-REIMB-01 Expense Reimbursement Request | $7 | https://buy.stripe.com/fZucN6etqef622M9Xx1Jm0n |
| SKU-NW-LEDGER-01 Simple Cash / Petty Ledger | $7 | https://buy.stripe.com/00wdRa70Yb2U22M1r11Jm0o |
| SKU-NW-ELEV-01 Elevated Work / Fall Protection Checklist | $15 | https://buy.stripe.com/aFa28scli1skgXGfhR1Jm0p |
| SKU-NW-WATER-01 Working Over Water Checklist | $15 | https://buy.stripe.com/6oU5kE0CA0og7n67Pp1Jm0q |
| SKU-NW-RESP-01 Respiratory Protection Checklist (checklist only) | $15 | https://buy.stripe.com/14A3cwadac6Y7n6c5F1Jm0r |
| SKU-NW-DRILL-01 EM Drill / Exercise Assessment | $19 | https://buy.stripe.com/dRm4gAada4Ew4aUglV1Jm0s |

## Guides (`/seo/` aisle map)

Aisle map matches the store: Gear / Permits / Ops / Admin. Shared disclaimer on each page: Blank template for [Department] to adopt and fill. Not legal advice. Not a completed report or authorization. Not OSHA law. Not AHJ approval. Not an audit. No new Stripe Payment Links. No Gumroad. ROPE / TURN / CYL / LADDER / EXT / GEN / APP (membership) / REIMB / LEDGER / ELEV / WATER / RESP / DRILL Buy CTAs use the frozen catalog links below. LADDER and EXT are aisle cards only — no dedicated guide HTML yet (HANDOFF: add guide Buy links only when those pages exist). GEN guide is live; fences stay on the card (not NFPA 110 certification; not a completed EPSS; not an apparatus inspection; cadence / load-test years = buyer/AHJ INPUT). RESP guide and card stay checklist-only (not a full respiratory program; not a medical evaluation; not a fit-test certificate; not OSHA 1910.134 compliance). ELEV: not OSHA certification / not a completed permit. WATER: not USCG certification / not a completed rescue report. DRILL: not HSEEP certification / not a completed graded exercise filing. Gear APP remains the apparatus inspection log — SKU-NW-APP-01 membership application lives under Admin.

| Aisle | Page | Path | CTA |
|---|---|---|---|
| Index | Guides aisle map | `seo/index.html` | Catalog `#catalog` |
| Admin | Treasurer report | `seo/volunteer-fd-monthly-treasurer-report.html` | Live TR buy + `#admin` |
| Ops | Incident AAR | `seo/volunteer-fd-incident-aar.html` | Live AAR buy + `#ops` |
| Ops | Heat illness SOP | `seo/firefighter-heat-illness-sop-blank.html` | Live HEAT buy + `#ops` |
| Ops | Training cert tracker | `seo/volunteer-fd-training-cert-tracker.html` | Live TRAIN buy + `#ops` |
| Admin | Annual budget builder | `seo/volunteer-fd-annual-budget-spreadsheet.html` | Live BUD buy + `#admin` |
| Gear | Apparatus inspection log | `seo/volunteer-fd-apparatus-inspection-log.html` | Live APP buy + `#gear` |
| Gear | PPE / SCBA tracker | `seo/volunteer-fd-ppe-scba-tracker.html` | Live PPE buy + `#ppe-scba` / `#gear` |
| Admin | Donation register | `seo/volunteer-fd-donation-register.html` | Live DON buy + `#admin` |
| Gear | Life-safety rope log | `seo/volunteer-fd-life-safety-rope-inspection-log.html` | Live ROPE buy + `#rope` / `#gear` |
| Gear | Turnout advanced cleaning log | `seo/turnout-gear-advanced-cleaning-log.html` | Live TURN buy + `#turnout` / `#gear` |
| Gear | SCBA cylinder due dates | `seo/scba-cylinder-hydro-due-date-spreadsheet.html` | Live CYL buy + `#scba-cyl` / `#gear` |
| Gear | Ladder inspection log | aisle card on `seo/index.html` only (no guide HTML yet) | Live LADDER buy + `#ladder` / `#gear` |
| Gear | Extinguisher inspection log | aisle card on `seo/index.html` only (no guide HTML yet) | Live EXT buy + `#extinguisher` / `#gear` |
| Gear | Station generator / fuel log | `seo/volunteer-fire-station-generator-fuel-log.html` | Live GEN buy + `#generator` / `#gear` |
| Ops | Exposure / near-miss log | `seo/firefighter-exposure-near-miss-log.html` | Live EXP buy + `#ops` |
| Ops | Cold weather SOP | `seo/firefighter-cold-weather-sop-blank.html` | Live COLD buy + `#ops` |
| Admin | Member meeting packet | `seo/volunteer-fd-meeting-agenda-minutes.html` | Live MTG buy + `#admin` |
| Admin | Volunteer membership application | `seo/volunteer-fd-membership-application.html` | Live APP (membership) buy + `#membership-app` / `#admin` |
| Admin | Expense reimbursement request | `seo/volunteer-fd-expense-reimbursement-request.html` | Live REIMB buy + `#reimbursement` / `#admin` |
| Admin | Simple cash / petty ledger | `seo/volunteer-fd-simple-cash-petty-ledger.html` | Live LEDGER buy + `#petty-ledger` / `#admin` |
| Ops | Elevated work / fall protection checklist | `seo/volunteer-fd-elevated-work-fall-protection-checklist.html` | Live ELEV buy + `#elevated-work` / `#ops` |
| Ops | Working over water checklist | `seo/volunteer-fd-working-over-water-checklist.html` | Live WATER buy + `#working-over-water` / `#ops` |
| Ops | Respiratory protection checklist | `seo/volunteer-fd-respiratory-protection-checklist.html` | Live RESP buy + `#respiratory` / `#ops` |
| Ops | EM drill / exercise assessment | `seo/volunteer-fd-em-drill-exercise-assessment.html` | Live DRILL buy + `#em-drill` / `#ops` |
| Permits | Hot work permit | `seo/volunteer-fd-hot-work-permit.html` | Live HWP buy + `#hot-work` / `#permits` |
| Permits | Confined space entry | `seo/volunteer-fd-confined-space-entry-permit.html` | Live CSE buy + `#confined-space` / `#permits` |
| Permits | Permit to work | `seo/volunteer-fd-permit-to-work.html` | Live PTW buy + `#permit-to-work` / `#permits` |
| Permits | Lockout-Tagout pack | `seo/volunteer-fd-loto-lockout-tagout.html` | Live LOTO buy + `#loto` / `#permits` |

Live buy URLs stay the frozen catalog links in the table above this section. Do not rotate or recreate them.

Catalog card ids: `#ppe-scba`, `#rope`, `#turnout`, `#scba-cyl`, `#ladder`, `#extinguisher`, `#generator`, `#confined-space`, `#hot-work`, `#permit-to-work`, `#loto`, `#membership-app`, `#reimbursement`, `#petty-ledger`, `#elevated-work`, `#working-over-water`, `#respiratory`, `#em-drill`, `#bundle` (legacy TR+AAR+HEAT mix).

## Notes

- Public storefront prefers nightwarder.com. Avoid personal-name leakage in public copy and asset paths.
- Samples are sterile EXAMPLE / Station 99 / 2099 demo screenshots of the live kits.
- Audience copy (title, meta, eyebrow, footer) leads with volunteer and small-department fire / EMS. Do not write facility EM / house-or-site drift.
- Catalog date 2026-09-06. Count is 29. End-cap seven is v2026-09-06. GEN-01 remains v2026-09-05a.
- LOTO Buy is live: https://buy.stripe.com/dRmfZietq3AsfTC7Pp1Jm0f. Do not rotate or recreate it.
- ROPE Buy is live: https://buy.stripe.com/5kQcN6852gneazi2v51Jm0g. Do not rotate or recreate it.
- TURN Buy is live: https://buy.stripe.com/aFa8wQ8521sk7n6glV1Jm0i. Do not rotate or recreate it.
- CYL Buy is live: https://buy.stripe.com/cNi3cw2KI0ogfTCfhR1Jm0h. Do not rotate or recreate it.
- LADDER Buy is live: https://buy.stripe.com/7sYcN670Y0ogfTCedN1Jm0j. Do not rotate or recreate it.
- EXT Buy is live: https://buy.stripe.com/fZu3cwgBydb28ra0mX1Jm0k. Do not rotate or recreate it.
- GEN Buy is live: https://buy.stripe.com/5kQbJ2cli7QI36Q0mX1Jm0l. Do not rotate or recreate it.
- APP (membership) Buy is live: https://buy.stripe.com/9B65kE4SQc6YgXG9Xx1Jm0m. Do not rotate or recreate it.
- REIMB Buy is live: https://buy.stripe.com/fZucN6etqef622M9Xx1Jm0n. Do not rotate or recreate it.
- LEDGER Buy is live: https://buy.stripe.com/00wdRa70Yb2U22M1r11Jm0o. Do not rotate or recreate it.
- ELEV Buy is live: https://buy.stripe.com/aFa28scli1skgXGfhR1Jm0p. Do not rotate or recreate it.
- WATER Buy is live: https://buy.stripe.com/6oU5kE0CA0og7n67Pp1Jm0q. Do not rotate or recreate it.
- RESP Buy is live: https://buy.stripe.com/14A3cwadac6Y7n6c5F1Jm0r. Do not rotate or recreate it. RESP remains checklist only.
- DRILL Buy is live: https://buy.stripe.com/dRm4gAada4Ew4aUglV1Jm0s. Do not rotate or recreate it.
