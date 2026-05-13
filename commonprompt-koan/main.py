"""Possible entrypoint for koan."""

import click


@click.command()
def hello_world() -> None:
    """Print hello world."""
    print("Hello World!")


if __name__ == "__main__":
    hello_world()
