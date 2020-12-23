#!/usr/bin/env python3
# coding: utf-8

"""
This file may help you to test the module, you will be provided code snippets to understand how to use the module besides the documentation
"""

# Importing the module
import ccg


def main():
    SEP = "\n===-===-===-===-===-===-===-===-===-===\n"
    print(f"\n=== CCG testing script ===\n")

    try:
        print(
            "Creating a challgene with no parameter on purpose, this should raise an error")
        c = ccg.Challenge()
        print(c)

    except Exception as e:
        print(e)

    print(SEP, "Showing the current (default) categories with corresponding sub-categories")
    #CATEGORIES = ccg.Categories().categories
    print(ccg.CATEGORIES)

    try:
        print(SEP, "Creating a challenge with existing category but not existing sub-category should also raise an error")
        c = ccg.Challenge(category="web", sub_category="not_existing")
        print(c)
    except Exception as e:
        print(e)

    try:
        print(SEP, "Creating a correct challenge, with a custom flag")
        c = ccg.Challenge(category="web", sub_category="ssti", difficulty=1,
                          flag="My_sUp3r_fL4g!", name="My super challenge")
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
                          difficulty=1, name="My super challenge")
        print(c)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
