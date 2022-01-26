"""Console script for gh_release."""
import click

from . import __version__


# -----------------------------------------------------------------------
@click.command()
@click.version_option(version=__version__)
def gh_release():
    """gh_release dummy command"""
    print("Hello world")


# -----------------------------------------------------------------------
