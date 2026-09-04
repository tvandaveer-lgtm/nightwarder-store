#!/usr/bin/env python3
"""Generate honest NightWarder kit-cover thumbnails (not fake sheet screenshots)."""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets" / "thumbs"

SKUS = [
    {
        "file": "core-bundle.svg",
        "title": "Core bundle",
        "sub": "Treasurer · AAR · Heat SOP",
        "kind": "3-kit pack",
        "accent": "#d4652a",
        "accent2": "#8a3d16",
        "paper": "#1b1612",
        "ink": "#f3ece4",
        "muted": "#b9a89a",
        "icon": "stack",
    },
    {
        "file": "treasurer-report.svg",
        "title": "Treasurer report",
        "sub": "Monthly workbook",
        "kind": "Workbook kit",
        "accent": "#7a9a4e",
        "accent2": "#3d5226",
        "paper": "#151811",
        "ink": "#eef3e6",
        "muted": "#a8b49a",
        "icon": "ledger",
    },
    {
        "file": "incident-aar.svg",
        "title": "Incident AAR",
        "sub": "After-action packet",
        "kind": "Review kit",
        "accent": "#5b7fb3",
        "accent2": "#2c4366",
        "paper": "#12161c",
        "ink": "#e8eef6",
        "muted": "#9aa8bc",
        "icon": "clipboard",
    },
    {
        "file": "heat-illness-sop.svg",
        "title": "Heat illness SOP",
        "sub": "Template only — not OSHA law",
        "kind": "SOP kit",
        "accent": "#e06a2a",
        "accent2": "#8a3a12",
        "paper": "#1c1410",
        "ink": "#f6ebe3",
        "muted": "#c4a894",
        "icon": "sun",
    },
    {
        "file": "training-cert-tracker.svg",
        "title": "Training cert tracker",
        "sub": "Certs and renewals",
        "kind": "Tracker kit",
        "accent": "#3f7f96",
        "accent2": "#1f4554",
        "paper": "#10161a",
        "ink": "#e6f1f4",
        "muted": "#95b0b8",
        "icon": "badge",
    },
    {
        "file": "annual-budget-builder.svg",
        "title": "Annual budget builder",
        "sub": "Department workbook",
        "kind": "Workbook kit",
        "accent": "#6b8f45",
        "accent2": "#354822",
        "paper": "#141811",
        "ink": "#eef3e6",
        "muted": "#a6b396",
        "icon": "bars",
    },
    {
        "file": "apparatus-inspection-log.svg",
        "title": "Apparatus inspection",
        "sub": "Blank inspection log",
        "kind": "Log kit",
        "accent": "#c24a36",
        "accent2": "#6e261c",
        "paper": "#1a1212",
        "ink": "#f6e8e6",
        "muted": "#c4a29c",
        "icon": "truck",
    },
    {
        "file": "ppe-scba-tracker.svg",
        "title": "PPE / SCBA tracker",
        "sub": "Inventory and inspection",
        "kind": "Tracker kit",
        "accent": "#c4893a",
        "accent2": "#6e4a1a",
        "paper": "#181410",
        "ink": "#f4eee4",
        "muted": "#c0b09a",
        "icon": "shield",
    },
    {
        "file": "donation-register.svg",
        "title": "Donation register",
        "sub": "Fundraising log",
        "kind": "Register kit",
        "accent": "#c9a24a",
        "accent2": "#6e5618",
        "paper": "#1a1710",
        "ink": "#f6f0de",
        "muted": "#c4b48a",
        "icon": "box",
    },
    {
        "file": "exposure-near-miss-log.svg",
        "title": "Exposure / near-miss",
        "sub": "Blank log template",
        "kind": "Log kit",
        "accent": "#d4b03a",
        "accent2": "#6e5a12",
        "paper": "#1a1710",
        "ink": "#f6f1dc",
        "muted": "#c8b888",
        "icon": "diamond",
    },
    {
        "file": "cold-weather-sop.svg",
        "title": "Cold weather SOP",
        "sub": "Template only — not OSHA law",
        "kind": "SOP kit",
        "accent": "#6aa3c4",
        "accent2": "#2c5366",
        "paper": "#10161a",
        "ink": "#e6f0f6",
        "muted": "#9ab4c4",
        "icon": "flake",
    },
    {
        "file": "member-meeting-packet.svg",
        "title": "Member meeting packet",
        "sub": "Agenda and minutes",
        "kind": "Packet kit",
        "accent": "#8a94a0",
        "accent2": "#3e4650",
        "paper": "#141618",
        "ink": "#eef0f3",
        "muted": "#a8b0b8",
        "icon": "agenda",
    },
]


