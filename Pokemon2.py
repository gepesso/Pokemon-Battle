import sys
import numpy as np
import random
import os
import pandas as pd
import time

# READS THE FILE WITH ALL POKEMON AND STATS
xls = pd.read_excel('Pokemon.xlsx')

# READS THE FILE WITH ALL THE MOVES
xls2 = pd.read_excel('Pokemon_moves.xlsx', 'Moves')

# READS THE FILE WITH ALL THE WEAKNESSES
xls3 = pd.read_excel('Pokemon_weaknesses.xlsx', 'Matrix (RG)')

# CREATES A DICTIONARY WITH ALL THAT INFO
pk_d = xls.to_dict('records')
pk_m = xls2.to_dict('records')
xls3 = xls3.set_index('Adv')
pk_a = xls3.to_dict('indexes')
print(pk_a['NORMAL']['ROCK'])


# Delay printing

def delay_print(str):
    # Print one character at a time
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)


class Pokemon:

    def __init__(self, pk_d):
        self.attmoves = []
        self.name = pk_d['Name']
        self.types = [pk_d['Type 1'], pk_d['Type 2']]
        self.health = pk_d["HP"]
        self.attack = pk_d["Attack"]
        self.defense = pk_d["Defense"]
        self.speed = pk_d["Speed"]
        self.bars = 20  # amount of health bars

    def moves(self, pk_m):
        for i in range(0, 4):
            move = pk_m[random.randint(1, 615)]
            # print(move["Type"], self.types[0], self.types[1])
            while move["Type"] != self.types[0] and move["Type"] != self.types[1]:
                move = pk_m[random.randint(1, 615)]
            self.attmoves.append(move)

            # print(self.attmoves)
        return self.attmoves

    def weakness(self, pk_a, otherpokemon):
        # ERROR IS HERE!

        print(pk_a[self.types[0].upper()])
        self.adv = pk_a[self.types[0].upper()]
        if self.types[1] != "nAn":
            self.adv = self.adv + pk_a[self.types[1].upper()]
        return self.adv


Pokemon1 = Pokemon(pk_d[1])
Pokemon2 = Pokemon(pk_d[4])
print(Pokemon1.name + "\n" + Pokemon2.name)
print(Pokemon1.types)
# print(Pokemon1.attack)
# print(pk_m[random.randint(1,100)])
print(Pokemon1.moves(pk_m))
print(Pokemon2.moves(pk_m))
print(Pokemon1.weakness(pk_a))
print(Pokemon2.weakness(pk_a))

# CREATES VARIABLE TO CHECK FOR GAME OVER
game_over = False

# MAIN AREA OF THE GAME
while not game_over:

    if Pokemon1.health <= 0 or Pokemon2.health <= 0:
        game_over = True
