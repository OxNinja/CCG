#!/usr/bin/env python3
# coding: utf-8

"""
This file may help you to test the module, you will be provided code snippets to understand how to use the module besides the documentation
"""

# Importing the module
import ccg

# For some random you know
import random


def main():
    SEP = "\n===-===-===-===-===-===-===-===-===-===\n"
    print(f"\n=== CCG testing script ===\n")

    print("Showing the actual list of all challenges")
    print(ccg.challenges)

    try:
        print(SEP, "Creating a challgene with no parameter on purpose, this should raise an error")
        c = ccg.Challenge()
        print(c)

    except Exception as e:
        print(e)

    print(SEP, "Showing the current (default) categories with corresponding sub-categories")
    print(ccg.CATEGORIES)

    try:
        print(SEP, "Creating a challenge with existing category but not existing sub-category should also raise an error")
        c = ccg.Challenge(category="web", sub_category="not_existing")
        print(c)
    except Exception as e:
        print(e)

    try:
        print(SEP, "Creating a correct challenge, with a custom flag")
        c = ccg.Challenge(category="web", sub_category="ssti", difficulty=2,
                          flag="My_sUp3r_fL4g!", name="My challenge")
        print(c)
    except Exception as e:
        print(e)

    try:
        print(SEP, "Customizing the flag format")
        ccg.FLAG_FORMAT = "my_format-flag_here"
        # you must keep the 'flag_here' string in the format, but you can change it using the global variable FLAG_FORMAT_FLAG:
        # ccg.FLAG_FORMAT_FLAG = 'hello_there'
        # ccg.FLAG_FORMAT = 'frmt[hello_there]'
        c = ccg.Challenge(category="web", sub_category="ssti",
                          difficulty=1, name="My super challenge")
        print(c)
    except Exception as e:
        print(e)

    try:
        print(SEP, "Using custom categories")
        ccg.CATEGORIES = {'cstm': ['a', 'b', 'hey']}
        c = ccg.Challenge(category="cstm", sub_category="hey",
                          difficulty=3, name="My super challenge")
        print(c)
    except Exception as e:
        print(e)

    print(SEP, "Showing the actual list of all challenges")
    print(ccg.challenges)

    try:
        # Getting one random challenge's id
        i = ccg.challenges[random.randint(0, len(ccg.challenges) - 1)].id
        print(SEP, f"Retrieving a challenge by its id: '{i}'")
        print(ccg.get_challenge_by_id(i))
    except Exception as e:
        print(e)

    try:
        print(SEP, "Retrieving challenges with their names: 'My super challenge'")
        print(ccg.get_challenges_by_name("My super challenge"))
    except Exception as e:
        print(e)

    try:
        print(SEP, "Generating a basic challenge")
        # Reseting the categories by default
        ccg.CATEGORIES = ccg.Categories().categories
        c = ccg.Challenge(category="crypto", sub_category="encoding", difficulty=1, name="My encoding 1")
        print(c)
        c.generate()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