def icon_markup(kind: str, accent: str, ink: str) -> str:
    # Centered around 180, 198
    if kind == "stack":
        return f"""
      <g transform="translate(180 198)">
        <rect x="-52" y="-8" width="88" height="58" rx="4" fill="{accent}" opacity="0.35"/>
        <rect x="-44" y="-18" width="88" height="58" rx="4" fill="{accent}" opacity="0.6"/>
        <rect x="-36" y="-28" width="88" height="58" rx="4" fill="{accent}"/>
        <rect x="-26" y="-14" width="68" height="4" rx="2" fill="{ink}" opacity="0.85"/>
        <rect x="-26" y="-4" width="48" height="3" rx="1.5" fill="{ink}" opacity="0.45"/>
        <rect x="-26" y="5" width="56" height="3" rx="1.5" fill="{ink}" opacity="0.45"/>
      </g>"""
    if kind == "ledger":
        return f"""
      <g transform="translate(180 198)">
        <rect x="-48" y="-36" width="96" height="72" rx="5" fill="none" stroke="{accent}" stroke-width="3"/>
        <line x1="-48" y1="-12" x2="48" y2="-12" stroke="{accent}" stroke-width="2"/>
        <line x1="-16" y1="-36" x2="-16" y2="36" stroke="{accent}" stroke-width="2"/>
        <rect x="-8" y="-4" width="40" height="4" rx="2" fill="{ink}" opacity="0.7"/>
        <rect x="-8" y="8" width="28" height="3" rx="1.5" fill="{ink}" opacity="0.4"/>
        <rect x="-8" y="18" width="34" height="3" rx="1.5" fill="{ink}" opacity="0.4"/>
      </g>"""
    if kind == "clipboard":
        return f"""
      <g transform="translate(180 198)">
        <rect x="-40" y="-40" width="80" height="86" rx="6" fill="none" stroke="{accent}" stroke-width="3"/>
        <rect x="-18" y="-50" width="36" height="16" rx="3" fill="{accent}"/>
        <rect x="-26" y="-16" width="52" height="4" rx="2" fill="{ink}" opacity="0.75"/>
        <rect x="-26" y="-4" width="40" height="3" rx="1.5" fill="{ink}" opacity="0.4"/>
        <rect x="-26" y="8" width="46" height="3" rx="1.5" fill="{ink}" opacity="0.4"/>
        <rect x="-26" y="20" width="30" height="3" rx="1.5" fill="{ink}" opacity="0.4"/>
      </g>"""
    if kind == "sun":
        return f"""
      <g transform="translate(180 198)">
        <circle cx="0" cy="0" r="22" fill="{accent}"/>
        <g stroke="{accent}" stroke-width="4" stroke-linecap="round">
          <line x1="0" y1="-42" x2="0" y2="-32"/>
          <line x1="0" y1="32" x2="0" y2="42"/>
          <line x1="-42" y1="0" x2="-32" y2="0"/>
          <line x1="32" y1="0" x2="42" y2="0"/>
          <line x1="-30" y1="-30" x2="-23" y2="-23"/>
          <line x1="23" y1="23" x2="30" y2="30"/>
          <line x1="30" y1="-30" x2="23" y2="-23"/>
          <line x1="-23" y1="23" x2="-30" y2="30"/>
        </g>
      </g>"""
    if kind == "badge":
        return f"""
      <g transform="translate(180 198)">
        <path d="M0 -44 L36 -28 L36 8 C36 28 18 42 0 48 C-18 42 -36 28 -36 8 L-36 -28 Z"
              fill="none" stroke="{accent}" stroke-width="3"/>
        <circle cx="0" cy="-2" r="14" fill="{accent}"/>
        <path d="M-6 2 L-1 7 L8 -6" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      </g>"""
    if kind == "bars":
        return f"""
      <g transform="translate(180 198)">
        <rect x="-42" y="8" width="18" height="32" rx="3" fill="{accent}" opacity="0.45"/>
        <rect x="-16" y="-8" width="18" height="48" rx="3" fill="{accent}" opacity="0.7"/>
        <rect x="10" y="-28" width="18" height="68" rx="3" fill="{accent}"/>
        <line x1="-48" y1="44" x2="48" y2="44" stroke="{ink}" stroke-width="2" opacity="0.5"/>
      </g>"""
    if kind == "truck":
        return f"""
      <g transform="translate(180 198)">
        <rect x="-54" y="-10" width="78" height="28" rx="4" fill="{accent}"/>
        <rect x="18" y="-2" width="32" height="20" rx="3" fill="{accent}" opacity="0.75"/>
        <rect x="-46" y="-22" width="36" height="14" rx="2" fill="{accent}" opacity="0.55"/>
        <circle cx="-28" cy="24" r="9" fill="none" stroke="{ink}" stroke-width="3"/>
        <circle cx="22" cy="24" r="9" fill="none" stroke="{ink}" stroke-width="3"/>
      </g>"""
    if kind == "shield":
        return f"""
      <g transform="translate(180 198)">
        <path d="M0 -44 L40 -28 L40 6 C40 28 20 44 0 50 C-20 44 -40 28 -40 6 L-40 -28 Z"
              fill="none" stroke="{accent}" stroke-width="3.5"/>
        <path d="M0 -26 L18 -18 L18 4 C18 16 8 26 0 30 C-8 26 -18 16 -18 4 L-18 -18 Z" fill="{accent}"/>
      </g>"""
    if kind == "box":
        return f"""
      <g transform="translate(180 198)">
        <path d="M-40 -6 L0 -26 L40 -6 L0 14 Z" fill="{accent}"/>
        <path d="M-40 -6 L-40 22 L0 42 L0 14 Z" fill="{accent}" opacity="0.7"/>
        <path d="M40 -6 L40 22 L0 42 L0 14 Z" fill="{accent}" opacity="0.45"/>
      </g>"""
    if kind == "diamond":
        return f"""
      <g transform="translate(180 198)">
        <path d="M0 -48 L48 0 L0 48 L-48 0 Z" fill="none" stroke="{accent}" stroke-width="4"/>
        <rect x="-4" y="-18" width="8" height="22" rx="2" fill="{accent}"/>
        <circle cx="0" cy="16" r="5" fill="{accent}"/>
      </g>"""
    if kind == "flake":
        return f"""
      <g transform="translate(180 198)" stroke="{accent}" stroke-width="4" stroke-linecap="round">
        <line x1="0" y1="-40" x2="0" y2="40"/>
        <line x1="-40" y1="0" x2="40" y2="0"/>
        <line x1="-28" y1="-28" x2="28" y2="28"/>
        <line x1="28" y1="-28" x2="-28" y2="28"/>
        <circle cx="0" cy="0" r="8" fill="{accent}" stroke="none"/>
      </g>"""
    # agenda
    return f"""
      <g transform="translate(180 198)">
        <rect x="-44" y="-36" width="88" height="72" rx="5" fill="none" stroke="{accent}" stroke-width="3"/>
        <rect x="-30" y="-20" width="60" height="5" rx="2" fill="{accent}"/>
        <rect x="-30" y="-6" width="44" height="4" rx="2" fill="{ink}" opacity="0.45"/>
        <rect x="-30" y="6" width="50" height="4" rx="2" fill="{ink}" opacity="0.45"/>
        <rect x="-30" y="18" width="36" height="4" rx="2" fill="{ink}" opacity="0.45"/>
      </g>"""


