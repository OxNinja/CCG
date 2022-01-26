from os.path import join

from ccg.models.challenge import Challenge
from ccg.models.categories.category import Category


class ChallengeEncoding(Category):
    """Generate a crypto/encoding challenge
    easy:
        basic encoding (base 2, 16, 32, 64, rot13...)
        the challenge is generated into a file named `{challenge.name}.txt` in the `./files/` folder
    """
    def __init__(self, challenge):
        super().__init__(challenge)

    @staticmethod
    def generate(challenge):
        # TODO: test this method
        challenge_file = f"{challenge.name}.txt"
        challenge.files.append(challenge_file)
        # generate challenge.yml
        Category.create_config(challenge)
        # create flag file
        Category.create_flag(challenge)
        # generate challenge file
        encoded = flag
        with open(join(challenge.out, 'files', challenge_file), 'w') as file:
            file.write(encoded)
        
