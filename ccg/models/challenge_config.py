from yaml import dump


class ChallengeConfig:
    def __init__(self, name=None, description=None, points=None, category=None, sub_category=None, files=None, author=None, containers=None):
        self.name = name
        self.description = description
        self.points = points
        self.category = category
        self.sub_category = sub_category
        self.files = files
        self.author = author
        self.containers = containers

    def generate_file(self, file_path):
        config = {
                "name": self.name,
                "description": self.description,
                "points": self.points,
                "category": self.category,
                "sub_category": self.sub_category,
                "files": self.files,
                "author": self.author,
                "containers": self.containers,
                }

        content = dump(config)
        with open(file_path, "w") as file:
            file.write(content)
