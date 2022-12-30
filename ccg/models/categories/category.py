""" Template file for a challenge category
Just copy/paste it to start a new category
"""

from os.path import join

from ccg.models.challenge import Challenge
from ccg.models.challenge_config import ChallengeConfig


class Category:
    def __init__(self):
        # nothing here, only static methods
        pass

    @staticmethod
    def create_config(challenge):
        """Create the challenge.yml config file
        Uses the ChallengeConfig class in order to dump the config into a yaml file
        """
        # generate the yaml config from object attributes
        challenge_config = ChallengeConfig(name=challenge.name,
                description=challenge.description,
                points=challenge.points,
                category=challenge.category,
                sub_category=challenge.sub_category,
                author="CCG",
                files=challenge.files)
        # create the challenge.yml file
        challenge_config.generate_file(join(challenge.out, "challenge.yml"))

    @staticmethod
    def create_flag(challenge):
        """Create the flag file (flag.txt), overwriting if already existing
        This file contains the flag (validation password) of the challenge
        """
        with open(join(challenge.out, "flag.txt"), "w") as file:
            file.write(challenge.flag)

    @staticmethod
    def generate(challenge):
        """Need to override this method for each challenge categories
        """
        pass
