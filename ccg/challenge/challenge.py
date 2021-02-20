from os.path import join


class Challenge():
    """Creates a Challenge object used for data manipulation and challenge creation

    :param name: The challenge's name
    :type name: str
    :param flag: The challenge's flag
    :type flag: str
    :param category: The challenge's category
    :type category: str
    :param sub_category: The challenge's sub-category
    :type sub_category: str
    :param difficulty: The challenge's difficulty
    :type difficulty: int
    """

    def __init__(self, name=None, flag=None, category=None, sub_category=None, difficulty=None, path=None, points=None):
        """Constructor method
        """
        # TODO: initiate None values to random values
        # TODO: initiate an ID to a challenge, and use it in Challenge.path
        self.name = name
        self.flag = flag
        self.category = category
        self.sub_category = sub_category
        self.difficulty = difficulty
        self.points = points
        self.path = join(path, self.name)

    def __str__(self):
        """String method
        """
        return f"""\nChallenge '{self.name}' ({self.points}pts):
        {self.flag}
        {self.category} ({self.sub_category}) [{self.difficulty}]
        '{self.path}'
        """

    def generate(self):
        """Generates the challenge, ie. generates the corresponding source code, files, Dockerfile...
        """
