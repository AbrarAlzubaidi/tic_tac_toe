
"""
1. player1----> bot will randomly choose a position
2. find the winning array for the bot position
3. choose a number from array that not used before if its not choose another position(position_bot != position user)
4. keep check winning position player
"""

import builtins
import random

class bot:
    def __init__(self):
        self.old_print =print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    def choose_position(self):
        pass


