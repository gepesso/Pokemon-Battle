import sys
import math
import time


# Delay printing

def delay_print(str):
    # Print one character at a time
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)


class Pokemon:

    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.bars = 20  # amount of health bars
