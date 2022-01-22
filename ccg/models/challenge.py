from os import makedirs
from os.path import isdir, join
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
        self.flag = flag
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
        # create file structure
        try:
            output_path = join(self.out, self.id)
            # prevent overwriting existing challenge
            if not isdir(output_path):
                makedirs(output_path)
                challenge_config = ChallengeConfig(name=self.name, description=self.description, points=self.points, category=self.category, sub_category=self.sub_category, author="CCG", files=self.files)
                challenge_config.generate_file(join(output_path, "challenge.yml"))
            else:
                self.log(f"'{output_path}' already existing, exiting.")
                
        except Exception as err:
            self.log(f"error -> {err}")

        # create challenge.yml
        # create flag
        # create Dockerfile or docker-compose.yml
        # create src/
        
