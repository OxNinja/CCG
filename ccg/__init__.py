#!/usr/bin/env python3
# coding: utf-8

import argparse, json


"""
Global variables
"""

CONFIG_DIR = 'config'
CATEGORIES_FILE = CONFIG_DIR + '/categories.json'
FLAG_FORMAT_FILE = CONFIG_DIR + '/flag.txt'
CATEGORIES = {}
TEMPLATE_DIR = 'templates'
DESC = 'CCG - CTF Challenge Generator'


def main():
    """First function to be called: programm's entrypoint

    Creates challenges according to user's parsed arguments
    """

    """ Initalize variables """
    # Get categories from config file
    with open(CATEGORIES_FILE) as f:
        CATEGORIES = json.load(f)

    """ CLI arguments """
    # Create a parser for CLI arguments
    p = argparse.ArgumentParser(description=DESC)
    # Exclusive groups
    g = p.add_mutually_exclusive_group()
    g.add_argument('-c','--category',
            help='set the challenge\'s category')
    g.add_argument('-r','--random',action='store_true',
            help='generate a challenge for a random category')
    # CLI arguments
    p.add_argument('-d','--difficulty',type=int,choices=[1,2,3],
            help='set the challenge\'s difficulty')
    p.add_argument('-f','--flag',
            help='set the challenge\'s flag')
    
    # Parse the CLI arguments and store them
    args = p.parse_args() 

    """ Process the arguments """
    #
    print(args)


if __name__ == '__main__':
    main()
