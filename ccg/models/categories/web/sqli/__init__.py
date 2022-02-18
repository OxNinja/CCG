from os import makedirs
from os.path import join
from random import randint
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
            # generate common files
            Category.create_config(challenge)
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
                            "image": "php:7.2-apache",
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

            # generate flag file
            # select template
            # fix template config
            challenge.log("ok")
        else: # bad difficulty input
            raise Exception(f"the choosen difficulty ({challenge.difficulty}) is not compatible with the current category ({challenge.sub_category})")
