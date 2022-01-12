from os import makedirs
from os.path import isdir, join
from slugify import slugify
from tempfile import gettempdir
from time import time
from yaml import dump as yaml_dump

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
                """
                name: chall
                description: blablabla
                points: 10
                category: pwn
                author: 0xLaPoutre
                files:
                - chall.jpg
                containers:
                - image: nginx:latest
                    ports:
                    - proto: TCP
                        port: 80
                    - proto: UDP
                        port: 31337
                """
                challenge_config = {
                    "name": self.name,
                    "description": self.description,
                    "points": self.points,
                    "category": self.category,
                    "author": "CCG",
                    "files": self.files
                }
                with open(join(output_path, "challenge.yml"), 'w') as file:
                    yaml_content = yaml_dump(challenge_config)
                    file.write(yaml_content)
            else:
                self.log(f"'{output_path}' already existing, exiting.")
                
        except Exception as err:
            self.log(f"error -> {err}")

        # create challenge.yml
        # create flag
        # create Dockerfile or docker-compose.yml
        # create src/
        
