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
	if not flag:
		flag = '{0:016x}'.format(random.randrange(pow(10,20)))
	return FLAG_FORMAT.replace(FLAG_FORMAT_FLAG, flag)


"""
Classes
"""

"""
Errors class:
	Print errors according to CCG
"""

class CCGError(Exception):


	"""
	CCGError.__init__(): calls an exception with custom text when raised
	"""
	def __init__(self, problem):
		super().__init__(f"[CCG] An error occured: {problem}")



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
	Categories.__str__(): overwrite class.to_string()
	"""
	def __str__(self):
		return self.categories



"""
Challenge class:
	Initialize challenge, set variables (flag, difficulty, category...), check things and generate challenge
"""

class Challenge:


	"""
	Challenge.__init__(): initialize default values for challenge
		User must update variable CATEGORIES before creating a challenge (ex: `CATEGORIES = Categories().categories`) if needed
	"""
	def __init__(self,category=None,sub_category=None,difficulty=None,flag=None,name=None):
		global CATEGORIES 
		CATEGORIES = Categories().categories
		# TODO: Check for good types (if category is a correct string, if difficulty is a correct integer...)
		self.category = category
		self.sub_category = sub_category
		self.difficulty = difficulty
		self.flag = gen_flag(flag)
		self.name = name

		# Check if challenge is okay
		self.check()


	"""
	Challenge.__str__(): overwrite class.to_string()
	"""
	def __str__(self):
		# TODO: better print for a challenge
		return f"""=-= SOC: {self.name} =-=
	- Category: {self.category}
	- Sub-category: {self.sub_category}
	- Difficulty: {self.difficulty}
	- Flag: {self.flag}
=-= EOC =-="""


	"""
	Challenge.check():
		Checks if challenge is okay (ie. if category exists...)
	"""
	def check(self):
		# Check for category
		if not self.category in CATEGORIES:
			raise CCGError(f"challenge's category '{self.category}' not found")
		
		# Check for sub-category
		if not self.sub_category in CATEGORIES[self.category]:
			raise CCGError(f"challenge's sub-category '{self.sub_category}' not found in category '{self.category}'")


	"""
	Challenge.set_category(category, sub_category):
		Modify a challenge's category and sub-category, then checks if it is okay
	"""
	def set_category(self, category, sub_category):
		self.category = category
		self.sub_category = sub_category
		self.check()


	"""
	Challenge.random_category():
		Modfify a challenge's category and sub-category for a random correct value
	"""
	def random_category(self):
		r_category = random.randrange(len(CATEGORIES))
		r_sub_category = random.randrange(len(list(CATEGORIES.values())[r_category]))
		self.set_category(list(CATEGORIES.keys())[r_category], list(CATEGORIES.values())[r_category][r_sub_category])


	"""
	Challenge.generate(): generate challenge according to category, difficulty and output path
	"""
	def generate(self):
		# TODO: generate a challenge
		print(self)


