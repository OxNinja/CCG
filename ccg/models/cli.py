from yaspin import yaspin
from yaspin.spinners import Spinners


class CLI:
    def __init__(self):
        self.spinner = Spinners.dots
        self.ok = "✅"
        self.fail = "❌"

    def spin(self, text=""):
        return yaspin(self.spinner, text)


CCG_CLI = CLI()