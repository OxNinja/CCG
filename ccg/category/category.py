import sys
from yaspin import yaspin
from yaspin.spinners import Spinners

from ccg.challenge.challenge import Challenge
from ccg.models import DIFFICULTIES, SPIN_FAIL, SPIN_OK


class ChallengeCategory:
    """Generic Category class, will be used by other categories to generate source code, files... for a given challenge
    If you want to create a custom category, just add it to `../models/category.py`, inherit this class and override the `generate()` method with your own code, adjust the difficulties if needed
    """

    # By default we accept all difficulties
    ACCEPTABLE_DIFFICULTY = list(DIFFICULTIES.keys())

    @classmethod
    def generating(cls, challenge: Challenge) -> None:
        """Wrapper to the `generate()` method, this method checks if the challenge can be generated and then calls the `generate()` method

        :param challenge: The challenge to generate
        """
        print(challenge.difficulty, cls.ACCEPTABLE_DIFFICULTY)
        with yaspin(Spinners.line, text=f"[{challenge.name}] Generating files...") as spinner:
            # TODO: Check if difficulty is acceptable
            # if challenge.difficulty not in cls.ACCEPTABLE_DIFFICULTY:
            #    spinner.text = f"Difficulty '{challenge.difficulty}' is not accepted by the category '{challenge.sub_category}' ({challenge.category})"
            #    spinner.fail(SPIN_FAIL)
            #    sys.exit(1)

            # Actually generating the challenge
            cls.generate(challenge)

            spinner.text = f"[{challenge.name}] Files generated successfully!"
            spinner.ok(SPIN_OK)

    @classmethod
    def generate(cls, challenge: Challenge) -> None:
        """Creates the correct files for a challenge

        :param challenge: The challenge to generate
        """
        # Empty method, implement your own for a custom category
        sys.exit()
