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
        time.sleep(.01)


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
        self.attplus = 0

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

        self.hdivider = self.health / 20
        self.bars = "===================="  # amount of health bars
        self.displayHP = self.bars

    def moves(self, pk_m):
        for i in range(0, 4):
            move = pk_m[random.randint(1, 615)]
            while move["Type"] != self.types[0] and move["Type"] != self.types[1]:
                move = pk_m[random.randint(1, 615)]
            self.attmoves.append(move)

            # CORRECTS THE POWER TO BE ONLY NUMBERS
            if "—" in str(self.attmoves[i]['Power']):
                self.attmoves[i]['Power'] = "0"
            if "*" in str(self.attmoves[i]['Power']):
                self.attmoves[i]['Power'] = str(self.attmoves[i]['Power'])[:- 1]

            # CORRECTS ACCURACY FOR SOME MOVES
            if "—" in str(self.attmoves[i]['Accuracy']):
                self.attmoves[i]['Accuracy'] = "100"
            if "*" in str(self.attmoves[i]['Accuracy']):
                self.attmoves[i]['Accuracy'] = str(self.attmoves[i]['Accuracy'])[:- 1]
            if "%" in str(self.attmoves[i]['Accuracy']):
                self.attmoves[i]['Accuracy'] = str(self.attmoves[i]['Accuracy'])[:- 1]
            if "%*" in str(self.attmoves[i]['Accuracy']):
                self.attmoves[i]['Accuracy'] = str(self.attmoves[i]['Accuracy'])[:- 2]
            if float(self.attmoves[i]['Accuracy']) > 1.0:
                self.attmoves[i]['Accuracy'] = float(self.attmoves[i]['Accuracy'])/100


        return self.attmoves

    # THIS FUNCTION CALCULATES THE ADVANTAGE OR DISADVANTAGE OF EACH ATTACK FOR EACH POKEMON AND
    # CREATES A LIST BASED ON THE ADVANTAGE TABLE
    def weakness(self, pk_a, opok):
        # ITERATES ON OPPOSING POKEMON TYPE
        for j in range(0, 2):
            for i in range(0, len(opok.attmoves)):
                # ITERATES INSIDE BOTH THE ATTAACKS FOR EACH POKEMON AND THE TYPE OF THE DEFENSE POKEMON
                if not isNaN(opok.types[j]):
                    # GETS THE ADVANTAGE/DISADVANTAGE FROM THE TABLE
                    self.attadv[i] *= pk_a[self.attmoves[i]['Type'].upper()][str(opok.types[j]).upper()]

    def attack_phrase(self, i, move):
        # DESCRIBES THE POKEMON AND ATTACK USED
        pokemontext1 = "\n{} used {}"

        # BELOW SELECTS THE EFFECTIVENESS OF THE ATTACK
        if self.attadv[i-1] < 1:
            pokemontext2= "\n{} attack was not very effective..."
        elif 1 < self.attadv[i-1] < 2:
            pokemontext2 = "\n{} attack was very effective."
        elif self.attadv[i-1] >=2:
            pokemontext2 = "\n{} attack was very effective."
        else:
            pokemontext2 = "\n{} attack was effective."

        # PRINTS TO THE SCREEN
        delay_print(pokemontext1.format(self.name, move))
        delay_print(pokemontext2.format(self.name))

    def fighthing(self, opok):
        global game_over, choice
        # PRINTS THE SECOND POKEMON NAME
        print("{} H:{} LVL:{}".format(opok.name, opok.health, opok.level))
        # CHECKS FOR DUAL TYPE
        if isNaN(opok.types[1]):
            print("TYPE: {}".format(opok.types[0]))
        else:
            print("TYPE: {} / {}".format(opok.types[0], opok.types[1]))
        # PRINTS THE HP BARS
        print("HP: {}".format(opok.displayHP))

        print("\n----VS----\n")

        # PRINTS THE POKEMON NAME
        print("{} H:{} LVL:{}".format(self.name, self.health, self.level))
        # CHECKS FOR DUAL TYPE
        if isNaN(self.types[1]):
            print("TYPE: {}".format(self.types[0]))
        else:
            print("TYPE: {} / {}".format(self.types[0], self.types[1]))
        # PRINTS THE HP BARS
        print("HP: {}\n".format(self.displayHP))

        # PRINTS YOUR POKEMON ATTACKS
        for i in range(0, len(opok.attmoves)):
            print("{} - {} - POWER: {} ACCURACY: {} %".format(i + 1, self.attmoves[i]['Name'], self.attmoves[i]['Power'], 100*self.attmoves[i]['Accuracy']))

        # INPUT TO CHOOSE ATTACK
        # THIS PART CHECKS FOR THE INPUT, IF IT IS INCORRECT IS ASKS TO BE RE-ENTERED
        while True:
            try:
                choice = int(input("\nChoose your attack: "))
                if choice > 4:
                    print("Please Re-enter your attack selection")
                    continue
            except ValueError:
                print("Please Re-enter your attack selection")
                continue
            else:
                break

        # AFTER CHOOSING THE ATTACK, ATTACK HAPPENS
        # YOUR POKEMON ATTACK BASED ON YOUR CHOICE

        # ATTACK IS CALCULATED BASED ON POKEMON BASE ATTACK AND MOVE ATTACK
        # IF POWER ZERO, THEN ATTACK ZERO
        if self.attmoves[choice - 1]['Power'] == '0':
            self.attackpoke = 0.0
        # ELSE CALCULATES THE ATTACK DAMAGE
        else:
            self.attackpoke = self.attadv[choice-1]*(2+((2*self.level/5 + 2)*float(self.attmoves[choice - 1]['Power'])*self.attack/opok.defense)/50)

        Pokemon1.attack_phrase(choice, self.attmoves[choice - 1]['Name'])


        # DEFENSE BASED ON BASE DEFENSE
        self.defensepoke = float(self.defense)

        # CHECK FOR ACCURACY (TO SEE IF THE POKEMON MISSES THE ATTACK)
        self.accuracy = self.attmoves[choice - 1]['Accuracy']*random.random()
        if (self.accuracy <= .15) or (self.attmoves[choice - 1]['Power'] == 0):
            self.attackpoke = 0
            delay_print("\n{} missed the attack.".format(self.name))
        if self.accuracy >= .95:
            self.attackpoke *= 2
            delay_print("\nCritical Hit!")

        # OPPOSING POKEMON ATTACK
        # RANDOMLY SELECTS AN ATTACK FOR THE OPPOSING POKEMON
        otherchoice = random.randint(1, 4)

        # ATTACK IS CALCULATED BASED ON POKEMON BASE ATTACK AND MOVE ATTACK
        if opok.attmoves[otherchoice - 1]['Power'] == '0':
            opok.attackpoke = 0.0
        else:
            opok.attackpoke = opok.attadv[otherchoice-1]*(2+((2*opok.level/5 + 2)*float(opok.attmoves[otherchoice - 1]['Power'])*opok.attack/self.defense)/50)

        # PRINTS THE POKEMON, ATTACK AND EFFECTIVENESS
        Pokemon2.attack_phrase(otherchoice, opok.attmoves[otherchoice - 1]['Name'])

        # DEFENSE BASED ON BASE DEFENSE
        opok.defensepoke = float(opok.defense)

        # CHECK FOR ACCURACY (TO SEE IF THE POKEMON MISSES THE ATTACK)
        opok.accuracy = opok.attmoves[choice - 1]['Accuracy'] * random.random()
        if (opok.accuracy <= .15) or (opok.attmoves[otherchoice - 1]['Power'] == 0):
            opok.attackpoke = 0
            delay_print("\n{} missed the attack.".format(opok.name))
        if opok.accuracy >= .95:
            opok.attackpoke *= 2
            delay_print("\nCritical Hit!")

        # CALCULATES YOUR HEALTH AND OPPONENT'S HEALTH

        self.health = round(self.health - opok.attackpoke, 1)

        self.attplus += round(opok.attackpoke / self.hdivider)

        opok.health = round(opok.health - self.attackpoke, 1)

        opok.attplus += round(self.attackpoke / opok.hdivider)

        if self.attplus >= 1:
            self.displayHP = self.bars[:-self.attplus]
        else:
            self.displayHP = self.displayHP

        if opok.attplus >= 1:
            opok.displayHP = opok.bars[:-opok.attplus]
        else:
            opok.displayHP = opok.displayHP

        print("\n",self.attplus, opok.attplus)
        print("\n----\n")


Pokemon1 = Pokemon(pk_d[11])
Pokemon2 = Pokemon(pk_d[5])
Pokemon1.moves(pk_m)
Pokemon2.moves(pk_m)

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
