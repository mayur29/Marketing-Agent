#!/usr/bin/env python3

"""Lightweight workflow runner for DISH campaign files.

This script does not generate marketing copy by itself.
It helps the team run the workflow consistently by:
- locating the campaign input file
- listing the expected workflow files
- showing what exists and what is still missing
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
        description="Show the workflow stages for a DISH campaign slug."
    )
    parser.add_argument(
        "--slug",
        required=True,
        help="Campaign slug used in filenames, for example: pos or reservation",
    )
    return parser.parse_args()


def expected_files(slug: str) -> list[tuple[str, Path]]:
    return [
        ("campaign_input", KNOWLEDGE_DIR / f"sample-campaign-{slug}.md"),
        ("cmo_output", OUTPUTS_DIR / f"{slug}-cmo-output.md"),
        ("research_output", OUTPUTS_DIR / f"{slug}-research-output.md"),
        ("messaging_output", OUTPUTS_DIR / f"{slug}-messaging-output.md"),
        ("campaign_brief", OUTPUTS_DIR / f"{slug}-campaign-brief-filled.md"),
        ("landing_page", OUTPUTS_DIR / f"{slug}-copy-landing-page.md"),
        ("email_sequence", OUTPUTS_DIR / f"{slug}-copy-email-sequence.md"),
        ("meta_ads", OUTPUTS_DIR / f"{slug}-copy-meta-ads.md"),
        ("analytics_plan", OUTPUTS_DIR / f"{slug}-analytics-plan.md"),
    ]


def print_stage(index: int, label: str, path: Path) -> None:
    status = "DONE" if path.exists() else "TODO"
    rel = path.relative_to(ROOT)
    print(f"{index}. [{status}] {label}: {rel}")


def main() -> int:
    args = parse_args()
    files = expected_files(args.slug)

    campaign_input = files[0][1]
    if not campaign_input.exists():
        print(
            f"Missing campaign input: {campaign_input.relative_to(ROOT)}",
            file=sys.stderr,
        )
        print(
            "Create it first with scripts/scaffold_campaign.py or add it manually.",
            file=sys.stderr,
        )
        return 1

    print(f"Workflow for slug: {args.slug}")
    print()
    print("Stage order:")
    for index, (label, path) in enumerate(files, start=1):
        print_stage(index, label, path)

    print()
    print("Recommended flow:")
    print("1. Confirm the campaign input is complete.")
    print("2. Produce strategy outputs: CMO, research, messaging, campaign brief.")
    print("3. Review claims, market, language, and tone before copy.")
    print("4. Produce copy outputs: landing page, email, Meta ads.")
    print("5. Finalize the analytics plan before launch.")

    remaining = [path for _, path in files if not path.exists()]
    print()
    if remaining:
        print("Next missing file:")
        print(f"- {remaining[0].relative_to(ROOT)}")
    else:
        print("All standard workflow files exist for this campaign.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
