#!/usr/bin/env python3
"""Render NightWarder EXAMPLE / Station 99 catalog samples (not kit-cover art).

These pages recreate the live-kit UI the buyer sees: gold inputs, navy headers,
and sterile 2099 demo figures. Output: assets/thumbs/<sku>.png
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "thumbs"
WORK = ROOT / "scripts" / "sample-pages"
SHOT = Path("/tmp/nw-sample-shots")

NAVY = "#1b365d"
NAVY2 = "#16304f"
GOLD = "#f3e2a6"
GREEN = "#d7ead4"
LABEL = "#d7e0ea"
PEACH = "#f7ece0"
INK = "#1a2330"
MUTED = "#5c6774"
RED = "#b42318"
BANNER = "#c62828"

SHEET_CSS = f"""
  :root {{ --navy:{NAVY}; --navy2:{NAVY2}; --gold:{GOLD}; --green:{GREEN};
           --label:{LABEL}; --peach:{PEACH}; --ink:{INK}; --muted:{MUTED}; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; color:var(--ink);
    font-family: "IBM Plex Sans", "Liberation Sans", Arial, sans-serif; }}
  body {{ width:1600px; min-height:1000px; padding:22px 28px 28px; }}
  .banner {{ background:{BANNER}; color:#fff; font-weight:700; font-size:15px;
    letter-spacing:.04em; padding:8px 14px; margin:0 0 12px; }}
  .badge {{ position:absolute; top:18px; right:28px; background:#111; color:#fff;
    border-radius:999px; padding:7px 14px; font-size:13px; font-weight:700;
    letter-spacing:.04em; }}
  .badge em {{ color:#f0c14b; font-style:normal; }}
  .wrap {{ position:relative; }}
  h1 {{ margin:4px 0 4px; font-size:26px; color:var(--navy); }}
  .sub {{ color:var(--muted); font-size:14px; font-style:italic; margin:0 0 12px; }}
  table {{ border-collapse:collapse; width:100%; font-size:15px; margin:0 0 14px; }}
  th {{ background:var(--navy); color:#fff; font-weight:650; text-align:left;
    padding:7px 9px; border:1px solid var(--navy2); }}
  td {{ border:1px solid #c5cdd6; padding:6px 9px; }}
  td.l {{ background:var(--label); font-weight:600; width:22%; }}
  td.g {{ background:var(--gold); }}
  td.f {{ background:var(--green); font-variant-numeric:tabular-nums; }}
  td.p {{ background:var(--peach); }}
  tr.alt td {{ background:#fbf6f0; }}
  .sec {{ background:var(--navy); color:#fff; font-size:14px; font-weight:700;
    letter-spacing:.06em; text-transform:uppercase; padding:7px 10px; margin:10px 0 0; }}
  .note {{ font-size:13px; color:var(--muted); font-style:italic; margin:2px 0 8px; }}
  .foot {{ font-size:12px; color:#8a93a0; margin-top:8px; }}
  .money {{ text-align:right; font-variant-numeric:tabular-nums; }}
"""

DOC_CSS = f"""
  :root {{ --navy:{NAVY}; --gold:{GOLD}; --label:{LABEL}; --ink:{INK}; --muted:{MUTED}; }}
  * {{ box-sizing: border-box; }}
  html, body {{ margin:0; padding:0; background:#fff; color:var(--ink);
    font-family: "Liberation Serif", "Times New Roman", Georgia, serif; }}
  body {{ width:1200px; min-height:1550px; padding:22px 28px 28px; }}
  .meta {{ font-family:"IBM Plex Sans", Arial, sans-serif; font-size:12px; color:#8a93a0; }}
  .badge {{ position:absolute; top:18px; right:28px; background:#16304f; color:#fff;
    border-radius:10px; padding:8px 14px; font-size:13px; font-weight:700;
    font-family:"IBM Plex Sans", Arial, sans-serif; }}
  .badge em {{ color:#f0c14b; font-style:normal; }}
  .wrap {{ position:relative; }}
  h1 {{ margin:10px 0 4px; font-size:30px; color:var(--navy); }}
  .bar {{ background:var(--navy); color:#fff; font-size:20px; font-weight:700;
    padding:10px 14px; margin:8px 0 8px; letter-spacing:.02em; }}
  .sub {{ font-style:italic; color:var(--muted); font-size:15px; margin:0 0 12px; }}
  table {{ border-collapse:collapse; width:100%; font-size:15px; margin:0 0 12px;
    font-family:"IBM Plex Sans", Arial, sans-serif; }}
  th {{ background:var(--navy); color:#fff; font-weight:650; text-align:left;
    padding:7px 8px; }}
  td {{ border:1px solid #b7c0cb; padding:7px 8px; }}
  td.l {{ background:var(--label); font-weight:600; width:24%; }}
  td.g {{ background:var(--gold); min-height:28px; }}
  .checks {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px;
    background:var(--gold); padding:12px; border:1px solid #d4c48a;
    font-family:"IBM Plex Sans", Arial, sans-serif; font-size:15px; }}
  .checks span {{ display:flex; align-items:center; gap:8px; }}
  .box {{ width:16px; height:16px; border:1.5px solid #1b365d; background:#fff; }}
  .foot {{ font-size:12px; color:#8a93a0; font-style:italic; margin-top:10px; }}
  h2 {{ margin:14px 0 4px; font-size:22px; color:var(--navy); }}
  h3 {{ margin:8px 0 4px; font-size:16px; color:var(--navy);
    font-family:"IBM Plex Sans", Arial, sans-serif; }}
  .rule {{ border:0; border-top:2px solid var(--navy); margin:4px 0 12px; }}
  .ver {{ font-style:italic; font-size:12px; color:#8a93a0; margin:0 0 2px; }}
  .warn {{ border:2px solid #e0c36a; background:#fff6d0; padding:10px 12px; margin:6px 0 12px;
    font-family:"IBM Plex Sans", Arial, sans-serif; font-size:14px; }}
  .goldbox {{ background:var(--gold); border:2px solid #c4a24a; padding:10px 12px; margin:8px 0 12px;
    font-family:"IBM Plex Sans", Arial, sans-serif; font-size:13.5px; font-weight:700; }}
  table.goldframe {{ outline:3px solid #c4a24a; }}
"""


def page(kind: str, body: str) -> str:
    css = SHEET_CSS if kind == "sheet" else DOC_CSS
    width = 1600 if kind == "sheet" else 1200
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet"/>
<style>{css}</style></head>
<body><div class="wrap">{body}</div></body></html>
"""


def badge() -> str:
    return '<div class="badge">EXAMPLE · <em>Station 99</em></div>'


PAGES: dict[str, tuple[str, int, int, str]] = {}


def _sheet_banner() -> str:
    return f'{badge()}<div class="banner">EXAMPLE ONLY — FAKE FIGURES — DO NOT COPY INTO WORKING SHEETS</div>'


PAGES["treasurer-report"] = (
    "sheet",
    1600,
    1000,
    _sheet_banner()
    + """
<h1>EXAMPLE VFD — Station 99 — Treasurer report (September 2099)</h1>
<p class="sub">Gold = you type it from a source document. Green = formula, locked. Every Difference line must read $0.00 before this report goes to the membership.</p>
<div class="sec">Money market / share account</div>
<table>
  <tr><td class="l">Balance forward</td><td class="g money">$1,000.00</td><td class="l">Interest / dividend</td><td class="g money">$5.00</td></tr>
  <tr><td class="l">Transfers in</td><td class="g money">$0.00</td><td class="l">Transfers out</td><td class="g money">$0.00</td></tr>
  <tr><td class="l">Ending balance</td><td class="f money">$1,005.00</td><td class="l">Statement / Difference</td><td class="f money">$0.00</td></tr>
</table>
<div class="sec">Savings / share account</div>
<table>
  <tr><td class="l">Balance forward</td><td class="g money">$2,000.00</td><td class="l">Interest / dividend</td><td class="g money">$5.00</td></tr>
  <tr><td class="l">Ending balance</td><td class="f money">$2,005.00</td><td class="l">Statement / Difference</td><td class="f money">$0.00</td></tr>
</table>
<div class="sec">Checking account</div>
<table>
  <tr><td class="l">Balance forward</td><td class="g money">$5,000.00</td><td class="l">Treasurer / chief debits</td><td class="g money">$5.00</td></tr>
  <tr><td class="l">Book ending balance</td><td class="f money">$4,995.00</td><td class="l">Bank service charges</td><td class="g money">$0.00</td></tr>
</table>
<div class="sec">Checking bank reconciliation — this is the line the membership should look at</div>
<table>
  <tr><td class="l">Statement balance</td><td class="g money">$5,795.00</td><td class="l">Book balance</td><td class="f money">$4,995.00</td></tr>
  <tr><td class="l">Deposits in transit − outstanding</td><td class="g money">($800.00)</td><td class="l">Difference</td><td class="f money">$0.00</td></tr>
</table>
<div class="sec">Total available funds as of September 30, 2099</div>
<table>
  <tr><td class="l">Money market</td><td class="f money">$1,005.00</td><td class="l">Savings</td><td class="f money">$2,005.00</td><td class="l">Checking</td><td class="f money">$4,995.00</td><td class="l">Grand total</td><td class="f money">$8,005.00</td></tr>
</table>
<p class="foot">NightWarder — blank template. Not legal advice. Not a completed report. EXAMPLE ONLY — fake round 2099 figures.</p>
""",
)

PAGES["training-cert-tracker"] = (
    "sheet",
    1600,
    1000,
    _sheet_banner()
    + """
<h1>EXAMPLE VFD — Station 99 — Training snapshot (year 2099 fake data)</h1>
<p class="sub">Sample roster and requirements. Intervals are toy figures — not legal intervals.</p>
<div class="sec">Sample roster (fake)</div>
<table>
  <tr><th>Member ID</th><th>Name</th><th>Rank / role</th><th>Status</th><th>Hire / join</th><th>Notes</th></tr>
  <tr><td>M-01</td><td class="g">Member Alpha</td><td>Firefighter</td><td>Active</td><td class="g">2095-03-01</td><td class="p">EXAMPLE</td></tr>
  <tr class="alt"><td>M-02</td><td class="g">Member Bravo</td><td>Lieutenant</td><td>Active</td><td class="g">2094-06-15</td><td class="p">EXAMPLE</td></tr>
  <tr><td>M-03</td><td class="g">Member Charlie</td><td>Engineer</td><td>Active</td><td class="g">2096-01-10</td><td class="p">EXAMPLE</td></tr>
</table>
<div class="sec">Sample requirements (fake months — NOT legal intervals)</div>
<table>
  <tr><th>Course</th><th>Category</th><th>Months (fake)</th><th>Notes</th></tr>
  <tr><td>Example CPR</td><td>Medical</td><td class="g">24</td><td>Toy interval</td></tr>
  <tr class="alt"><td>Example Driver</td><td>Apparatus</td><td class="g">12</td><td>Toy interval</td></tr>
  <tr><td>Example Bloodborne</td><td>Safety</td><td class="g">12</td><td>Toy interval</td></tr>
</table>
<div class="sec">Sample training records (fake)</div>
<table>
  <tr><th>Member</th><th>Course</th><th>Completed</th><th>Expires (manual toy)</th><th>Instructor</th><th>Status note</th></tr>
  <tr><td>Member Alpha</td><td>Example CPR</td><td class="g">2097-04-12</td><td class="f">2099-04-12</td><td>Instructor Example</td><td class="f">Current (toy)</td></tr>
  <tr class="alt"><td>Member Bravo</td><td>Example Driver</td><td class="g">2098-02-01</td><td class="f">2099-02-01</td><td>Instructor Example</td><td class="p">Due soon (toy)</td></tr>
  <tr><td>Member Charlie</td><td>Example Bloodborne</td><td class="g">2097-09-20</td><td class="f">2098-09-20</td><td>Instructor Example</td><td style="background:#f8d4d0">Overdue (toy)</td></tr>
</table>
<p class="foot">NightWarder — blank template. Not legal advice. Not a completed report.</p>
""",
)

PAGES["annual-budget-builder"] = (
    "sheet",
    1600,
    1000,
    _sheet_banner()
    + """
<h1>EXAMPLE VFD — Station 99 — FY2099 budget toy figures</h1>
<p class="sub">FAKE ONLY. Do not copy into Chart of Accounts / Budget Draft / Monthly Phasing. Variance math for illustration only.</p>
<table>
  <tr><th>Code</th><th>Description</th><th>Type</th><th>Prior actual</th><th>Proposed</th><th>Variance $</th><th>Var %</th><th>Notes</th></tr>
  <tr><td>E-100</td><td>Example Fuel</td><td>Expense</td><td class="g money">$8,000.00</td><td class="g money">$9,000.00</td><td class="f money">$1,000.00</td><td class="f">12.5%</td><td class="p">FAKE</td></tr>
  <tr class="alt"><td>E-200</td><td>Example Insurance</td><td>Expense</td><td class="g money">$12,000.00</td><td class="g money">$12,500.00</td><td class="f money">$500.00</td><td class="f">4.2%</td><td class="p">FAKE</td></tr>
  <tr><td>E-300</td><td>Example Training</td><td>Expense</td><td class="g money">$3,000.00</td><td class="g money">$3,500.00</td><td class="f money">$500.00</td><td class="f">16.7%</td><td class="p">FAKE</td></tr>
  <tr class="alt"><td>E-400</td><td>Example Apparatus</td><td>Expense</td><td class="g money">$15,000.00</td><td class="g money">$10,000.00</td><td class="f money">($5,000.00)</td><td class="f">-33.3%</td><td class="p">FAKE — lower one-time</td></tr>
  <tr><td colspan="4" class="l">Totals</td><td class="f money">$35,000.00</td><td class="f money">($3,000.00)</td><td class="f"></td><td></td></tr>
</table>
<p class="note">Lines are for illustration of variance math only — not a benchmark for a real budget.</p>
<p class="foot">NightWarder — blank template. Not legal advice. Not a completed report.</p>
""",
)

PAGES["apparatus-inspection-log"] = (
    "sheet",
    1600,
    1000,
    _sheet_banner()
    + """
<h1>EXAMPLE VFD — Station 99 — Engine 99 toy inspection (2099)</h1>
<p class="sub">Checklist items are examples of how a buyer might fill rows — not a mandated list.</p>
<div class="sec">Sample roster</div>
<table>
  <tr><th>Unit ID</th><th>Type</th><th>Year</th><th>Status</th><th>Station</th><th>Hours</th><th>Notes</th></tr>
  <tr><td class="g">E-99</td><td>Engine</td><td class="g">2090</td><td>In service</td><td>Station 99</td><td class="g">4400</td><td class="p">EXAMPLE</td></tr>
</table>
<div class="sec">Sample daily check rows</div>
<table>
  <tr><th>Date</th><th>Unit</th><th>Inspector</th><th>Item</th><th>Result</th><th>Notes</th><th>Overall</th></tr>
  <tr><td class="g">2099-03-02</td><td>E-99</td><td>Engineer Example</td><td>Fluid levels</td><td class="f">Pass</td><td></td><td class="f">In service</td></tr>
  <tr class="alt"><td class="g">2099-03-02</td><td>E-99</td><td>Engineer Example</td><td>Lights / siren</td><td class="f">Pass</td><td></td><td class="f">In service</td></tr>
  <tr><td class="g">2099-03-02</td><td>E-99</td><td>Engineer Example</td><td>Example pump panel</td><td style="background:#f8d4d0;font-weight:700">Fail</td><td class="p">Gauge sticky</td><td class="p">See defect</td></tr>
</table>
<div class="sec">Sample defect</div>
<table>
  <tr><th>Date</th><th>Unit</th><th>Defect</th><th>Severity</th><th>OOS</th></tr>
  <tr><td>2099-03-02</td><td>E-99</td><td class="g">Example pump panel gauge sticky</td><td>Minor</td><td class="f">N</td></tr>
</table>
<p class="foot">NightWarder — blank template. Not legal advice. Not a completed report. Formulas in the live file; typed values shown here.</p>
""",
)

PAGES["ppe-scba-tracker"] = (
    "sheet",
    1600,
    1000,
    _sheet_banner()
    + """
<h1>EXAMPLE VFD — Station 99 — PPE / SCBA toy data (2099)</h1>
<p class="sub">Demonstration only. Not OSHA law. Not a recommendation of intervals or manufacturers.</p>
<div class="sec">Sample inventory</div>
<table>
  <tr><th>Item type</th><th>Serial</th><th>Member</th><th>Manufacturer</th><th>Model</th><th>Size</th><th>In-service</th><th>Status</th></tr>
  <tr><td>SCBA</td><td class="g">EX-1001</td><td>Member Alpha</td><td>Example Mfr</td><td class="g">M-A</td><td>—</td><td>2095-04-01</td><td class="f">In service</td></tr>
  <tr class="alt"><td>Mask</td><td class="g">EX-2002</td><td>Member Bravo</td><td>Example Mfr</td><td class="g">M-B</td><td>M</td><td>2096-02-10</td><td class="f">In service</td></tr>
  <tr><td>Turnout coat</td><td class="g">EX-3003</td><td>Member Alpha</td><td>Example Mfr</td><td class="g">M-C</td><td>42</td><td>2095-08-20</td><td class="f">In service</td></tr>
</table>
<div class="sec">Sample fit tests (fake months)</div>
<table>
  <tr><th>Date</th><th>Member</th><th>Mask</th><th>Result</th><th>Months (fake)</th><th>Next due</th><th>Tester</th><th>Notes</th></tr>
  <tr><td class="g">2098-03-15</td><td>Member Alpha</td><td>EX-2001</td><td class="f">Pass</td><td class="g">12</td><td class="f">2099-03-15</td><td>Tester Example</td><td class="p">Toy interval</td></tr>
  <tr class="alt"><td class="g">2098-03-15</td><td>Member Bravo</td><td>EX-2002</td><td class="f">Pass</td><td class="g">12</td><td class="f">2099-03-15</td><td>Tester Example</td><td class="p">Toy interval</td></tr>
</table>
<p class="note">The highlighted 12 is a placeholder — not a recommendation.</p>
<p class="foot">NightWarder — blank template. Not legal advice. Not a completed report.</p>
""",
)

PAGES["donation-register"] = (
    "sheet",
    1600,
    1000,
    _sheet_banner()
    + """
<h1>EXAMPLE VFD — Station 99 — Donation toy register (2099)</h1>
<p class="sub">FAKE ONLY. Not tax advice. Not a Form 990.</p>
<div class="sec">Sample receipts</div>
<table>
  <tr><th>Date</th><th>Receipt #</th><th>Donor</th><th>Amount</th><th>Method</th><th>Rest.?</th><th>Purpose</th><th>Batch</th><th>Thank-you</th></tr>
  <tr><td class="g">2099-03-02</td><td>R-01</td><td class="g">Donor Example A</td><td class="g money">$250.00</td><td>Check</td><td>N</td><td class="p">General</td><td>DEP-01</td><td class="f">Y</td></tr>
  <tr class="alt"><td class="g">2099-03-02</td><td>R-02</td><td class="g">Donor Example B</td><td class="g money">$350.00</td><td>Check</td><td>N</td><td class="p">General</td><td>DEP-01</td><td class="f">Y</td></tr>
  <tr><td class="g">2099-03-10</td><td>R-03</td><td class="g">Donor Example C</td><td class="g money">$50.00</td><td>Cash</td><td>N</td><td class="p">General</td><td></td><td></td></tr>
  <tr><td colspan="3" class="l">TOTAL</td><td class="f money">$650.00</td><td colspan="5"></td></tr>
</table>
<div class="sec">Sample deposit tie-out</div>
<table>
  <tr><th>Batch</th><th>Date</th><th>Bank $</th><th>Notes</th></tr>
  <tr><td>DEP-01</td><td class="g">2099-03-03</td><td class="f money">$600.00</td><td class="p">Matches R-01 + R-02. R-03 left open on purpose so the buyer sees an unmatched receipt.</td></tr>
</table>
<p class="foot">NightWarder — blank template. Not legal advice. Not a completed report. Not tax advice. Not a Form 990.</p>
""",
)

PAGES["incident-aar"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-AAR-01 | Blank template | Version 2026-09-03c</p>
{badge()}
<h1>4. Incident header</h1>
<p class="sub">Copy times from CAD or the radio log. Check every type that applies. Gold is input. Do not invent.</p>
<table>
  <tr><td class="l">Department / AHJ</td><td class="g"></td><td class="l">Incident name</td><td class="g"></td></tr>
  <tr><td class="l">Incident # (CAD)</td><td class="g"></td><td class="l">Run report / NFIRS #</td><td class="g"></td></tr>
  <tr><td class="l">Date</td><td class="g"></td><td class="l">Address / location</td><td class="g"></td></tr>
  <tr><td class="l">Alarm time</td><td class="g"></td><td class="l">First unit on scene</td><td class="g"></td></tr>
  <tr><td class="l">Control time</td><td class="g"></td><td class="l">Available / last unit clear</td><td class="g"></td></tr>
  <tr><td class="l">Incident commander</td><td class="g"></td><td class="l">Safety officer / ISO</td><td class="g"></td></tr>
  <tr><td class="l">First-due unit</td><td class="g"></td><td class="l">Shift / tour</td><td class="g"></td></tr>
  <tr><td class="l">Alarm level / assignment</td><td class="g"></td><td class="l">Total personnel on scene</td><td class="g"></td></tr>
  <tr><td class="l">Weather observed</td><td class="g"></td><td class="l">Heat index or WBGT</td><td class="g"></td></tr>
  <tr><td class="l">Mutual aid</td><td class="g"></td><td class="l">Who wrote this packet</td><td class="g"></td></tr>
</table>
<p class="sub" style="margin-top:8px">Incident type — check all that apply</p>
<div class="checks">
  <span><i class="box"></i> Fire</span><span><i class="box"></i> MVC</span>
  <span><i class="box"></i> Medical</span><span><i class="box"></i> Hazmat</span>
  <span><i class="box"></i> Weather</span><span><i class="box"></i> Other</span>
  <span><i class="box"></i> Rescue / extrication</span><span><i class="box"></i> Wildland</span>
  <span><i class="box"></i> Water / ice</span><span><i class="box"></i> Alarm / good intent</span>
  <span><i class="box"></i> Standby / cover</span><span><i class="box"></i> Training</span>
</div>
<p class="sub" style="margin-top:14px">Brief nature / occupancy / what was dispatched</p>
<table><tr><td class="g" style="height:42px"></td></tr></table>
<p class="foot">Brief nature is a phrase you would say on the radio, not a finished narrative.</p>
""",
)

PAGES["heat-illness-sop"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-HEAT-01 | Blank template | Version 2026-09-03c</p>
{badge()}
<div class="bar">ATTACHMENT A | HEAT INCIDENT / REHAB LOG</div>
<p class="sub">Operational log. Not a medical record. Not a workers' comp form. Not OSHA law. File with the incident.</p>
<table>
  <tr><td class="l">Incident / drill name</td><td class="g"></td><td class="l">Date</td><td class="g"></td></tr>
  <tr><td class="l">Location</td><td class="g"></td><td class="l">Operational period</td><td class="g"></td></tr>
  <tr><td class="l">Incident Commander</td><td class="g"></td><td class="l">ISO / Safety</td><td class="g"></td></tr>
  <tr><td class="l">Rehab officer</td><td class="g"></td><td class="l">Rehab location</td><td class="g"></td></tr>
</table>
<div class="bar" style="font-size:16px">Conditions (descriptive — not an action-level determination)</div>
<table>
  <tr><th>Weather / sun (describe)</th><th>Metric used, if any (AHJ)</th><th>Value observed</th><th>PPE in use</th></tr>
  <tr><td class="g" style="height:36px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
<div class="bar" style="font-size:16px">Member log</div>
<p class="sub">Vitals only as local EMS protocol requires. This form does not set cutoffs.</p>
<table>
  <tr><th>Name</th><th>Unit</th><th>In</th><th>Vitals (local EMS)</th><th>Fluids</th><th>Cooling</th><th>Out</th><th>RTD Y/N | notes</th></tr>
  <tr><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
<div class="bar" style="font-size:16px">Members who were symptomatic or transported</div>
<table>
  <tr><th>Name</th><th>Time noticed</th><th>Time cooling started</th><th>Destination / refused</th></tr>
  <tr><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
<p class="foot">SKU-NW-HEAT-01 Attachment A | Blank template | Not a completed program | Does not replace [Department] injury reporting, workers' comp, or OSHA recordkeeping.</p>
""",
)

PAGES["cold-weather-sop"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-COLD-01 | Blank template | Version 2026-09-03e</p>
{badge()}
<div class="bar">ATTACHMENT A | COLD INCIDENT / REHAB LOG <span style="float:right;font-size:14px;font-weight:500">One page | empty form</span></div>
<p class="sub">Operational log. Not a medical record, not a workers' compensation form, not OSHA recordkeeping. File with the incident.</p>
<table>
  <tr><td class="l">Incident / drill name</td><td class="g"></td><td class="l">Date</td><td class="g"></td></tr>
  <tr><td class="l">Location</td><td class="g"></td><td class="l">Operational period</td><td class="g"></td></tr>
  <tr><td class="l">Incident Commander</td><td class="g"></td><td class="l">ISO / Safety</td><td class="g"></td></tr>
  <tr><td class="l">Rehab officer</td><td class="g"></td><td class="l">Rehab / warming location</td><td class="g"></td></tr>
</table>
<div class="bar" style="font-size:16px">Conditions — descriptive. This is not an action-level determination.</div>
<table>
  <tr><th>Weather / wind (describe)</th><th>Metric used, if any</th><th>Value observed</th><th>Wet PPE? (Y/N)</th></tr>
  <tr><td class="g" style="height:36px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:36px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
<div class="bar" style="font-size:16px">Member log — vitals only as local EMS protocol requires. This form sets no cutoffs.</div>
<table>
  <tr><th>Name</th><th>Unit</th><th>In</th><th>Vitals (local EMS)</th><th>Fluids</th><th>Warming</th><th>Out</th><th>Released Y/N — by whom</th></tr>
  <tr><td class="g" style="height:30px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:30px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:30px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:30px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:30px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
""",
)

PAGES["exposure-near-miss-log"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-EXP-01 | Blank template | Version 2026-09-03e</p>
{badge()}
<h1>2. Incident / near-miss header</h1>
<p class="sub">Gold = input.</p>
<table>
  <tr><td class="l">Department / AHJ</td><td class="g"></td><td class="l">Date of event</td><td class="g"></td></tr>
  <tr><td class="l">Location / address</td><td class="g"></td><td class="l">CAD / incident #</td><td class="g"></td></tr>
  <tr><td class="l">IC / OIC</td><td class="g"></td><td class="l">Log / report #</td><td class="g"></td></tr>
  <tr><td class="l">Time noticed</td><td class="g"></td><td class="l">Immediate risk still open?</td><td class="g"></td></tr>
</table>
<p class="sub">Type — check all that apply</p>
<div class="checks" style="grid-template-columns:repeat(4,1fr)">
  <span><i class="box"></i> Exposure</span>
  <span><i class="box"></i> Near-miss</span>
  <span><i class="box"></i> Injury-adjacent</span>
  <span><i class="box"></i> Equipment failure</span>
</div>
<p class="sub" style="margin-top:12px">Brief nature — one radio-length phrase</p>
<table><tr><td class="g" style="height:40px"></td></tr></table>
<h1>3. Sequence of events</h1>
<p class="sub">Chronological log. Copy times from CAD, the radio, or what you observed.</p>
<table>
  <tr><th style="width:16%">Time</th><th style="width:28%">Source (CAD / radio / observed)</th><th>Event</th></tr>
  <tr><td class="g" style="height:32px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:32px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:32px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:32px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:32px"></td><td class="g"></td><td class="g"></td></tr>
</table>
""",
)

PAGES["member-meeting-packet"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-MTG-01 | Blank template | Version 2026-09-03e</p>
{badge()}
<h1>1. Meeting header</h1>
<p class="sub">Gold blanks. Fill when the meeting is called to order. Do not invent.</p>
<table>
  <tr><td class="l">Department / body</td><td class="g"></td><td class="l">Meeting type (regular / special)</td><td class="g"></td></tr>
  <tr><td class="l">Meeting date</td><td class="g"></td><td class="l">Call-to-order time</td><td class="g"></td></tr>
  <tr><td class="l">Location</td><td class="g"></td><td class="l">Adjournment time</td><td class="g"></td></tr>
  <tr><td class="l">Presiding officer</td><td class="g"></td><td class="l">Secretary / recorder</td><td class="g"></td></tr>
  <tr><td class="l">Quorum required</td><td class="g"></td><td class="l">Quorum present?</td><td class="g"></td></tr>
  <tr><td class="l">Notice given</td><td class="g"></td><td class="l">Bylaws / SOP reference</td><td class="g"></td></tr>
</table>
<p class="foot">No quorum means no binding action. Discussion is still discussion — record it, and record that nothing was adopted.</p>
<h1>1.1 Prior minutes</h1>
<table>
  <tr><th>Item</th><th style="width:10%">Yes</th><th style="width:10%">No</th><th>Detail</th></tr>
  <tr><td>Prior minutes read or distributed</td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td>Corrections offered</td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td>Approved as read / as corrected</td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td>Date of the minutes approved</td><td colspan="2" class="g"></td><td class="g"></td></tr>
</table>
<h1>1.2 Officers present</h1>
<table>
  <tr><th>Office / role</th><th>Name (print)</th><th style="width:14%">Present</th><th style="width:14%">Excused</th></tr>
  <tr><td class="l">Chief / presiding</td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Secretary</td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Treasurer</td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
""",
)

PAGES["hot-work-permit"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-HWP-01 | Blank template</p>
<p class="ver">Ver. 2026-09-04a</p>
{badge()}
<hr class="rule"/>
<h1>6. PPE blank list</h1>
<p class="sub">Buyer lists PPE required for THIS job. Empty rows until known. Do not invent.</p>
<table>
  <tr><th style="width:8%">#</th><th>PPE item (buyer lists)</th><th style="width:36%">Confirmed (Y/N/NA + initials)</th></tr>
  <tr><td>1</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
  <tr><td>2</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
  <tr><td>3</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
  <tr><td>4</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
  <tr><td>5</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
  <tr><td>6</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
  <tr><td>7</td><td class="g" style="height:26px"></td><td class="g"></td></tr>
</table>
<h1>7. Authorizations</h1>
<h3>7.1 Signatures before work starts</h3>
<p class="sub">Gold blanks. A blank signature means this is still a template — not a completed authorization.</p>
<table class="goldframe">
  <tr><th style="width:26%">Role</th><th>Printed name</th><th>Signature</th><th style="width:16%">Date</th></tr>
  <tr><td class="l">Operator</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Fire watch</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Authorizer</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Contact / other (title):</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
</table>
<div class="goldbox">NOT A COMPLETED AUTHORIZATION. Unsigned gold rows mean this permit is not authorized. NightWarder signature blocks are blanks — not AHJ approval and not OSHA permission.</div>
<h1>8. Close-out</h1>
<p class="sub">Complete when work stops or the permit is cancelled.</p>
<table>
  <tr><td class="l">Work stopped? (Y / N + time)</td><td class="g" style="height:28px"></td></tr>
</table>
""",
)

PAGES["confined-space-entry-permit"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-CSE-01 | Blank template</p>
<p class="ver">Ver. 2026-09-04c</p>
{badge()}
<hr class="rule"/>
<h1>4.1 Isolation / energy control note</h1>
<div class="warn"><strong>LOTO IS SEPARATE.</strong> This is NOT a full lockout/tagout procedure. If energy isolation is required, follow [Department]'s separate LOTO process and record a brief status note below.</div>
<table>
  <tr><td class="l">Isolation / LOTO status note (not a full LOTO procedure)</td><td class="g" style="height:32px"></td></tr>
  <tr><td class="l">LOTO procedure reference / permit # (if any)</td><td class="g" style="height:28px"></td></tr>
</table>
<h1>5. Atmosphere testing log</h1>
<p class="sub">Empty rows. Fill only from real tests. Do not invent O2 / LEL / toxic values. Columns are INPUT blanks — not claimed OSHA limits.</p>
<table>
  <tr><th>Time</th><th>O2</th><th>LEL</th><th>H2S (toxic)</th><th>CO (toxic)</th><th>Other toxic</th><th>Tester</th></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="g" style="height:24px"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
<table>
  <tr><td class="l">Instrument ID / calibration note (if known)</td><td class="g" style="height:28px"></td></tr>
  <tr><td class="l">Acceptable ranges used (local / AHJ — blank until set)</td><td class="g" style="height:28px"></td></tr>
</table>
<h1>6. Rescue plan / retrieval and communication</h1>
<p class="sub">Blank fields only. Do not invent rescue capability. If [Department] cannot support entry rescue as required locally, do not authorize entry on this form alone.</p>
<table>
  <tr><td class="l">Rescue / retrieval note</td><td class="g" style="height:28px"></td></tr>
</table>
""",
)

PAGES["permit-to-work"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-PTW-01 | Blank template</p>
<p class="ver">Ver. 2026-09-04a</p>
{badge()}
<hr class="rule"/>
<table>
  <tr><td class="l">Emergency contact / radio channel for this job</td><td class="g" style="height:30px"></td></tr>
</table>
<table>
  <tr><th>Item (label only — buyer completes)</th><th style="width:14%">Y / N / NA</th><th style="width:28%">Notes / initials</th></tr>
  <tr><td class="l">Briefing held with performing party</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Area authority aware of work window</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Required specific permits attached / referenced</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Other precaution (describe in notes)</td><td></td><td class="g" style="height:26px"></td></tr>
</table>
<h1>5. Approvals</h1>
<h3>5.1 Authorization signatures</h3>
<p class="sub">Gold blanks. A blank signature means this is still a template — not a completed authorization.</p>
<table class="goldframe">
  <tr><th style="width:26%">Role</th><th>Printed name</th><th>Signature</th><th style="width:16%">Date</th></tr>
  <tr><td class="l">Requestor</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Area / officer authority</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Safety (optional)</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Other (title):</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
</table>
<div class="goldbox">NOT A COMPLETED AUTHORIZATION. Unsigned gold rows mean this cover is not authorized. Not AHJ approval. Not OSHA permission. Does not replace specific permits.</div>
<h1>6. Suspend / close-out</h1>
<p class="sub">Use when work is suspended, cancelled, or completed.</p>
<table>
  <tr><td class="l">Status (Active / Suspended / Closed)</td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Suspend reason / time (if used)</td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Work complete? (Y / N + time)</td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Area restored / inspected? (Y / N + by whom)</td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Closed by (printed name)</td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Close-out signature / date</td><td class="g" style="height:26px"></td></tr>
</table>
""",
)

PAGES["lockout-tagout-pack"] = (
    "doc",
    1200,
    1550,
    f"""
<p class="meta">NightWarder | SKU-NW-LOTO-01 | Blank template</p>
<p class="ver">Ver. 2026-09-05</p>
{badge()}
<hr class="rule"/>
<h1>Lockout / Tagout authorization</h1>
<p class="sub">Blank pack: authorization + isolation checklist + device log. Not a completed lockout. Not a written energy-control program. Not OSHA law.</p>
<table>
  <tr><td class="l">Equipment / energy source (buyer names)</td><td class="g" style="height:28px"></td></tr>
  <tr><td class="l">Location / site</td><td class="g" style="height:28px"></td></tr>
  <tr><td class="l">Work window (start / expected end)</td><td class="g" style="height:28px"></td></tr>
  <tr><td class="l">Authorized employee (printed name)</td><td class="g" style="height:28px"></td></tr>
</table>
<h1>Isolation checklist</h1>
<p class="sub">Label-only rows. Gold blanks until the buyer fills them from the real job. Do not invent isolation steps.</p>
<table>
  <tr><th>Step (label only — buyer completes)</th><th style="width:14%">Y / N / NA</th><th style="width:28%">Notes / initials</th></tr>
  <tr><td class="l">Notify affected people</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Shut down equipment</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Isolate energy source(s)</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Apply lock / tag devices</td><td></td><td class="g" style="height:26px"></td></tr>
  <tr><td class="l">Verify zero energy (try-out)</td><td></td><td class="g" style="height:26px"></td></tr>
</table>
<h1>Device log</h1>
<p class="sub">Empty rows. Record devices actually applied. A blank log is not a lockout.</p>
<table>
  <tr><th style="width:8%">#</th><th>Device ID / type</th><th>Energy type</th><th>Location on equipment</th><th style="width:16%">Applied by</th></tr>
  <tr><td>1</td><td class="g" style="height:26px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td>2</td><td class="g" style="height:26px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td>3</td><td class="g" style="height:26px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td>4</td><td class="g" style="height:26px"></td><td class="g"></td><td class="g"></td><td class="g"></td></tr>
</table>
<h1>Authorization signatures</h1>
<p class="sub">Gold blanks. A blank signature means this is still a template — not a completed lockout.</p>
<table class="goldframe">
  <tr><th style="width:26%">Role</th><th>Printed name</th><th>Signature</th><th style="width:16%">Date</th></tr>
  <tr><td class="l">Authorized employee</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Area / officer authority</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
  <tr><td class="l">Other (title):</td><td class="g" style="height:28px"></td><td class="g"></td><td class="g"></td></tr>
</table>
<div class="goldbox">NOT A COMPLETED LOCKOUT. Unsigned gold rows mean energy is not controlled on this form. Not a written energy-control program. Not OSHA law. Not AHJ approval.</div>
""",
)


def chrome_shot(html_path: Path, png_path: Path, w: int, h: int) -> None:
    png_path.parent.mkdir(parents=True, exist_ok=True)
    if png_path.exists():
        png_path.unlink()
    cmd = [
        "google-chrome",
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--hide-scrollbars",
        "--no-first-run",
        "--force-device-scale-factor=1",
        f"--window-size={w},{h}",
        f"--screenshot={png_path}",
        html_path.resolve().as_uri(),
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(80):
        if png_path.exists() and png_path.stat().st_size > 2000:
            proc.kill()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
            return
        if proc.poll() is not None:
            break
        __import__("time").sleep(0.25)
    proc.kill()
    if not png_path.exists() or png_path.stat().st_size < 2000:
        raise RuntimeError(f"screenshot failed for {html_path.name}")


def crop_top(src: Path, dest: Path, ratio_w: int = 16, ratio_h: int = 10) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target_h = int(w * ratio_h / ratio_w)
    if h > target_h:
        im = im.crop((0, 0, w, target_h))
    im.save(dest, "PNG", optimize=True)


def collage(parts: list[Path], dest: Path) -> None:
    tiles = [Image.open(p).convert("RGB") for p in parts]
    tw, th = 720, 450
    fitted = []
    for t in tiles:
        t = t.copy()
        t.thumbnail((tw, th), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (tw, th), (18, 20, 24))
        x = (tw - t.width) // 2
        y = (th - t.height) // 2
        canvas.paste(t, (x, y))
        fitted.append(canvas)
    gap = 22
    pad_x, pad_top, pad_bot = 36, 88, 56
    width = pad_x * 2 + tw * 3 + gap * 2
    height = pad_top + th + pad_bot
    bg = Image.new("RGB", (width, height), (28, 30, 34))
    draw = ImageDraw.Draw(bg)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 42)
        small = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 20)
        cap = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 18)
    except OSError:
        title_font = small = cap = ImageFont.load_default()
    draw.text((36, 22), "Core bundle sample", fill=(240, 196, 75), font=title_font)
    draw.rounded_rectangle((width - 280, 22, width - 36, 58), 16, fill=(17, 17, 17))
    draw.text((width - 262, 28), "EXAMPLE  ·  Station 99", fill=(240, 196, 75), font=small)
    labels = ["Treasurer report", "Incident AAR", "Heat illness SOP"]
    for i, (tile, label) in enumerate(zip(fitted, labels)):
        x = pad_x + i * (tw + gap)
        bg.paste(tile, (x, pad_top))
        draw.text((x, pad_top + th + 10), label, fill=(230, 232, 236), font=cap)
    bg.save(dest, "PNG", optimize=True)


def main() -> int:
    WORK.mkdir(parents=True, exist_ok=True)
    SHOT.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    for name, (kind, w, h, body) in PAGES.items():
        html_path = WORK / f"{name}.html"
        html_path.write_text(page(kind, body), encoding="utf-8")
        raw = SHOT / f"{name}-raw.png"
        print(f"screenshot {name} ({w}x{h})")
        chrome_shot(html_path, raw, w, h)
        crop_top(raw, OUT / f"{name}.png", 16, 10)

    collage(
        [OUT / "treasurer-report.png", OUT / "incident-aar.png", OUT / "heat-illness-sop.png"],
        OUT / "core-bundle.png",
    )
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
