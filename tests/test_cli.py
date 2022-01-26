#!/usr/bin/env python
"""Tests for `gh_release` package."""
import re

from click.testing import CliRunner

from gh_release.cli import gh_release as app

runner = CliRunner()


def test_cli_help():
    """Test the CLI."""
    help_result = runner.invoke(app, ["--help"])
    assert help_result.exit_code == 0
    assert "gh_release dummy command" in help_result.output  # it gets the file wrong
    assert help_result.exit_code == 0
    assert re.search(r"--help \s+ Show this message and exit.", help_result.output)


def test_cli_version():
    """Test the CLI."""
    version_result = runner.invoke(app, ["--version"])
    assert version_result.exit_code == 0
    assert "version 0.4.0" in version_result.output
