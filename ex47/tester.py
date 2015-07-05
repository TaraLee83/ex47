import random
from sys import exit
from tile_desc import tile_d
from format_incoming import format_text
from help_f import help_func
from input_parsing import (encounter_directory, Blacksmith_Inp, Desert_Scholar_Inp, Herbalist_Inp, Meadow_Mystic_Inp, 
Memory_Nymphs_Inp, Merchant_Inp, Sorrow_Lake_Inp, The_Beginning)
from maps import actions_map, graph, foe_map, tile_loc, gather_map, weapon_efficacy_map
from merchant import sell, merchant_func
from sorrow_lake import sorrow_lake_2
from scenes import (The_Beginning_Scenes, Red_Dragon_Scenes, Green_Dragon_Scenes, Gold_Dragon_Scenes, Scorpian_Scenes,
Spewer_Scenes, The_Sorrow_Lake_Scenes, The_Sorrow_Island_Scenes, Tree_Disease_Scenes, Twiggins_Scenes, 
Twiggins_Swarm_Scenes, Blacksmith_Scenes, Herbalist_Scenes, Desert_Scholar_Scenes, Meadow_Mystic_Scenes,
Memory_Nymphs_Scenes, Merchant_Scenes, Tile_Change_Scene, White_Dragon_Scenes, Winner)
from sorrow_func import the_sorrow
from bag import *
from hp import *

###get input string, copy all keys found within to list. If only a main trigger word, i.e., sell
###was input, request more information. If two appropriate keys were entered funnel to matching
###function.
words = "Something to write home about."
keys = {"Something": 0, "home": 0}
listed = words.split()

onward = []


def check_it(self):
    for key in keys:
        if key in listed:
            onward.append(key)
        else:
            pass
    print onward

def count_keys(self):
    pass



def passive_encounter(self, current_space):
    current_scenes = encounter[current_space]
    current_dict = encounter_directory[current_space]
    intro_scene = current_scenes[0]
    print format_text('self', intro_scene)
    val = 0
    c = 0

    while val != 1:
        u_i = raw_input("> ")
        key_list = list_from_input('self', current_space, u_i)

        if len(key_list) == 0:
            print current_scenes[5]
        elif len(key_list) != 0:
            for item in key_list:
                c += 1
                if current_dict[item] == 1:
                    val = 1
                else:
                    ###all options that return functionality for trade, sell etc. Post assignment of a and b
                    continue    
    
    print format_text('self', current_scenes[1])
    
            


def list_from_input(self, current_space, u_i):
    current_dict = encounter_directory[current_space]
    key_list = []
    c = 0

    while c < len(current_dict): 
        itemized = u_i.split()

        for key in current_dict:
                c += 1
                if key in itemized:
                    key_list.append(key)
                elif key not in itemized:
                    continue              
    else:
        return key_list                     



test = passive_encounter('self', 8)