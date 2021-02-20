from base64 import b64encode
from os.path import join
from random import randint

from ccg.category.category import ChallengeCategory
from ccg.challenge.challenge import Challenge
from ccg.models import DIFFICULTIES, EASY
from ccg.utility import rot_n, file_write


class ChallengeEncoding(ChallengeCategory):
    """Encoding challenge category: basic CTF challenge, like binary decode, base64, hex...
    """

    # Encoding challenge can only be of difficulty 'easy'
    ACCEPTABLE_DIFFICULTY = list(DIFFICULTIES[EASY])

    @classmethod
    def generate(cls, challenge: Challenge) -> None:
        """Class method override
        """
        # Retrieve the flag
        flag = challenge.flag

        # Choose randomly from:
        choices = ['bin', 'hex', 'base64', 'rotn', 'dec']
        choice = choices[randint(0, len(choices) - 1)]
        # Encode the flag depending on the choice
        if choice == 'bin':
            tmp = ''
            for char in flag:
                char = bin(char)[2:]
                tmp += f"{char} "
            flag = tmp[:-1]
            print("Binary encoding challenge")
        elif choice == 'hex':
            flag = flag.encode().hex()
            print("Hexadecimal encoding challenge")
        elif choice == 'base64':
            flag = b64encode(flag.encode()).decode()
            print("Base64 encoding challenge")
        elif choice == 'rotn':
            shift = randint(1, 25)
            flag = rot_n(flag, shift)
            print(f"ROT-{shift} encoding challenge")
        elif choice == 'dec':
            tmp = ''
            for char in flag.encode():
                tmp += f"{char} "
            flag = tmp[:-1]
            print("Decimal encoding challenge")

        # Write the encoded flag in the output file
        file_write(flag, join(challenge.path, "challenge.txt"))