def cover(sku: dict) -> str:
    accent = sku["accent"]
    accent2 = sku["accent2"]
    paper = sku["paper"]
    ink = sku["ink"]
    muted = sku["muted"]
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 480" width="360" height="480" role="img" aria-label="NightWarder kit cover: {sku['title']}">
  <title>NightWarder kit cover — {sku['title']}</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{paper}"/>
      <stop offset="1" stop-color="#0b0d10"/>
    </linearGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{accent2}"/>
      <stop offset="1" stop-color="{accent}"/>
    </linearGradient>
    <pattern id="grid" width="18" height="18" patternUnits="userSpaceOnUse">
      <path d="M18 0H0V18" fill="none" stroke="{ink}" stroke-opacity="0.04" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="360" height="480" fill="url(#bg)"/>
  <rect width="360" height="480" fill="url(#grid)"/>
  <rect x="0" y="0" width="360" height="10" fill="url(#bar)"/>
  <rect x="18" y="18" width="324" height="444" rx="10" fill="none" stroke="{accent}" stroke-opacity="0.28" stroke-width="1.5"/>

  <g font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif">
    <text x="32" y="54" fill="{accent}" font-size="11" font-weight="700" letter-spacing="2.4">NIGHTWARDER</text>
    <text x="328" y="54" fill="{muted}" font-size="10" font-weight="600" letter-spacing="1.4" text-anchor="end">KIT COVER</text>
  </g>
  <line x1="32" y1="66" x2="328" y2="66" stroke="{accent}" stroke-opacity="0.35" stroke-width="1"/>

  {icon_markup(sku["icon"], accent, ink)}

  <g font-family="Georgia, 'Iowan Old Style', 'Times New Roman', serif">
    <text x="32" y="310" fill="{ink}" font-size="26" font-weight="700">{sku["title"]}</text>
  </g>
  <g font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif">
    <text x="32" y="336" fill="{muted}" font-size="13">{sku["sub"]}</text>
    <rect x="32" y="354" width="118" height="22" rx="11" fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-opacity="0.45"/>
    <text x="91" y="369" fill="{accent}" font-size="10" font-weight="700" letter-spacing="1.2" text-anchor="middle">{sku["kind"].upper()}</text>
    <text x="32" y="416" fill="{muted}" font-size="11">Blank template cover</text>
    <text x="32" y="434" fill="{muted}" font-size="11" opacity="0.8">Not a live spreadsheet screenshot</text>
  </g>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for sku in SKUS:
        path = OUT / sku["file"]
        path.write_text(cover(sku), encoding="utf-8")
        print(f"wrote {path.relative_to(OUT.parent.parent)}")


if __name__ == "__main__":
    main()
