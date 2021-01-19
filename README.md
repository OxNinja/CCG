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

```
$ ccg new my-challenge

$ ccg new my-challenge --flag=mY_sUpeR_fl4G --category=web --difficulty=2

$ ccg new -f mY_sUpeR_fl4G -c web -s ssti -d 1
```

### Custom categories

Add your custom category to the models:

```py
# /ccg/models/category.py
CATEGORIES = {
    ...
    "custom_category": ["my_category", "other_category"],
    ...
}
```

Create your own class for your category:

```py
# /ccg/category/my_category.py
from ccg.challenge.challenge import Challenge
from ccg.models import DIFFICULTIES

class MyCategory(ChallengeCategory):
    # We don't want easy nor hard challenges
    ACCEPTABLE_DIFFICULTY = list(DIFFICULTIES.keys()).remove(3).remove(1)

    @classmethod
    def generate(cls, challenge: Challenge) -> None:
        # Your own code for your category here
```

Use it with CCG:

```
$ ccg new custom-chall -c custom_category -s my_category
```

## FAQ

### I like trains

Yes of course

### Other question

No I don't
