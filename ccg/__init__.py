#!/usr/bin/env python3
# coding: utf-8

"""
Imports
"""

import hashlib
import random
import time

"""
Global variables
"""

CATEGORIES = None
FLAG_FORMAT = 'FLAG{flag_here}'
FLAG_FORMAT_FLAG = 'flag_here'
OUTPUT_DIR = '/tmp/ccg/'

"""
Functions
"""
# TODO: get_challenge_by_id and name or something


def gen_id(a, b):
    """
    gen_id(a, b): returns an md5 hash created with two initializers parameters (text + salt)
    """
    text = str(time.time())
    # TODO: check types of a and b
    if a and b:
        text += a + b
    elif b and not a:
        text += b
    elif a and not b:
        # should never happen but just to be sure you know
        text += a

    uid = hashlib.md5(text.encode()).hexdigest()

    return uid


def gen_flag(flag=None):
    """
    gen_flag(): returns a generated flag containing given string, or random hex value
    """
    global FLAG_FORMAT
    global FLAG_FORMAT_FLAG
    if not flag:
        flag = '{0:016x}'.format(random.randrange(pow(10, 20)))
    return FLAG_FORMAT.replace(FLAG_FORMAT_FLAG, flag)


"""
Classes
"""


class CCGError(Exception):
    """
    Errors class:
            Print errors according to CCG
    """

    def __init__(self, problem):
        """
        CCGError.__init__(problem): calls an exception with custom text when raised
        """
        super().__init__(f"[CCG] An error occured: {problem}")


class Categories:
    """
    Categories class:
            Initialize categories and corresponding sub-categories, add sub-categories and categories on the fly
    """

    def __init__(self):
        """
        Categories.__init__(): initialize default values for categories
        """
        self.categories = {
            'crypto': ['base64', 'rsa'],
            'steg': ['hidden_message', 'lsb'],
            'web': ['sqli', 'ssti', 'xss']
        }

    def __str__(self):
        """
        Categories.__str__(): overwrite class.to_string()
        """
        return self.categories


class Challenge:
    """
    Challenge class:
            Initialize challenge, set variables (flag, difficulty, category...), check things and generate challenge
    """

    def __init__(self, category=None, sub_category=None, difficulty=None, flag=None, name=None):
        """
        Challenge.__init__(): initialize default values for challenge
                User must update variable CATEGORIES before creating a challenge (ex: `CATEGORIES = Categories().categories`) if needed
        """
        global CATEGORIES
        if not CATEGORIES:
            CATEGORIES = Categories().categories
        # TODO: Check for good types (if category is a correct string, if difficulty is a correct integer...)
        self.category = category
        self.sub_category = sub_category
        self.difficulty = difficulty
        self.flag = gen_flag(flag)
        self.name = name
        self.id = gen_id(self.name, self.flag)

        # Check if challenge is okay
        self.check()

    def __str__(self):
        """
        Challenge.__str__(): overwrite class.to_string()
        """
        # TODO: better print for a challenge
        return f"""=-= SOC: {self.name} =-=
    - ID: {self.id}
    - Category: {self.category}
    - Sub-category: {self.sub_category}
    - Difficulty: {self.difficulty}
    - Flag: {self.flag}
=-= EOC =-="""

    def check(self):
        """
        Challenge.check():
                Checks if challenge is okay (ie. if category exists...)
        """
        global CATEGORIES
        # Check for category
        if not self.category in CATEGORIES:
            raise CCGError(f"challenge's category '{self.category}' not found")

        # Check for sub-category
        if not self.sub_category in CATEGORIES[self.category]:
            raise CCGError(
                f"challenge's sub-category '{self.sub_category}' not found in category '{self.category}'")

    def set_category(self, category, sub_category):
        """
        Challenge.set_category(category, sub_category):
                Modify a challenge's category and sub-category, then checks if it is okay
        """
        self.category = category
        self.sub_category = sub_category
        self.check()

    def random_category(self):
        """
        Challenge.random_category():
                Modfify a challenge's category and sub-category for a random correct value
        """
        r_category = random.randrange(len(CATEGORIES))
        r_sub_category = random.randrange(
            len(list(CATEGORIES.values())[r_category]))
        self.set_category(list(CATEGORIES.keys())[r_category], list(
            CATEGORIES.values())[r_category][r_sub_category])

    def generate(self):
        """
        Challenge.generate(): generate challenge according to category, difficulty and output path
        """
        # TODO: generate a challenge: call the right function in Challenges.py script according to challenge's sub_category
        print(self)
