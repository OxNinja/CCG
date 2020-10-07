#!/usr/bin/env python3
# coding: utf-8

"""
Global variables
"""

OUTPUT_DIR='/tmp/ccg/'

"""
Challenge class:
    Initialize challenge, set variables (flag, difficulty, category...) and generate challenge
"""

class Challenge:


    """
    __init__(): initialize default values for challenge
    """
    def __init__(self,category=None,sub_category=None,difficulty=None,flag=None,name=None):
        # TODO: Check for good type
        self.category = category
        self.sub_category = sub_category
        self.difficulty = difficulty
        self.flag = flag
        self.name = name


    """
    __str__(): overwrite class.to_string()
    """
    def __str__(self):
        return """=-= Challenge {} =-=
        - Category: {}
        - Sub-category: {}
        - Difficulty: {}
        - Flag: {}""".format(
                self.name,
                self.category,
                self.sub_category,
                self.difficulty,
                self.flag)


    """
    generate(): generate challenge according to category, difficulty and output path
    """
    def generate(self):
        print(self)
        return 0
