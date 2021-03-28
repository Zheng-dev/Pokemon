import csv
class Poke:
    pokedex = []

    def pokeinfo(self, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_flying,
                against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel,
                against_water, attack, base_total, capture_rate, classification, defense, exp_growth, height, hp, jp_name, name, percent_male, percent_female,
                pokedex_num, sp_attack, sp_defense, speed, type1, type2, weight, generation, is_legendary, base_egg_steps, base_happiness,
                ability1, ability2, ability3, ability4, ability5) :

        #identification
        self.name = name
        self.jp_name = jp_name
        self.pokedex_num = pokedex_num
        self.classification = classification
        self.height = height
        self.weight = weight

        #additional details
        self.generation = generation
        self.is_legendary = is_legendary
        self.percent_male = percent_male
        self.percent_female = percent_female
        self.capture_rate = capture_rate
        self.exp_growth = exp_growth

        #base stats
        self.base_egg_steps = base_egg_steps
        self.base_happiness = base_happiness
        self.base_total = base_total

        #combat stats
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp.defense
        self.speed = speed

        #types and abilities
        self.type1 = type1
        self.type2 = type2
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.ability4 = ability4
        self.ability5 = ability5

        #type interactions
        self.against_bug = against_bug
        self.against_dark = against_dark
        self.against_dragon = against_dragon
        self.against_electric = against_electric
        self.against_fairy = against_fairy
        self.against_fight = against_fight
        self.against_fire = against_fire
        self.against_flying = against_flying
        self.against_ghost = against_fire
        self.against_grass = against_grass
        self.against_ground = against_ground
        self.against_ice = against_ice
        self.against_normal = against_normal
        self.against_poison = against_poison
        self.against_psychic = against_psychic
        self.against_rock = against_rock
        self.against_steel = against_steel
        self.against_water = against_water



pokemon_list = []

file_to_open = "pokemon.csv"
with open(file_to_open,'r', encoding ="utf8") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=",")
    next(this_csv_reader)
    for row in this_csv_reader:
        temp_abilities_list = []
        abilities = row[0]
        print(abilities)
        for i in abilities:
             if(i not in temp_abilities_list):
                temp_abilities_list.append(i)





