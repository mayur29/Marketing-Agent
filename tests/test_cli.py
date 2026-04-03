#!/usr/bin/env python3

"""Basic smoke tests for the campaign CLI tools."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent.parent


class CampaignCliSmokeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="marketing-agents-test-"))
        self.repo_copy = self.temp_dir / "repo"
        shutil.copytree(ROOT, self.repo_copy, ignore=shutil.ignore_patterns(".git"))

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def run_cmd(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            args,
            cwd=self.repo_copy,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_scaffold_campaign_creates_expected_files(self) -> None:
        result = self.run_cmd(
            "python3",
            "scripts/scaffold_campaign.py",
            "--slug",
            "website",
            "--product",
            "DISH Website",
            "--campaign-name",
            "DISH Website DE Demand Push",
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertTrue(
            (self.repo_copy / "knowledge" / "sample-campaign-website.md").exists()
        )
        self.assertTrue(
            (self.repo_copy / "outputs" / "website-cmo-output.md").exists()
        )
        self.assertTrue(
            (self.repo_copy / "outputs" / "website-analytics-plan.md").exists()
        )

    def test_run_workflow_reports_done_for_existing_campaign(self) -> None:
        result = self.run_cmd(
            "python3",
            "scripts/run_workflow.py",
            "--slug",
            "pos",
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("[DONE] campaign_input", result.stdout)
        self.assertIn("[DONE] analytics_plan", result.stdout)

    def test_scaffold_campaign_refuses_to_overwrite_without_force(self) -> None:
        first = self.run_cmd(
            "python3",
            "scripts/scaffold_campaign.py",
            "--slug",
            "website",
            "--product",
            "DISH Website",
            "--campaign-name",
            "DISH Website DE Demand Push",
        )
        self.assertEqual(first.returncode, 0, msg=first.stderr)

        second = self.run_cmd(
            "python3",
            "scripts/scaffold_campaign.py",
            "--slug",
            "website",
            "--product",
            "DISH Website",
            "--campaign-name",
            "DISH Website DE Demand Push",
        )
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("Refusing to overwrite existing file", second.stderr)


if __name__ == "__main__":
    unittest.main()
