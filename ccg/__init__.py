#!/usr/bin/env python3
# coding: utf-8

"""
Imports
"""

import random

"""
Global variables
"""

CATEGORIES=None
FLAG_FORMAT='FLAG{flag_here}'
FLAG_FORMAT_FLAG='flag_here'
OUTPUT_DIR='/tmp/ccg/'

"""
Functions
"""


"""
gen_flag(): returns a generated flag containing given string, or random hex value
"""
def gen_flag(flag=None):
    if flag == None:
        flag = '{0:016x}'.format(random.randrange(pow(10,20)))
    return FLAG_FORMAT.replace(FLAG_FORMAT_FLAG, flag)


"""
Classes
"""

"""
Categories class:
    Initialize categories and corresponding sub-categories, add sub-categories and categories on the fly
"""

class Categories:


    """
    Categories.__init__(): initialize default values for categories
    """
    def __init__(self):
        self.categories = {
            'crypto': [ 'base64', 'rsa' ],
            'steg': [ 'hidden_message', 'lsb' ],
            'web': [ 'sqli', 'ssti', 'xxs' ]
        }


    """
    Categories.__str__(): averwrite class.to_string()
    """
    def __str__(self):
        return self.categories



"""
Challenge class:
    Initialize challenge, set variables (flag, difficulty, category...) and generate challenge
"""

class Challenge:


    """
    Challenge.__init__(): initialize default values for challenge
        User MUST update variable CATEGORIES before creating a challenge (ex: `CATEGORIES = Categories().categories`)
    """
    def __init__(self,category=None,sub_category=None,difficulty=None,flag=None,name=None):
        # TODO: Check for good type
        self.category = category
        self.sub_category = sub_category
        self.difficulty = difficulty
        self.flag = gen_flag(flag)
        self.name = name


    """
    Challenge.__str__(): overwrite class.to_string()
    """
    def __str__(self):
        # TODO: better print for a challenge
        return """=-= SOC: {} =-=
    - Category: {}
    - Sub-category: {}
    - Difficulty: {}
    - Flag: {}
=-= EOC =-=""".format(
                self.name,
                self.category,
                self.sub_category,
                self.difficulty,
                self.flag)


    """
    Challenge.generate(): generate challenge according to category, difficulty and output path
    """
    def generate(self):
        # TODO: generate a challenge
        print(self)
