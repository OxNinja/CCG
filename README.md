# CTF Challenge Generator (CCG)

![Logo](static/logo.png)

This package generates CTF challenges according to user-provided options, such as category, difficulty, custom flag...

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

`ccg new challenge --category web`

`ccg new challenge --category web --subcategory xss --flag c0ngr4tz_y0u_foUNd_1t --difficulty medium --name My-XSS-1 --points 100`

## FAQ

### I can't install CCG, what can I do?

Blame me and create a new question in the repository.
