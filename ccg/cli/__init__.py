import click
import sys
from os.path import isdir
from tempfile import gettempdir
from yaspin import yaspin
from yaspin.spinners import Spinners
from ccg.category.category import ChallengeCategory
from ccg.challenge.challenge import Challenge
from ccg.models import CATEGORIES, SPIN_FAIL, SPIN_OK
from ccg.utility import is_slug


@click.group()
def cli():
    pass


# TODO: add help messages for options
@cli.command()
@click.argument("name", type=str, default=None, nargs=1, required=False)
@click.option("-c", "--category", "category", type=str, default=None, nargs=1, multiple=False)
@click.option("-d", "--difficulty", "difficulty", type=click.IntRange(1, 3, clamp=True), default=None, nargs=1, multiple=False)
@click.option("-f", "--flag", "flag", type=str, default=None, nargs=1, multiple=False)
@click.option("-o", "--outdir", "outdir", type=str, default=gettempdir(), nargs=1, multiple=False)
@click.option("-p", "--points", "points", type=int, default=10, nargs=1, multiple=False)
@click.option("-s", "--sub-category", "sub_category", type=str, default=None, nargs=1, multiple=False)
def new(name, flag, category, sub_category, difficulty, outdir, points):
    """Creates one or more new challenge with the given arguments and names
    If attributes are left to None, random will be applied
    """
    with yaspin(Spinners.line, text="Creating new challenge...") as spinner:
        # Check for challenge's name
        if name is not None:
            if not is_slug(name):
                spinner.text = f"'{name}' is not a valid challenge name"
                spinner.fail(SPIN_FAIL)
                sys.exit(1)

        # Check for challenge's category
        if category is not None:
            if category not in CATEGORIES:
                spinner.text = f"'{category}' is not a valid challenge category"
                spinner.fail(SPIN_FAIL)
                sys.exit(1)
            # Check for challenge's sub-category
            elif sub_category is not None:
                if sub_category not in CATEGORIES[category]:
                    spinner.text = f"'{sub_category}' is not a valid sub-category for category '{category}'"
                    spinner.fail(SPIN_FAIL)
                    sys.exit(1)

        # Check if sub_category but no category specified
        # This check is here to prevent sub-category name collision
        if category is None and sub_category is not None:
            spinner.text = "You can't specify a sub-category without a category"
            spinner.fail(SPIN_FAIL)
            sys.exit(1)

        # Check if given outdir is valid
        if not isdir(outdir):
            spinner.text = f"'{outdir}' is not a valid directory"
            spinner.fail(SPIN_FAIL)
            sys.exit(1)

        # Create a new Challenge object with the given arguments
        # Yes, you can have negative points challenges :innocent:
        chall = Challenge(name=name, flag=flag, category=category,
                          sub_category=sub_category, difficulty=difficulty, path=outdir, points=points)
        # Generating the challenge within a nice wrapper
        chall.generate()

        spinner.text = f"Challenge '{chall.name}' sucessfully created!"
        spinner.ok(SPIN_OK)
