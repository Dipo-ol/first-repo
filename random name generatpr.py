import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']
num = [23, 45, 65, 23, 76]


def capitalize_suffix(suffix):
    name = suffix.capitalize()
    return name


def fire_in_name(name):
    return 'Fire' in name


def concatenate_names(name_1, name_2):
    return name_1 + '' + name_2


def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + random.choice(list_2) + str(random.choice(num))


try:
    capped = list(map(capitalize_suffix, suffixes))

    random_name = [create_fantasy_name(prefixes, capped) for i in range(1)]
   
    fire_benders = list(filter(fire_in_name, random_name))
   
    try:
        reduced_benders = reduce(concatenate_names, fire_benders)
    except:
        reduced_benders = 'no words to reduce'
except:
    print('something went wrong')


def display_info(list1, list2, list3):
    for name in list1:
        print(name)
    try:
        print('\nname with fire:', list2)
        print('reduced names :', list3)
    except:
        print("no such name")


create_fantasy_name(prefixes, suffixes)
display_info(random_name, fire_benders, reduced_benders)
