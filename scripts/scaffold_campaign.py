#!/usr/bin/env python3

"""Scaffold a new DISH campaign workflow.

This creates:
- a product-specific sample campaign file in knowledge/
- the standard workflow output files in outputs/

It is intentionally lightweight so the team can start from consistent files
and then fill them in manually or with agent help.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / "knowledge"
OUTPUTS_DIR = ROOT / "outputs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold a new DISH campaign workflow."
    )
    parser.add_argument(
        "--slug",
        required=True,
        help="Short slug used in filenames, for example: kiosk or website-fr",
    )
    parser.add_argument(
        "--product",
        required=True,
        help="Product name, for example: DISH Website",
    )
    parser.add_argument(
        "--campaign-name",
        required=True,
        help="Human-readable campaign name",
    )
    parser.add_argument(
        "--market",
        default="Germany",
        help="Campaign market or country",
    )
    parser.add_argument(
        "--language",
        default="German",
        help="Primary campaign language",
    )
    parser.add_argument(
        "--tone",
        default="DE `Sie`",
        help="Tone register, for example: DE `Sie`",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite files if they already exist",
    )
    return parser.parse_args()


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sample_campaign_content(args: argparse.Namespace) -> str:
    return f"""# Sample Campaign

## Campaign Name

{args.campaign_name}

## Business Goal

[Define the business goal for {args.product}.]

## Target Audience

- [Audience segment 1]
- [Audience segment 2]
- [Audience segment 3]

## Offer

{args.product}

## Core Problem

[Describe the main operator pain point.]

## Main Promise

[Describe the approved primary value promise.]

## Proof Themes

- [Approved proof point 1]
- [Approved proof point 2]
- [Approved proof point 3]

## Market and Language

- {args.market}
- {args.language}
- {args.tone}

## Suggested Channels

- landing page
- email
- Meta ads
- sales enablement follow-up

## Primary CTA

Book a demo

## Primary KPI

Qualified demo requests

## Secondary KPIs

- landing page conversion rate
- email click-through rate
- cost per qualified lead
- sales follow-up rate

## Notes

[Add campaign-specific notes, risks, and constraints.]
"""


def generic_output_content(title: str, args: argparse.Namespace) -> str:
    return f"""# {title}

## Campaign

{args.campaign_name}

## Market and Language

- market: {args.market}
- primary language: {args.language}
- tone register: {args.tone}

## Draft

[Fill this section using the corresponding agent workflow.]
"""


def campaign_brief_content(args: argparse.Namespace) -> str:
    return f"""# Campaign Brief

## Campaign Name

{args.campaign_name}

## Objective

- [Define the business objective]

## Target Audience

- [Audience segment 1]
- [Audience segment 2]

## Market and Language

- Country or market: {args.market}
- Primary language: {args.language}
- Tone register: {args.tone}

## Offer

- {args.product}

## Core Message

- [Primary campaign message]

## Supporting Proof

- [Approved proof point 1]
- [Approved proof point 2]

## Funnel Stage

- Consideration to conversion

## Channels

- Landing page
- Email
- Meta ads
- Sales follow-up

## Assets Needed

- landing page
- email sequence
- Meta ad variants
- sales follow-up summary sheet

## CTA

- Demo buchen

## KPIs

- Primary KPI: qualified demo requests
- Secondary KPIs: landing page conversion rate, email click-through rate, cost per qualified lead

## Timeline

- Start date: to be defined
- Launch date: to be defined

## Risks and Constraints

- [Approved claims only]

## Experiments

- [Angle test 1]
- [Angle test 2]

## Approvals Required

- human review before launch

## Notes

- [Implementation notes]

## Approval Status

- Draft

## Handoff Package

- Next agent: Copywriter Agent
- Expected output: landing page, email, and paid drafts
"""


def analytics_plan_content(args: argparse.Namespace) -> str:
    return f"""# Analytics and Optimization Plan

## Campaign

{args.campaign_name}

## Market and Language

- market: {args.market}
- primary language: {args.language}
- tone register: {args.tone}

## Performance Summary

[Define how this campaign will be measured.]

## KPI Status Framework

### Primary KPI

- qualified demo requests

### Secondary KPIs

- landing page conversion rate
- email click-through rate
- cost per qualified lead

### Leading Indicators

- hero-to-CTA click rate
- form completion rate
- ad click-through rate

## Recommended Next Actions

- [Experiment 1]
- [Experiment 2]

## Reporting Cadence

- pre-launch measurement review
- week 1 review
- week 2 optimization review

## Next Handoff

Send learnings back to:

- CMO Agent
- Messaging and Positioning Agent
- Campaign Strategist Agent
"""


def main() -> int:
    args = parse_args()

    knowledge_path = KNOWLEDGE_DIR / f"sample-campaign-{args.slug}.md"
    output_paths = {
        OUTPUTS_DIR / f"{args.slug}-cmo-output.md": generic_output_content(
            "CMO Output", args
        ),
        OUTPUTS_DIR / f"{args.slug}-research-output.md": generic_output_content(
            "Market Research Output", args
        ),
        OUTPUTS_DIR / f"{args.slug}-messaging-output.md": generic_output_content(
            "Messaging and Positioning Output", args
        ),
        OUTPUTS_DIR / f"{args.slug}-campaign-brief-filled.md": campaign_brief_content(
            args
        ),
        OUTPUTS_DIR / f"{args.slug}-copy-landing-page.md": generic_output_content(
            "Landing Page Draft", args
        ),
        OUTPUTS_DIR / f"{args.slug}-copy-email-sequence.md": generic_output_content(
            "Email Sequence Draft", args
        ),
        OUTPUTS_DIR / f"{args.slug}-copy-meta-ads.md": generic_output_content(
            "Meta Ad Copy Draft", args
        ),
        OUTPUTS_DIR / f"{args.slug}-analytics-plan.md": analytics_plan_content(args),
    }

    try:
        write_file(knowledge_path, sample_campaign_content(args), args.force)
        for path, content in output_paths.items():
            write_file(path, content, args.force)
    except FileExistsError as exc:
        print(exc, file=sys.stderr)
        print("Use --force to overwrite existing files.", file=sys.stderr)
        return 1

    print(f"Created: {knowledge_path.relative_to(ROOT)}")
    for path in output_paths:
        print(f"Created: {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
