#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 12:51:02 2018

@author: andreunsal
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import operator

allPokemon = pd.read_csv('pokemon.csv')
#firstGen = dataSet[:166]

class Pokedex:
    
    def TypeScatter(self):
        pkmn_type_colors = ['#78C850',  # Grass
                            '#F08030',  # Fire
                            '#6890F0',  # Water
                            '#A8B820',  # Bug
                            '#A8A878',  # Normal
                            '#A040A0',  # Poison
                            '#F8D030',  # Electric
                            '#E0C068',  # Ground
                            '#EE99AC',  # Fairy
                            '#C03028',  # Fighting
                            '#F85888',  # Psychic
                            '#B8A038',  # Rock
                            '#705898',  # Ghost
                            '#98D8D8',  # Ice
                            '#7038F8',  # Dragon
                            ]
        plt.figure(figsize = (10, 7))
        sns.countplot(x = 'Type_1', data = allPokemon, palette = pkmn_type_colors)
        plt.grid()
        plt.title('Number of Each Pokemon by Primary Type')
        plt.xticks(rotation = -55)
        plt.show()
        return(0)
    
    def HighestHp(self):
        hpList = allPokemon['HP']
        pokemon = allPokemon['Name']
        threshold = 130
        print('\n')
        HighestHp = {}
        print("HIGHEST HP:")
        for i in range(len(hpList)):
            if hpList[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestHp[pokemon[i]] = allPokemon.iloc[i, 5]
        sortedHighestHp = sorted(HighestHp.items(), key = operator.itemgetter(1))
        for i in range(len(sortedHighestHp)):
            print(sortedHighestHp[i])
        plt.figure(figsize = (10, 7))
        plt.plot(hpList, color = 'green')
        plt.ylabel('Base HP')
        plt.xlabel('Pokedex Entry')
        plt.grid()
        plt.title('Hp vs. Pokemon\'s Index')
        plt.show()
        return(sortedHighestHp)
    
    def HighestAttackers(self):
        attackList = allPokemon['Attack']
        pokemon = allPokemon['Name']
        threshold = 130
        print('\n')
        HighestAttackers = {}
        print("HIGHEST ATTACKERS:")
        for i in range(len(attackList)):
            if attackList[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestAttackers[pokemon[i]] = allPokemon.iloc[i, 6]
        sortedHighestAttackers = sorted(HighestAttackers.items(), key = operator.itemgetter(1))
        for i in range(len(sortedHighestAttackers)):
            print(sortedHighestAttackers[i])
        plt.figure(figsize = (10, 7))
        plt.plot(attackList, color = 'red')
        plt.grid()
        plt.ylabel('Base Attack')
        plt.xlabel('Pokedex Entry')
        plt.title('Attack vs. Pokemon\'s Index')
        plt.show()
        return(sortedHighestAttackers)
        
    def HighestDefenders(self):
        defenseList = allPokemon['Defense']
        pokemon = allPokemon['Name']
        threshold = 130
        print('\n')
        HighestDefenders = {}
        print("HIGHEST DEFENDERS")
        for i in range(len(defenseList)):
            if defenseList[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestDefenders[pokemon[i]] = allPokemon.iloc[i, 7]
        sortedHighestDefenders = sorted(HighestDefenders.items(), key=operator.itemgetter(1))
        for i in range(len(sortedHighestDefenders)):
            print(sortedHighestDefenders[i])
        plt.figure(figsize = (10, 7))
        plt.plot(defenseList, color = 'grey')
        plt.grid()
        plt.ylabel('Base Defense')
        plt.xlabel('Pokedex Entry')
        plt.title('Defense vs. Pokemon\'s Index')
        plt.show()
        return(sortedHighestDefenders)
        
    def HighestSpAttackers(self):
        specialAttack = allPokemon['Sp_Atk']
        pokemon = allPokemon['Name']
        threshold = 125
        print('\n')
        HighestSpAttackers = {}
        print("HIGHEST SPECIAL ATTACKERS:")
        for i in range(len(specialAttack)):
            if specialAttack[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestSpAttackers[pokemon[i]] = allPokemon.iloc[i, 8]
        sortedHighestSpAttackers = sorted(HighestSpAttackers.items(), key=operator.itemgetter(1))
        for i in range(len(sortedHighestSpAttackers)):
            print(sortedHighestSpAttackers[i])
        plt.figure(figsize = (10,7))
        plt.plot(specialAttack, color = 'pink')
        plt.ylabel('Base Sp. Atk')
        plt.xlabel('Pokedex Entry')
        plt.grid()
        plt.title('Special Attack vs. Pokemon\'s Index')
        plt.show()
        return(sortedHighestSpAttackers)
    
    def HighestSpDefenders(self):
        specialDefense = allPokemon['Sp_Def']
        pokemon = allPokemon['Name']
        threshold = 125
        print('\n')
        HighestSpDefenders = {}
        print("HIGHEST SPECIAL DEFENDERS:")
        for i in range(len(specialDefense)):
            if specialDefense[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestSpDefenders[pokemon[i]] = allPokemon.iloc[i, 9]
        sortedHighestSpDefenders = sorted(HighestSpDefenders.items(), key=operator.itemgetter(1))
        for i in range(len(sortedHighestSpDefenders)):
            print(sortedHighestSpDefenders[i])
        plt.figure(figsize = (10, 7))
        plt.plot(specialDefense, color = 'blue')
        plt.ylabel('Base Sp. Def')
        plt.xlabel('Pokedex Entry')
        plt.grid()
        plt.title('Special Defense vs. Pokemon\'s Index')
        plt.show()
        return(sortedHighestSpDefenders)
        
    def HighestSpeeds(self):
        speed = allPokemon['Speed']
        pokemon = allPokemon['Name']
        threshold = 125
        print('\n')
        HighestSpeeds = {}
        print("HIGHEST SPEEDS:")
        for i in range(len(speed)):
            if speed[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestSpeeds[pokemon[i]] = allPokemon.iloc[i, 10]
        sortedSpeeds = sorted(HighestSpeeds.items(), key=operator.itemgetter(1))
        for i in range(len(sortedSpeeds)):
            print(sortedSpeeds[i])
        plt.figure(figsize = (10, 7))
        plt.plot(speed, color = 'orange')
        plt.ylabel('Base Speed')
        plt.xlabel('Pokedex Entry')
        plt.grid()
        plt.title('Speed vs. Pokemon\'s Index')
        plt.show()
        return(sortedSpeeds)
        
    def HighestOverall(self):
        totalList = allPokemon['Total']
        pokemon = allPokemon['Name']
        threshold = 550
        print('\n')
        HighestTotals = {}
        print("OVERALL BEST:")
        for i in range(len(totalList)):
            if totalList[i] >= threshold:
                if allPokemon.iloc[i, 12] == False: # Legendaries removed
                    HighestTotals[pokemon[i]] = allPokemon.iloc[i, 4]
        sortedTotals = sorted(HighestTotals.items(), key=operator.itemgetter(1))
        for i in range(len(sortedTotals)):
            print(sortedTotals[i])
        plt.figure(figsize = (10, 5))
        plt.title('Overall Highest Stat Pokemon')
        plt.grid()
        plt.ylabel('Overall Summed Base Stats')
        plt.bar(range(len(HighestTotals)), list(HighestTotals.values()), align='center', color = 'purple', alpha = 0.5)
        plt.xticks(range(len(HighestTotals)), list(HighestTotals.keys()), rotation = -45)
        plt.ylim(500, 700)
        plt.show()
        
def main():
    pokedex = Pokedex()
    pokedex.TypeScatter()
    pokedex.HighestHp()
    pokedex.HighestAttackers()
    pokedex.HighestDefenders()
    pokedex.HighestSpAttackers()
    pokedex.HighestSpDefenders()
    pokedex.HighestSpeeds()
    pokedex.HighestOverall()
    return(0)
    
if __name__ == "__main__":
    main()

"""
# Scatter plot Attack and Defense of firstGen Pokemon
    # We are classifying by Type 1 of each Pokemon
sns.lmplot(x = 'Attack', y = 'Defense', data = firstGen,
           fit_reg = False, hue = 'Type_1', size = 5, aspect = 1.5)
plt.title('Attack and Defense of Gen 1 Pokemon by Primary Type')

# Scatter plot Special Attack and Special Defense of firstGen Pokemon
    # We are classifying by Type 1 of each Pokemon
sns.lmplot(x = 'Sp_Atk', y = 'Sp_Def', data = firstGen,
           fit_reg = False, hue = 'Type_1', size = 5, aspect = 1.5)
plt.title('Sp. Atk and Sp. Def of Gen 1 Pokemon by Primary Type')
plt.show()

# Plotting speed of firstGen Pokemon
    # We are classifying by Type 1 of each Pokemon
sns.lmplot(x = 'Number', y = 'Speed', data = firstGen, 
           fit_reg = False, hue = 'Type_1', size = 5, aspect = 1.5)
plt.title('Speed of Gen 1 Pokemon by Primary Type')
plt.show()
       
"""
