from importlib import import_module
from os import makedirs
from os.path import isdir, join
from random import randrange
from slugify import slugify
from tempfile import gettempdir
from time import time

from ccg.models.challenge_config import ChallengeConfig


class Challenge:
    def __init__(self, name, description, category, sub_category, difficulty, flag, points, out, files):
        self.name = name
        # generate a 'unique' id for a challenge
        self.id = f"{slugify(self.name)}-{str(int(time()))[5:]}"
        self.description = description
        self.category = category
        self.sub_category = sub_category
        self.difficulty = difficulty
        if flag is not None:
            self.flag = flag
        else:
            self.flag = str(hex(randrange(0x100000000000, 0xffffffffffff)))[2:] # random hex value of 12 chars, faster than a hash generation
        self.points = points
        self.files = files
        # setup challenge output directory
        if out is not None and isdir(out):
            self.out = out
        else:
            self.out = gettempdir()
            self.log(f"'{out}' is not a directory, using '{self.out}' instead.")
 
    def __repr__(self):
        return f"""{self.name} ({self.difficulty}: {self.points}) [{self.category}, {self.sub_category}]
    {self.flag}
    {self.out}"""

    def log(self, message):
        print(f"\r\n[LOG (challenge {self.name})] {message}")

    def generate(self):
        """read categories/ directory containing all the challenges generation methods
        and call `self.category`.generate() method
        this method can thus be very custom and able to generate a challenge.yml but also a Dockerfile if needed including the sources of the challenge
        """
        # create file structure
        try:
            self.out = join(self.out, self.id)
            # prevent overwriting existing challenge
            # should use mkstemp in the future, preventing race conditions and other bad stuff
            if not isdir(self.out):
                makedirs(self.out)

                # TODO: call challenge category generate method
                # should check if module exists before importing it
                module = import_module(f"ccg.models.categories.{self.category}.{self.sub_category}")
                # the class name follows: ChallengeSubcategoryname
                class_name = f"Challenge{self.sub_category.capitalize()}"
                # generate the challenge using the custom method of this category
                challenge_class = getattr(module, class_name)
                challenge_class.generate(self)

            else:
                self.log(f"'{self.out}' already existing, exiting.")
                
        except Exception as err:
            self.log(f"error -> {err}")
