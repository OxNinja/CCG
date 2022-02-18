import setuptools

PKG_NAME = "ccg"
PKG_VERSION = "0.0.1"
PKG_AUTHOR = "0xNinja"
PKG_AUTHOR_EMAIL = "author@example.com"
PKG_DESC = "CCG - CTF Challenge Generator"
PKG_DESC_CON_TYPE = "text/markdown"
PKG_URL = "https://nephael.net"
PKG_CLASSIFIERS = [
   "Programming Language :: Python :: 3",
   "License :: OSI Approved :: MIT License",
   "Operating System :: OS Independent"
]
PKG_PYTHON_REQ = ">=3.10"
PKG_ENTRY = """
    [console_scripts]
    ccg=ccg.cli:cli
"""
PKG_DEP = [
    "Click",
    "yaspin",
    "python-slugify",
    "pyyaml",
]

with open("README.md", "r") as fh:
    PKG_LONG_DESC = fh.read()

setuptools.setup(
    name=PKG_NAME,
    version=PKG_VERSION,
    author=PKG_AUTHOR,
    author_email=PKG_AUTHOR_EMAIL,
    description=PKG_DESC,
    long_description=PKG_LONG_DESC,
    long_description_content_type=PKG_DESC_CON_TYPE,
    url=PKG_URL,
    install_requires=PKG_DEP,
    packages=setuptools.find_packages(),
    classifiers=PKG_CLASSIFIERS,
    python_requires=PKG_PYTHON_REQ,
    entry_points=PKG_ENTRY
)
