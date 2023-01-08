# CTF Challenge Generator (CCG)

![Logo](static/logo.png)

This package generates CTF challenges compatible with [CTF Kit](https://github.com/Team-FakeNews/CTFKit), according to user-provided options such as category, difficulty, custom flag...

## Install

### From source

> Use `https://github.com/OxNinja/CCG/tree/develop` for latest features (unstable)

```sh
git clone https://github.com/OxNinja/CCG && cd CCG
pip install -e .
```

### From PyPi package (not available for the moment)

```sh
pip install ccg
```

## Dependancies

* Python 3.10 or above
* pip

## How to use

### Basic usage

```sh
ccg new my-challenge

ccg new my-challenge --flag=mY_sUpeR_fl4G --category=web --difficulty=medium

ccg new -f mY_sUpeR_fl4G -c web -s ssti -d easy
```

### Concept

* Any challenge have an auto generated `challenge.yml` configuration file
  > This file represents a challenge in a YAML format, this files is useful to get information about the challenge, for the CTF platform and for its deployment. This file is [compatible with CTF Kit](https://git.fakenews.sh/ctfkit/ctfkit).
* Any challenge have a `flag.txt` validation file
* If a challenge requires users to download files, they will be writen in `{challenge_path}/files/`
* If a challenge requires sources, they will be stored in `{chalenge_path}/src/`
  > The challenge will be run using its own `Dockerfile` or `docker-compose.yml` in a containerization context.

## Implemented

* [x] Crypto
    * [x] Encodings (basics)
* [x] Reverse
    * [x] Code audit (basics)
* [x] Web
    * [x] SQLi (basic)

## Working on

* Selecting a random valid challenge category when possible
* Web template for Docker
* SQLi challenge template
* Basic static reverse challenges
* Refacto of the "selecting a random type of sub-category or challenge" part (creating a `utils.py` may help?)

## FAQ

### I can't install CCG, what can I do?

Blame me and create a new question in the repository.
