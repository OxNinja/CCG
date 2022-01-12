class Challenge:
    def __init__(self, name, description, category, sub_category, difficulty, flag, points, out):
        self.name = name
        self.description = description
        self.category = category
        self.sub_category = sub_category
        self.difficulty = difficulty
        self.flag = flag
        self.points = points
        self.out = out

    def __repr__(self):
        return f"""{self.name} ({self.difficulty}: {self.points}) [{self.category}, {self.sub_category}]
    {self.flag}
    {self.out}"""