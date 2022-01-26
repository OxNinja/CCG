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

## How to use

### Basic usage

`ccg new "My web challenge" --category web`

`ccg new "My XSS 1" --category web --subcategory xss --flag c0ngr4tz_y0u_foUNd_1t --difficulty medium --points 100`

### Concept

* Any challenge have an auto generated `challenge.yml` configuration file
  > This file represents a challenge in a YAML format, this files is useful to get information about the challenge, for the CTF platform and for its deployment. This file is [compatible with CTF Kit](https://git.fakenews.sh/ctfkit/ctfkit).
* Any challenge have a `flag.txt` validation file
* If a challenge requires users to download files, they will be writen in `{challenge_path}/files/`
* If a challenge requires sources, they will be stored in `{chalenge_path}/src/`
  > The challenge will be run using its own `Dockerfile` or `docker-compose.yml` in a containerization context.

## FAQ

### I can't install CCG, what can I do?

Blame me and create a new question in the repository.
