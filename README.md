# CTF Challenge Generator (CCG)

![Logo](static/logo.png)

This package generates CTF challenges according to user-provided options, such as category, difficulty, custom flag...

CCG creates a directory for each challenge at `OUTPUT_DIR/{name}_{id}` containing:

* `files/`:

  Containing all challenge's output files

* `src/` (optional):

  Containing all challenge's source in order to build it

* `challenge.yml`:

  The challenge's configuration (ie. flag, description, name...)

* `Dockerfile` (optional):

  The challenge's configuration in a Dockerfile, for prod use

* `docker-compose.yml` (optional):

  The challenge's configuration in a docker-compose file, for dev testing

## How to use

You should take a look at the [test.py](https://github.com/OxNinja/CCG/blob/master/test.py) file, you will find a ton of use cases :blush:

### Basic usage

```py
import ccg

my_challenge = ccg.Challenge(
 category="web",
 sub_category="ssti",
 difficulty=1,
 flag="my_super_flag",
 name="my_first_web_challenge")
```

### Custom categories

```py
import ccg

ccg.CATEGORIES = {
 "my_cat": ["sub_cat1", "sub_cat2"],
 "web": ["xxe", "any_sub_cat"]
}

my_challenge = ccg.Challenge(
 category="my_cat",
 sub_category="sub_cat_1",
 difficulty=1,
 flag="my_super_flag",
 name="my_challenge_in_custom_category"
)
```

## FAQ

### I like trains

Yes of course

### Other question

No I don't
