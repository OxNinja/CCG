import click
from yaspin import yaspin
from yaspin.spinners import Spinners

from ccg.category.category import ChallengeCategory
from ccg.challenge.challenge import Challenge
from ccg.models import SPIN_FAIL, SPIN_OK, CATEGORIES
from ccg.utility import is_slug


@click.group()
def cli():
    pass


# TODO: add help messages for options
@cli.command()
@click.argument("name", type=str, default=None, nargs=1, required=False)
@click.option("-f", "--flag", "flag", type=str, default=None, nargs=1, multiple=False)
@click.option("-c", "--category", "category", type=str, default=None, nargs=1, multiple=False)
@click.option("-s", "--sub-category", "sub_category", type=str, default=None, nargs=1, multiple=False)
@click.option("-d", "--difficulty", "difficulty", type=click.IntRange(1, 3, clamp=True), default=None, nargs=1, multiple=False)
def new(name, flag, category, sub_category, difficulty):
    """Creates one or more new challenge with the given arguments and names
    If attributes are left to None, random will be applied
    """
    with yaspin(Spinners.line, text="Creating new challenge...") as spinner:

        # Check for challenge's name
        if name is not None:
            if not is_slug(name):
                spinner.text = f"'{name}' is not a valid challenge name"
                spinner.fail(SPIN_FAIL)
                exit()

        # Check for challenge's category
        if category is not None:
            if category not in CATEGORIES:
                spinner.text = f"'{category}' is not a valid challenge category"
                spinner.fail(SPIN_FAIL)
                exit()
            # Check for challenge's sub-category
            elif sub_category is not None:
                if sub_category not in CATEGORIES[category]:
                    spinner.text = f"'{sub_category}' is not a valid sub-category for category '{category}'"
                    spinner.fail(SPIN_FAIL)
                    exit()
        
        # Check if sub_category but no category specified
        if category is None and sub_category is not None:
            spinner.text = "You can't specify a sub-category without a category"
            spinner.fail(SPIN_FAIL)
            exit()
        
        # Create a new Challenge object with the given arguments
        chall = Challenge(name=name, flag=flag, category=category, sub_category=sub_category, difficulty=difficulty)
        # Generating the challenge within a nice wrapper
        ChallengeCategory.generating(chall)

        spinner.text = f"Challenge '{chall.name}' sucessfully created!"
        spinner.ok(SPIN_OK)