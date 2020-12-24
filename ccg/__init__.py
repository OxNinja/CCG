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
    """Returns an md5 hash created with two initializers parameters (text + salt).
        :param a: By default the name of a challenge we want to generate an id for
        :type a: str or None
        :param b: By default the flag of the challenge we want to generate an id for
        :type b: str
        :return: A string in the form of an md5 hash
        :rtype: str
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
    """Returns a generated flag containing given string, or random hex value.
        :param flag: The flag you want to use for a challenge, or let the programm generate one for you, defaults to None
        :type flag: str
        :return: The flag of the challenge according to both global variables `FLAG_FORMAT` and `FLAG_FORMAT_FLAG`
        :rtype: str
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
    """Prints custom error according to CCG.
        :param problem: The content of the problem encoutered during execution
        :type problem: str
    """

    def __init__(self, problem):
        """Constructor method
        """
        super().__init__(f"[CCG] An error occured: {problem}")


class Categories:
    """Initializes categories and corresponding sub-categories.
    """

    def __init__(self):
        """Constructor method
        """
        self.categories = {
            'crypto': ['base64', 'rsa'],
            'steg': ['hidden_message', 'lsb'],
            'web': ['sqli', 'ssti', 'xss']
        }

    def __str__(self):
        """String method
        """
        return self.categories


class Challenge:
    """Initializes a challenge, set corresponding variables (`flag`, `difficulty`, `category`...), check things and generate challenge.
        :param category: The wanted category of the challenge. Defaults to None
        :type category: str
        :param sub_category: The wanted sub-category of the challenge. Defaults to None
        :type sub_category: str
        :param difficulty: The wanted difficulty level of the challenge. Defaults to None
        :type difficulty: int
        :param flag: The wanted flag of the challenge. Defaults to None
        :type flag: str, optional
        :param name: The wanted name of the challenge, will be used later for referencing to a challenge using its name or id. Defaults to None
        :type name: str, optional
    """
    # TODO: select a random sub-category if None and update the desc in docstring when done

    def __init__(self, category=None, sub_category=None, difficulty=None, flag=None, name=None):
        """Constructor method
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
        """String method
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
        """Checks if challenge is okay (ie. if category exists...)
                :raises CCGError: A generic error type, with self-explaining details of the encoutered problem
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
        """Modify a challenge's category and sub-category, then checks if it is okay
                :param category: The target category for the challenge
                :type category: str
                :param sub_category: The terget sub-category for the challenge
                :type sub_category: str
        """
        self.category = category
        self.sub_category = sub_category
        self.check()

    def random_category(self):
        """Modfify a challenge's category and sub-category for a random correct value according to the global variable `CATEGORIES`
        """
        global CATEGORIES
        r_category = random.randrange(len(CATEGORIES))
        r_sub_category = random.randrange(
            len(list(CATEGORIES.values())[r_category]))
        self.set_category(list(CATEGORIES.keys())[r_category], list(
            CATEGORIES.values())[r_category][r_sub_category])

    def generate(self):
        """Generates challenge according to category, difficulty and output path
        """
        # TODO: generate a challenge: call the right function in Challenges.py script according to challenge's sub_category
        print(self)
