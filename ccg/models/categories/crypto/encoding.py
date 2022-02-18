from os import makedirs
from os.path import join

from ccg.models.challenge import Challenge
from ccg.models.categories.category import Category


class ChallengeEncoding(Category):
    """Generate a crypto/encoding challenge
    easy:
        basic encoding (base 2, 16, 32, 64, rot13...)
        the challenge is generated into a file named `{challenge.name}.txt` in the `./files/` folder
    """

    def __init__(self):
        pass

    @staticmethod
    def generate(challenge):
        # TODO: test this method
        challenge_file = f"{challenge.name}.txt"
        # check if files are existing for the challenge
        if challenge.files is None:
            challenge.files = []
        challenge.files.append(challenge_file)
        # generate challenge.yml
        Category.create_config(challenge)
        # create flag file
        Category.create_flag(challenge)
        # generate challenge file
        encoded = challenge.flag

        # create the files directory
        challenge_files_dir = join(challenge.out, "files")
        makedirs(challenge_files_dir)

        with open(join(challenge_files_dir, challenge_file), 'w+') as file:
            file.write(encoded)
        
