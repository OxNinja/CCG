from os import listdir, makedirs
from os.path import abspath, dirname, join, splitext
from random import choice, randint
from shutil import copytree

from ccg.models.challenge import Challenge
from ccg.models.challenge import DIFFICULTIES
from ccg.models.categories.category import Category


class ChallengeCode(Category):
    """
    """
    def __init__(self):
        pass

    @staticmethod
    def generate(challenge):
        # select a template directory for the difficulty
        templates_dir = join(dirname(abspath(__file__)), "templates", challenge.difficulty)
        # creates the files directory for the challenge
        challenge_files_dir = join(challenge.out, "files")
        makedirs(challenge_files_dir)
        
        # check difficulty for the category
        if challenge.difficulty == DIFFICULTIES[0]: # easy challenge
            # select a random template from the directory of the difficulty
            template = choice(listdir(templates_dir))
            challenge.log(f"using template {template}")
            template_path = join(templates_dir, template)

            # copy templates files in challenge
            copytree(template_path, challenge_files_dir, dirs_exist_ok=True)

            # add the challenge files to its config
            challenge.files.extend(listdir(challenge_files_dir))

            # generate challenge config file
            Category.create_config(challenge)

            # generate challenge flag file
            Category.create_flag(challenge)

            # replace template config placeholders with current values
            # the actual standard for an easy challenge is to replace the following by:
            #   $SALT   # replace with a random int between 1 and 50
            #   $FLAG   # replace with a string ("".join([chr(ord(x) + salt) for x in flag]))
            
            # generate the values
            salt = randint(1, 50)
            flag = "".join([chr(ord(x) + salt) for x in challenge.flag])

            # get challenge file regardless the extension (chall.ext)
            challenge_file = None
            for f in listdir(challenge_files_dir):
                if splitext(f)[0] == "chall":
                    challenge_file = join(challenge_files_dir, f)
                    break
            
            # if no chall file has been provided in the template
            if challenge_file is None:
                raise Exception(f"the challenge template does not include a 'chall.ext' file")

            # get file content
            data = open(challenge_file, "r").read()

            # replace with values
            data = data.replace("$SALT", str(salt))
            data = data.replace("$FLAG", flag)

            # write back to file
            open(challenge_file, "w").write(data)

            challenge.log("template config updated with current values")
        else: # bad difficulty input
            raise Exception(f"the choosen difficulty ({challenge.difficulty}) is not compatible with the current category ({challenge.sub_category})")