"""Console script for gh_release."""
import click


# -----------------------------------------------------------------------
@click.command()
@click.version_option()
def gh_release():
    """gh_release dummy command"""
    print("Hello world")


# -----------------------------------------------------------------------
