from random import randrange

def which_gender(chance):
    male_chance = chance
    gender = ''

    if chance == 101:
        gender = "Neutral"
    else:
        generate_chance = randrange(1, 101)
        if generate_chance <= male_chance:
            gender = "Male"
        else:
            gender = "Female"
    return gender


def which_ability(ability_list):
    index = randrange(len(ability_list))

    return (ability_list[index])