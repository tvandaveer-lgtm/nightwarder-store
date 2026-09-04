# NightWarder store — 2026-09-04

**Status:** live visual rework. Catalog date 2026-09-04.

**Live URL:** https://nightwarder.com/

**Repo:** GitHub Pages on `nightwarder-store` (`index.html` + `assets/`). CNAME remains `nightwarder.com`.

**Checkout:** existing live Stripe Payment Links only. Do not invent, rotate, or recreate buy URLs. Do not change prices.

**Fulfillment / support:** `nightwarder@agentmail.to` only.

**Disclaimer (on page):** blank templates for the department to adopt. Not completed reports, not legal advice, and not an audit. Heat and cold weather SOPs are templates only — not OSHA law.

**Thumbnails:** honest kit-cover art (SVG), labeled as covers — not screenshots of live spreadsheet sheets.

## Asset map (SKU → thumb)

| SKU | Thumb |
|---|---|
| Core bundle (TR+AAR+HEAT) | `assets/thumbs/core-bundle.svg` |
| Treasurer report | `assets/thumbs/treasurer-report.svg` |
| Incident AAR | `assets/thumbs/incident-aar.svg` |
| Heat illness SOP | `assets/thumbs/heat-illness-sop.svg` |
| Training cert tracker | `assets/thumbs/training-cert-tracker.svg` |
| Annual budget builder | `assets/thumbs/annual-budget-builder.svg` |
| Apparatus inspection log | `assets/thumbs/apparatus-inspection-log.svg` |
| PPE / SCBA tracker | `assets/thumbs/ppe-scba-tracker.svg` |
| Donation register | `assets/thumbs/donation-register.svg` |
| Exposure / near-miss log | `assets/thumbs/exposure-near-miss-log.svg` |
| Cold weather SOP | `assets/thumbs/cold-weather-sop.svg` |
| Member meeting packet | `assets/thumbs/member-meeting-packet.svg` |

Also: `assets/mark.svg` (site mark), `assets/store.css`.

## Catalog (12) — buy URLs frozen

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

### Word kits

| Product | Price | Buy |
|---|---|---|
| Exposure / near-miss log | $19 | https://buy.stripe.com/8x2eVe70Yc6Y5eY7Pp1Jm09 |
| Cold weather SOP | $19 | https://buy.stripe.com/cNi7sM8524EwgXGfhR1Jm0b |
| Member meeting packet | $19 | https://buy.stripe.com/3cI3cw0CA9YQ22M9Xx1Jm0a |

## Notes

- Public storefront prefers nightwarder.com. Avoid personal-name leakage in public copy and asset paths.
- Cover generator: `scripts/generate_thumbs.py` (rebuild only; do not change buy links).
