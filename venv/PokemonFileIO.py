import PokeClass
import csv

pokemon_list = []
file_to_open = "pokemon.csv"
with open(file_to_open,'r', encoding ="utf8") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=",")
    header = next(this_csv_reader)
    print(header)
    for row in this_csv_reader:

        #abilties is a string, so this portion removes any unneeded char
        #and then splits them up in a list of abilities
        newstring = row[0].replace('[','')
        newstring = newstring.replace(']', '')
        newstring = newstring.replace("'", '')
        newstring = newstring.replace(" ", '')
        temp_abilities_list = newstring.split(',')


        #removes any duplicate abilities from the list
        abilities_list = []
        for i in temp_abilities_list:
            if i not in abilities_list:
                abilities_list.append(i)

        ba_bug, ba_dark, ba_dragon, ba_electric = row[1], row[2], row[3], row[4]        #battle aganst bug, dark, dragon, and electric types
        ba_fairy, fight, fire, flying = row[5], row[6], row[7], row[8]                  #battle against fairy, fighting, fire, and flying types
        ba_ghost, ba_grass, ba_ground, ba_ice = row [9], row[10], row[11], row[12]      #battle against ghost, grass, ground, and ice types
        ba_normal, ba_poison, ba_psychic, ba_rock = row[13], row[14], row[15], row[16]  #battle against normal, poison, psychic, and rock types
        ba_steel, ba_water = row[17], row[18]                                           #battle against steel and water types

        #pokemon battle stats (hp, attack, defense, sp attack, sp defense, speed)
        attack_stat, defense_stat = row[19], row[25]
        sp_attack_stat, sp_defense_stat = row[33], row[34]
        hp_stat, speed = row[28], row[35]


        poke_en_name, poke_jp_name, poke_num = row[30], row[29], row[32]                #pokemon's english name, japanese name, and pokedex entry #
        poke_height, poke_weight, poke_gene = row[27], row[38], row[39]                 #pokemon's height, weight, and generation they're from
        poke_type1, poke_type2, poke_is_legend = row[36], row[37], row[40]              #pokemon's types and if they're a legendary or not
        poke_class = row[24]                                                            #pokemon's classification

        base_egg, base_happy, base_stats = row[20], row[21], row[22]                    #base eggs steps, base happiness, and a pokemon's total base stats
        male_ratio, rate = row[31], row[23]                                             #pokemon's gender chance, and their chances to be captured
        needed_exp = row[26]                                                            #total amount of exp needed for people to fully evolve