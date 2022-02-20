from os import listdir, makedirs
from os.path import abspath, dirname, join
from random import choice, randint
from shutil import copytree
from yaml import dump

from ccg.models.challenge import Challenge
from ccg.models.challenge import DIFFICULTIES
from ccg.models.categories.category import Category


class ChallengeSqli(Category):
    """Generate a web/sqli challenge
    easy:
        basic injection in URL using the 'id=' GET parameter
        generates a docker-compose.yml file and challenge sources
    """
    def __init__(self):
        pass

    @staticmethod
    def generate(challenge):
        # check difficulty
        if challenge.difficulty == DIFFICULTIES[0]: # easy challenge
            # generate challenge config file
            Category.create_config(challenge)
            # generate challenge flag file
            Category.create_flag(challenge)

            # create src directory
            challenge_src_dir = join(challenge.out, "src")
            makedirs(challenge_src_dir)

            # generate config
            config_db_password = "testtest"

            # generate docker-compose.yml
            docker_compose = {
                    "services": {
                        "db": {
                            "image": "mysql:5.7",
                            "container_name": f"{challenge.name}_db",
                            "restart": "always",
                            "environment": [
                                f"MYSQL_ROOT_PASSWORD={config_db_password}",
                                f"MYSQL_DATABASE=database",
                                ],
                            "volumes": [
                                "./src/db/db.sql:/docker-entrypoint-initdb.d/db.sql",
                                ],
                            "ports": [
                                "3306:3306",
                                ],
                            "networks": {
                                "local_net"
                                }
                            },
                        "web": {
                            "build": {
                                "context": "src",
                                "dockerfile": "web.dockerfile",
                                },
                            "container_name": f"{challenge.name}_web",
                            "volumes": [
                                "./src/web/:/var/www/html/",
                                ],
                            "ports": [
                                "80:80",
                                ],
                            "networks": {
                                "local_net"
                                },
                            "depends_on": [
                                "db",
                                ]
                            },
                        },
                    "networks": {
                        "local_net": {
                            "ipam": {
                                "driver": "default"
                                }
                            }
                        }
                    }

            with open(join(challenge.out, "docker-compose.yml"), "w+") as f:
                f.write(dump(docker_compose))

            templates_dir = join(dirname(abspath(__file__)), "templates")
            # select random template
            template = choice(listdir(templates_dir))
            challenge.log(f"using template {template}")
            template_path = join(templates_dir, template)

            # copy template files in challenge
            copytree(template_path, challenge_src_dir, dirs_exist_ok=True)

            # replace template config placeholders with current values
            # the following files need to be changed for a template
            #   db/db.sql                   # for the flag
            #   web/includes/config.php     # for the web server config

            # TODO: for the moment no clean sed-like python module so here is a bad code example instead
            # TODO: create a function for that like `replace_in_file(file: str, to_replace: list)`
            # db/db.sql
            # open file and save its content
            config_file = join(challenge_src_dir, "db", "db.sql")
            data =  open(config_file, "r").read()

            # replace with values
            data = data.replace("$FLAG", challenge.flag)

            # write back to file
            open(config_file, "w").write(data)

            # web/includes/config.php
            # open file and save its content
            config_file = join(challenge_src_dir, "web", "includes", "config.php")
            data =  open(config_file, "r").read()

            # replace with values
            data = data.replace("$DB_DATABASE", "database")
            data = data.replace("$DB_USER", "root")
            data = data.replace("$DB_PASSWORD", "testtest")
            data = data.replace("$DB_HOST", "db")

            # write back to file
            open(config_file, "w").write(data)

            challenge.log("template config updated with current values")
        else: # bad difficulty input
            raise Exception(f"the choosen difficulty ({challenge.difficulty}) is not compatible with the current category ({challenge.sub_category})")
