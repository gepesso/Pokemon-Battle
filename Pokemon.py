# Test on pokemon battles

import time
import numpy as np
import pandas as pd
import sys
import math


# Delay printing

def delay_print(str):
    # Print one character at a time
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)


class Pokemon:

    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.bars = 20  # amount of health bars

    def fight(self,Pokemon2):
        # 2 pokemon fight

        # Print fight info
        print("-----POKEMON BATTLE-----")

        print(f"n\{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))

        print("\nVS")

        print(f"n\{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        # Consider type advantages
        version = ['Fire', 'Water','Grass']
        for i,k enumerate(version):
            if self.types == k:
                # Both are the same type
                if Pokemon2.types == k:
                    str1_attack = 'Its not very effective'
                    str2_attack = 'Its not very effective'
                # Pokemon 2 is strong
                if Pokemon2.types == version[(i+3)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *=2
                    self.attack /=2
                    self.defense /=2
                    str1_attack = 'Its not very effective'
                    str2_attack = 'Its super effective'
                # Pokemon2 is Weak
                if Pokemon2.types == version[(i+2)%3]
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    self.attack *= 2
                    self.defense *= 2
                    str2_attack = 'Its not very effective'
                    str1_attack = 'Its super effective'

        # Fighting starts
        while (self.bars > 0) and (Pokemon2.bars >0):
            # Print Health
            print(f"{self.name}\t\tHP\t{self.health}")
            print(f"{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"{self.name} used {moves[index - 1]}!")
            time.sleep(1)
            delay_print(str1_attack)

            #Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars + 1*Pokemon2.defense)):
                Pokemon2.health += "="






