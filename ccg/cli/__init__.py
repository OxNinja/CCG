import click

from ccg.models.challenge import Challenge
from ccg.models.cli import CCG_CLI as CLI


@click.group()
def cli():
    pass


@cli.command()
@click.argument("name", default=None)
@click.option("-c", "--category", "category")
@click.option("--description", "description")
@click.option("-s", "--sub-category", "sub_category")
@click.option("-d", "--difficulty", "difficulty")
@click.option("-f", "--flag", "flag")
@click.option("-p", "--points", "points", type=int)
@click.option("-o", "--out", "out")
@click.option("-i", "--files", "files")
def new(name, category, description, sub_category, difficulty, flag, points, out, files):
    if name is None: # prevent default name
        name = "Unnamed" # TODO: use a random name instead

    with CLI.spin(text=f"Creating new challenge '{name}'...") as spinner:
        
        # create a new challenge object
        challenge = Challenge(name=name,
            description=description,
            category=category,
            sub_category=sub_category,
            difficulty=difficulty,
            flag=flag,
            points=points,
            out=out,
            files=files)

        if challenge.generate():
            spinner.text = f"Challenge created! ({challenge.out})"
            spinner.ok(CLI.ok)
        else:
            spinner.text = f"Challenge creation failed"
            spinner.fail(CLI.fail)
