#!/usr/bin/env python3
# coding: utf-8

"""
Imports
"""

import base64
import hashlib
import os
import platform
import random
import string
import tempfile
import time

"""
Global variables
"""
# TODO: inconsistent use of UPPER and lower for global variables

CATEGORIES = None
FLAG_FORMAT = 'FLAG{flag_here}'
FLAG_FORMAT_FLAG = 'flag_here'
OS_SEP = '\\' if platform.system() == 'Windows' else '/'
OUTPUT_DIR = tempfile.gettempdir() + f'{OS_SEP}ccg{OS_SEP}'
challenges = list()
CHALLENGE = {"OUT": "files", "SOURCE": "src", "CONFIG": "challenge.yml"}

# Setup the system
try:
    os.mkdir(OUTPUT_DIR)
except Exception as e:
    print(e)

"""
Functions
"""


def get_challenge_by_id(id):
    """Returns one challenge with the given id or None if not found.

    :param id: The id of the challenge you want to get
    :type id: str
    :return: The challenge with the given id or None if not found
    :rtype: Challenge or None
    """
    global challenges
    for x in challenges:
        if x.id == id:
            return x
    return None


def get_challenges_by_name(name):
    """Returns a list containing the challenges whith the given name.

    :param name: The name of the challenge you want to get
    :type name: str
    :return: A list containing the challenges with the given name
    :rtype: list
    """
    global challenges
    chall_list = list()
    for x in challenges:
        if x.name == name:
            chall_list.append(x)
    return chall_list


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
            'crypto': ['encoding', 'rsa'],
            'steg': ['hidden_message', 'lsb'],
            'web': ['sqli', 'ssti', 'xss']
        }

    def __str__(self):
        """String method
        """
        return self.categories


class Challenge:
    """Initializes a challenge, set corresponding variables (`flag`, `difficulty`, `category`...), add it to the global challenge list, check things and generate the challenge.

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
        global challenges
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
        # Add the challenge to the global list
        challenges.append(self)

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
        """Modify a challenge's category and sub-category, then checks if it is okay.

        :param category: The target category for the challenge
        :type category: str
        :param sub_category: The terget sub-category for the challenge
        :type sub_category: str
        """
        self.category = category
        self.sub_category = sub_category
        self.check()

    def random_category(self):
        """Modfify a challenge's category and sub-category for a random correct value according to the global variable `CATEGORIES`.
        """
        global CATEGORIES
        r_category = random.randrange(len(CATEGORIES))
        r_sub_category = random.randrange(
            len(list(CATEGORIES.values())[r_category]))
        self.set_category(list(CATEGORIES.keys())[r_category], list(
            CATEGORIES.values())[r_category][r_sub_category])

    def output_challenge(self):
        """Returns the output directory for a challenge according to the given parameters and creates it.

        :return: The directory where to save the challenge
        :rtype: str
        """
        global OS_SEP
        output = f"{OUTPUT_DIR}{self.name}_{self.id}{OS_SEP}"
        try:
            os.mkdir(output)
        except Exception as e:
            print(e)

        return output

    def generate(self):
        """Generates challenge according to sub-category, difficulty and output path.
        """
        print(f"Generating challenge '{self.name}' ({self.id})...")
        # Calls the right function to generate the challenge
        # TODO: its dangerous to do so
        try:
            globals()["challenge_" + self.sub_category](self)
        except CCGError(f"challenge's generating function for sub-category '{self.sub_category}' does not exists, if you are using a custom category, please add your own 😀") as e:
            print(e)


"""
Challenge generation-related functions
Actually defined (working?):
    - encoding (no)
    - hidden_message (no)
    - lsb (no)
    - rsa (no)
    - sqli (no)
    - ssti (no)
    - xss (no)
"""


def challenge_encoding(c):
    """Generates an encoding challenge according to the specified difficulty and flag. Only `difficulty=1` is supported for the moment.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    """
    Difficulty 1 (random one of):
        Encode flag in rotN and write to output file
        Encode flag in hex and write to output file
        Encode flag in dec and write to output file
        Encode flag in base64 and write to output file

    Difficulty 2:
        XoR flag with random int and write to output file
    """
    global CHALLENGE
    global OS_SEP

    # Creating the challenge's directory and storing it
    output = c.output_challenge()

    try:
        flag = c.flag

        if c.difficulty == 1:
            random_choice = random.randint(0, 3)
            if random_choice == 0:
                # rotN
                n = random.randint(1, 25)
                print(f"\tROT-{n} challenge")
                upper = string.ascii_uppercase
                lower = string.ascii_lowercase
                tmp = ''
                for x in flag:
                    if x in upper:
                        tmp += upper[(upper.index(x) + n) % len(upper)]
                    elif x in lower:
                        tmp += lower[(lower.index(x) + n) % len(lower)]
                    else:
                        tmp += x
                flag = tmp
            elif random_choice == 1:
                # hex
                print("\tHex-decode challenge")
                flag = flag.encode().hex()
            elif random_choice == 2:
                # dec
                print("\tDecimal-decode challenge")
                tmp = ''
                for x in flag:
                    tmp += (str(ord(x)) + ' ')
                flag = tmp
            elif random_choice == 3:
                # base64
                print("\tBase64-decode challenge")
                flag = base64.b64encode(flag.encode()).decode()

            # Write flag to file
            # TODO: function to setup a challenge with given parameters (docker?, sources...), create mandatory files too
            files = output + CHALLENGE["OUT"]
            os.mkdir(files)
            out_file = files + f"{OS_SEP}{c.id}.txt"
            with open(out_file, "w") as f:
                f.write(flag)
            print(f"\tCreated challenge at '{out_file}'")
        else:
            print("Difficulty too high!")

    except Exception as e:
        print(e)


def challenge_hidden_message(c):
    """Generates a hidden message challenge according to the specified difficulty and flag.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    global CHALLENGE
    try:
        print(c)
    except Exception as e:
        print(e)


def challenge_lsb(c):
    """Generates a lsb challenge according to the specified difficulty and flag.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    global CHALLENGE
    try:
        print(c)
    except Exception as e:
        print(e)


def challenge_rsa(c):
    """Generates a rsa challenge according to the specified difficulty and flag.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    global CHALLENGE
    try:
        print(c)
    except Exception as e:
        print(e)


def challenge_sqli(c):
    """Generates an sqli challenge according to the specified difficulty and flag.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    global CHALLENGE
    try:
        print(c)
    except Exception as e:
        print(e)


def challenge_ssti(c):
    """Generates an ssti challenge according to the specified difficulty and flag.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    global CHALLENGE
    try:
        print(c)
    except Exception as e:
        print(e)


def challenge_xss(c):
    """Generates an xss challenge according to the specified difficulty and flag.

    :param c: The challenge we want to generate
    :type c: Challenge
    """
    global CHALLENGE
    try:
        print(c)
    except Exception as e:
        print(e)
