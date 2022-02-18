from base64 import b64encode as b64e
from os import makedirs
from os.path import join
from random import randint

from ccg.models.challenge import Challenge
from ccg.models.challenge import DIFFICULTIES
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

        # check difficulty for the category
        if challenge.difficulty == DIFFICULTIES[0]: # easy challenge
            # choose encoding
            # for the moment this is bad code but one day it will be better
            r = randint(0, 2) # 3 types
            match r:
                case 0: # binary
                    encoded = " ".join([bin(ord(x))[2:].zfill(7) for x in challenge.flag])
                    challenge.log("binary encoding")
                case 1: # hex
                    encoded = " ".join([hex(ord(x)) for x in challenge.flag])
                    challenge.log("hex encoding")
                case 2: # base64
                    encoded = b64e(challenge.flag.encode()).decode()
                    challenge.log("base64 encoding")
                case _:
                    raise Exception("error occured during the challenge generation process (ChallengeEncoding.generate())")
            challenge_file = f"{challenge.name}.txt"
            # check if files are existing for the challenge
            if challenge.files is None:
                challenge.files = []
            challenge.files.append(challenge_file)
            # generate challenge.yml
            Category.create_config(challenge)
            # create flag file
            Category.create_flag(challenge)

            # create the files directory
            challenge_files_dir = join(challenge.out, "files")
            makedirs(challenge_files_dir)

            with open(join(challenge_files_dir, challenge_file), 'w+') as file:
                file.write(encoded)
            
        else: # bad difficulty input
            raise Exception(f"the choosen difficulty ({challenge.difficulty}) is not compatible with the current category ({challenge.sub_category})")

