# NightWarder store — 2026-09-05

**Status:** live sample screenshots. Catalog date 2026-09-05. Audience widened beyond volunteer FD to fire / EMS, safety departments, and facility / industrial EM.

**Live URL:** https://nightwarder.com/

**Repo:** GitHub Pages on `nightwarder-store` (`index.html` + `assets/`). CNAME remains `nightwarder.com`.

**Checkout:** existing live Stripe Payment Links only. Do not invent, rotate, or recreate buy URLs. Do not change prices.

**Fulfillment / support:** file by email after payment from `nightwarder@agentmail.to` only. Not an instant download.

**Audience copy:** fire / EMS, safety departments, and facility / industrial EM. Keep the firehouse niche; do not write as if OSHA is the product.

**Disclaimer (on page):** blank templates for the department to adopt. Not completed reports, not legal advice, and not an audit. Heat and cold weather SOPs are templates only — not OSHA law. Permits are blank templates — not completed authorizations, not AHJ approval, and not OSHA law. PTW card: blank work-authorization cover template; not OSHA law; not a completed authorization; not AHJ approval; does not replace hot work / CSE permits. LOTO card: blank authorization + isolation checklist + device log; not OSHA law; not a completed lockout; not a written energy-control program.

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

Also: lantern brand mark (`assets/logo.png` header 256, `assets/logo-512.png`, `assets/favicon-32.png`, `assets/favicon-16.png`, `assets/apple-touch-icon.png`, root `favicon.ico`). Legacy `assets/mark.svg` unused. `assets/store.css`. Sample pages: `scripts/sample-pages/`. Rebuild: `scripts/generate_samples.py`. SEO guide pages: `seo/`.

Hot work card copy is finished buyer language (“for your department”). Do not leave `[Department]` tokens on live buy cards. Kit gold fields may still use fillable department blanks.

## Catalog (16) — buy URLs frozen

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

### Safety aisle (Safety Pack A + LOTO)

| Product | Price | Buy |
|---|---|---|
| Hot work permit | $19 | https://buy.stripe.com/eVq3cwbhe8UMfTC7Pp1Jm0c |
| Confined space entry permit | $24 | https://buy.stripe.com/aFadRadpmc6Y6j2d9J1Jm0d |
| Permit-to-work | $19 | https://buy.stripe.com/dRm5kE3OM5IAgXGfhR1Jm0e |
| SKU-NW-LOTO-01 Lockout-Tagout pack | $19 | https://buy.stripe.com/dRmfZietq3AsfTC7Pp1Jm0f |

## Guides (P0 SEO long-tail · REV1)

River BRIEF REV1 §5. Shared disclaimer on each: Blank template for your department to adopt and fill. Not legal advice. Not a completed report or authorization. Not OSHA law. Not AHJ approval. Not an audit. No new Stripe Payment Links.

| Page | Path | CTA |
|---|---|---|
| Guides index | `seo/index.html` | Catalog `#catalog` |
| Life-safety rope log | `seo/volunteer-fd-life-safety-rope-inspection-log.html` | Catalog `#ops` / `#catalog` (ROPE buy not live) |
| Turnout advanced cleaning log | `seo/turnout-gear-advanced-cleaning-log.html` | Catalog `#ops` + live PPE buy URL |
| SCBA cylinder due dates | `seo/scba-cylinder-hydro-due-date-spreadsheet.html` | Catalog `#ops` + live PPE buy URL |
| PPE / SCBA tracker | `seo/volunteer-fd-ppe-scba-tracker.html` | Live PPE buy URL + catalog `#ppe-scba` / `#ops` |
| Confined space entry | `seo/volunteer-fd-confined-space-entry-permit.html` | Live CSE buy URL + catalog `#confined-space` / `#permits` |

Live buy URLs (already on `index.html`): PPE `https://buy.stripe.com/3cI4gAcli2wobDmc5F1Jm07` · CSE `https://buy.stripe.com/aFadRadpmc6Y6j2d9J1Jm0d`.

Catalog card ids: `#ppe-scba`, `#confined-space`, `#hot-work`, `#permit-to-work`.

## Notes

- Public storefront prefers nightwarder.com. Avoid personal-name leakage in public copy and asset paths.
- Samples are sterile EXAMPLE / Station 99 / 2099 demo screenshots of the live kits.
- Audience copy (title, meta, eyebrow, footer) covers fire / EMS, safety departments, and facility / industrial EM — not volunteer FD only.
- Catalog date 2026-09-05. Count is 16.
- LOTO Buy is live: https://buy.stripe.com/dRmfZietq3AsfTC7Pp1Jm0f. Do not rotate or recreate it.
