"""Possible entrypoint for koan."""

import click


@click.command()
def koan() -> None:
    """Print hello world."""
    print("Hello World!")


if __name__ == "__main__":
    koan()
