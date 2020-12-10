# CTF Challenge Generator (CCG)

![Logo](static/logo.png)

This package generates CTF challenges according to user-provided options, such as category, difficulty, custom flag...
CCG creates either:

* A challenge file
    For basic challenges (txt file, encrypted content, image...)
* A challenge directory
    For more complex challenges, with a Dockerfile to deploy the challenge (web service, pwn socket...)

## How to use

### Basic usage

```py
from ccg import *

my_challenge = Challenge(
 category="web",
 sub_category="ssti",
 difficulty=1,
 flag="my_super_flag",
 name="my_first_web_challenge")

print(my_challenge)
```

### Custom categories

```py
from ccg import *

CATEGORIES = {
 "my_cat": ["sub_cat1", "sub_cat2"],
 "web": ["xxe", "any_sub_cat"]
}

my_challenge = Challenge(
 category="my_cat",
 sub_category="sub_cat_1",
 difficulty=1,
 flag="my_super_flag",
 name="my_challenge_in_custom_category"
)

print(my_challenge)
```

## FAQ

### I like trains

Yes of course

### Other question

No I don't
