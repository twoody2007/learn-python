###############################################################################
####    imports
###############################################################################
# standard library imports
import asyncio
from typing import Optional

# third party
import click


# your project!
from .doing_things import do_thing as _do_thing



###############################################################################
####    helper functions
###############################################################################
async def _do_example(message: Optional[str]) -> None:
    if message is not None:
        print(f"Here's an example of printing program input: {message}")
    else:
        print(f"This example doesn't have anything extra.")



###############################################################################
####    cli hooks
###############################################################################
@click.group()
def cli():
    click.echo("Running a learn-python command...")


@cli.command()
@click.option(
    "--message",
    type=str,
    help=f"Prints and example message, if supplied",
)
def example(message: str) -> None:
    """
    This is an example function for using click
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_do_example(message))
    return None


@cli.command()
def do_thing():
    """
    This shows that we can call the same function from both a CLI and a webserver!
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_do_thing())
    return None