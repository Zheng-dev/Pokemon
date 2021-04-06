from PokeClass import Pokemon
from termcolor import colored, cprint
from PIL import Image
import PlayGame
import csv
import re
import os

POKEDEX = []


def start():
    read_csv_file()


def read_csv_file():
    file_to_open = "pokemon.csv"
    with open(file_to_open, 'r', encoding="utf8") as this_csv_file:
        this_csv_reader = csv.reader(this_csv_file, delimiter=",")
        header = next(this_csv_reader)

        for row in this_csv_reader:

            # abilties is a string, so this portion removes any unneeded char
            # and then splits them up in a list of abilities
            newstring = row[0].replace('[', '')
            newstring = newstring.replace(']', '')
            newstring = newstring.replace("'", '')
            newstring = newstring.replace(" ", '')
            temp_abilities_list = newstring.split(',')

            # removes any duplicate abilities from the list
            abilities_list = []
            for i in temp_abilities_list:
                if i not in abilities_list:
                    abilities_list.append(i)

            # battle aganst bug, dark, dragon, and electric types
            ba_bug, ba_dark, ba_dragon, ba_electric = float(row[1]), float(row[2]), float(row[3]), float(row[4])

            # battle against fairy, fighting, fire, and flying types
            ba_fairy, ba_fight, ba_fire, ba_flying = float(row[5]), float(row[6]), float(row[7]), float(row[8])

            # battle against ghost, grass, ground, and ice types
            ba_ghost, ba_grass, ba_ground, ba_ice = float(row[9]), float(row[10]), float(row[11]), float(row[12])

            # battle against normal, poison, psychic, and rock types
            ba_normal, ba_poison, ba_psychic, ba_rock = float(row[13]), float(row[14]), float(row[15]), float(row[16])

            # battle against steel and water types
            ba_steel, ba_water = float(row[17]), float(row[18])

            # pokemon battle stats (hp, attack, defense, sp attack, sp defense, speed)
            attack_stat, defense_stat = int(row[19]), int(row[25])
            sp_attack_stat, sp_defense_stat = int(row[33]), int(row[34])
            hp_stat, speed_stat = int(row[28]), int(row[35])

            # pokemon's english name, japanese name, and pokedex entry
            poke_en_name, poke_jp_name, poke_num = row[30], row[29], row[32]

            # pokemon's height, weight, and generation they're from
            poke_height, poke_weight, poke_gene = row[27], row[38], row[39]

            # pokemon's types and if they're a legendary or not
            poke_type1, poke_type2, poke_is_legend = row[36], row[37], int(row[40])

            # pokemon's classification
            poke_class = row[24]

            # base eggs steps, base happiness, and a pokemon's total base stats
            base_egg, base_happy, base_stats = int(row[20]), int(row[21]), int(row[22])

            # total amount of exp needed for people to fully evolve
            needed_exp = int(row[26])

            # pokemon's gender chance, and their chances to be captured
            male_ratio, rate = row[31], row[23]

            # takes care of pokemon with no gender
            if male_ratio == '':
                male_ratio = 101

            male_ratio = float(male_ratio)

            # removes any characters
            rate = int(''.join(filter(str.isdigit, rate)))

            im = import_images(poke_num)
            POKEDEX.append(Pokemon(ba_bug, ba_dark, ba_dragon, ba_electric, ba_fairy, ba_fight, ba_fire, ba_flying,
                                   ba_ghost, ba_grass, ba_ground, ba_ice, ba_normal, ba_poison, ba_psychic, ba_rock,
                                   ba_steel, ba_water, attack_stat, base_stats, rate, poke_class, defense_stat,
                                   needed_exp, poke_height, hp_stat, poke_jp_name, poke_en_name, male_ratio, poke_num,
                                   sp_attack_stat,sp_defense_stat, speed_stat, poke_type1, poke_type2, poke_weight,
                                   poke_gene,poke_is_legend, base_egg, base_happy, abilities_list, im))


def display_pokedex():
    fmt = '{:<10} {:<25} {:<10} {:<10} {:<45}'
    fmt1 = '{:<10} {:<16} {:<10} {:<13} {:<50} {:<10}'
    print(fmt1.format("Dex #", "en name", "type 1", "type 2", "jp name", "abilities"))
    for i in POKEDEX:
        if i.is_legendary == 1:
            print(fmt.format(i.pokedex_num, colored(i.en_name, 'yellow'),
                             i.type1, i.type2, colored(i.jp_name, 'yellow')), "\t \t", i.abilities)
        else:
            print(fmt.format(i.pokedex_num, colored(i.en_name, 'white'),
                             i.type1, i.type2, colored(i.jp_name, 'white')), "\t \t", i.abilities)


def import_images(dex_num):
    im_list = []
    for file in os.listdir("pokemon_images"):
        if re.match("/[^0-9.,]+/", file):
            print("image#", dex_num, " ", file)
            im = Image.open(file)
    return im_list
