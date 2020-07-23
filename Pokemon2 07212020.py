import sys
import numpy as np
import random
import os
import math
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


# print(pk_a['NORMAL']['ROCK'])


# Delay printing

def delay_print(str):
    # Print one character at a time
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)


# CHECKS FOR NAN
def isNaN(num):
    return num != num


class Pokemon:

    def __init__(self, pk_d):
        self.attmoves = []
        self.attadv = [1, 1, 1, 1]
        self.name = pk_d['Name']
        self.types = [pk_d['Type 1'], pk_d['Type 2']]
        self.health = pk_d["HP"]
        self.attack = pk_d["Attack"]
        self.defense = pk_d["Defense"]
        self.speed = pk_d["Speed"]
        self.spatk = pk_d["Sp. Atk"]
        self.spdef = pk_d["Sp. Def"]
        self.total = self.health + self.attack + self.defense + self.speed + self.spatk + self.spdef

        # IF STATEMENT TO CALCULATE THE LEVEL AND HEALTH
        if self.total <= 100:
            self.level = 5 + random.randint(-4, 4)
            self.health = 4 * pk_d["HP"] - 2.5 * self.level
        elif self.total <= 00:
            self.level = 10 + random.randint(-4, 4)
            self.health = 4 * pk_d["HP"] - .5 * self.level
        elif self.total <= 300:
            self.level = 15 + random.randint(-3, 3)
            self.health = 4 * pk_d["HP"] - .5 * self.level
        elif self.total <= 400:
            self.level = 22 + random.randint(-5, 5)
            self.health = 4 * pk_d["HP"] + self.level * .5
        elif self.total <= 500:
            self.level = 34 + random.randint(-2, 10)
            self.health = 4 * pk_d["HP"] + self.level * 1.5
        else:
            self.level = 46 + random.randint(-4, 6)
            self.health = 4 * pk_d["HP"] + self.level * 3

        self.divider = self.health / 20
        self.bars = "===================="  # amount of health bars

    def moves(self, pk_m):
        for i in range(0, 4):
            move = pk_m[random.randint(1, 615)]
            while move["Type"] != self.types[0] and move["Type"] != self.types[1]:
                move = pk_m[random.randint(1, 615)]
            self.attmoves.append(move)

            # PRINTS THE ATTACK AD TYPE--> print(self.attmoves[i]['Name'] + ":"+ self.attmoves[i]['Type'] )
        return self.attmoves

    def weakness(self, pk_a, otherpokemon):
        # ITERATES ON OPPOSING POKEMON TYPE
        for j in range(0, 2):
            for i in range(0, len(otherpokemon.attmoves)):
                # ITERATES INSIDE BOTH THE ATTAACKS FOR EACH POKEMON AND THE TYPE OF THE DEFENSE POKEMON
                if not isNaN(otherpokemon.types[j]):
                    # GETS THE ADVANTAGE/DISADVANTAGE FROM THE TABLE
                    self.attadv[i] *= pk_a[self.attmoves[i]['Type'].upper()][str(otherpokemon.types[j]).upper()]

        print(self.attadv)

    def fighthing(self, otherpokemon):
        # PRINTS THE SECOND POKEMON NAME
        print("{} H:{} LVL:{}".format(otherpokemon.name, otherpokemon.health, otherpokemon.level))
        # CHECKS FOR DUAL TYPE
        if isNaN(otherpokemon.types[1]):
            print("TYPE: {}".format(otherpokemon.types[0]))
        else:
            print("TYPE: {} / {}".format(otherpokemon.types[0], otherpokemon.types[1]))
        # PRINTS THE HP BARS
        print("HP: {}".format(otherpokemon.bars))

        print("\n----VS----\n")

        # PRINTS THE POKEMON NAME
        print("{} H:{} LVL:{}".format(self.name, self.health, self.level))
        # CHECKS FOR DUAL TYPE
        if isNaN(self.types[1]):
            print("TYPE: {}".format(self.types[0]))
        else:
            print("TYPE: {} / {}".format(self.types[0], self.types[1]))
        # PRINTS THE HP BARS
        print("HP: {}\n".format(self.bars))

        # PRINTS YOUR POKEMON ATTACKS
        for i in range(0, len(otherpokemon.attmoves)):
            print("{} - {} - POWER: {}".format(i + 1, self.attmoves[i]['Name'], self.attmoves[i]['Power']))

        # INPUT TO CHOOSE ATTACK
        # THIS PART CHECKS FOR THE INPUT, IF IT IS INCORRECT IS ASKS TO BE RE-ENTERED
        while True:
            try:
                choice = int(input("\nChoose your attack: "))
                if choice >4:
                    print("Please Re-enter your attack selection")
                    continue
            except ValueError:
                print("Please Re-enter your attack selection")
                continue
            else:
                break

        #AFTER CHOOSING THE ATTACK, ATTACK HAPPENS
        # YOUR POKEMON ATTACK

        if "—" in str(self.attmoves[choice - 1]['Power']):
            self.attmoves[choice - 1]['Power'] = "0"
        if "*" in str(self.attmoves[choice - 1]['Power']):
            self.attmoves[choice - 1]['Power'] = str(self.attmoves[choice - 1]['Power'])[:len(str(self.attmoves[choice - 1]['Power']))-1]

        print(self.attmoves)
        self.attackpoke = float(self.attack) + float(self.attmoves[choice-1]['Power'])
        self.defensepoke = self.defense

        # OPPOSING POKEMON ATTACK
####ERROR IS HERE
        otherchoice = random.randint(1,4)
        # print(otherpokemon.attmoves)
        # otherchoice = int(input("\nChoose his attack: "))

        if "—" in str(otherpokemon.attmoves[otherchoice - 1]['Power']):
            otherpokemon.attmoves[otherchoice - 1]['Power'] = "0"
        if "*" in str(otherpokemon.attmoves[otherchoice - 1]['Power']):
            otherpokemon.attmoves[otherchoice - 1]['Power'] = str(otherpokemon.attmoves[otherchoice - 1]['Power'])[
                                                 :len(str(otherpokemon.attmoves[otherchoice - 1]['Power'])) - 1]

        otherpokemon.attackpoke = float(otherpokemon.attack) + float(otherpokemon.attmoves[choice - 1]['Power'])
        otherpokemon.defensepoke = otherpokemon.defense

        print("----\n")

Pokemon1 = Pokemon(pk_d[0])
Pokemon2 = Pokemon(pk_d[5])
print(Pokemon1.name + "\n" + Pokemon2.name)
print(Pokemon1.types)
print(Pokemon2.types)
Pokemon1.moves(pk_m)
Pokemon2.moves(pk_m)
# print(pk_m[random.randint(1,100)])
# print(Pokemon1.moves(pk_m))
# Pokemon2.moves(pk_m)
Pokemon1.weakness(pk_a, Pokemon2)
Pokemon2.weakness(pk_a, Pokemon1)

# CREATES VARIABLE TO CHECK FOR GAME OVER
game_over = False
print("\n-----Pokemon Battle------\n\n{} Vs. {}\n".format(Pokemon1.name, Pokemon2.name))

# MAIN AREA OF THE GAME
while not game_over:

    Pokemon1.fighthing(Pokemon2)

    if Pokemon1.health <= 0 or Pokemon2.health <= 0:
        game_over = True
