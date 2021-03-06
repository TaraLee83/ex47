import random
from sys import exit
from tile_desc import tile_d
from format_incoming import format_text
from help_f import help_func
from input_parsing import (action_directory, encounter_directory, Blacksmith_Inp, Desert_Scholar_Inp, Herbalist_Inp, Meadow_Mystic_Inp, 
Memory_Nymphs_Inp, Merchant_Inp, Sorrow_Lake_Inp, The_Beginning)
from maps import actions_map, graph, foe_map, item_map, tile_loc, weapon_efficacy_map
from merchant import sell, merchant_func
from sorrow_lake import sorrow_lake_2
from scenes import (encounter, The_Beginning_Scenes, Red_Dragon_Scenes, Green_Dragon_Scenes, Gold_Dragon_Scenes, Scorpian_Scenes,
Spewer_Scenes, The_Sorrow_Lake_Scenes, The_Sorrow_Island_Scenes, Tree_Disease_Scenes, Twiggins_Scenes, 
Twiggins_Swarm_Scenes, Blacksmith_Scenes, Herbalist_Scenes, Desert_Scholar_Scenes, Meadow_Mystic_Scenes,
Memory_Nymphs_Scenes, Merchant_Scenes, Tile_Change_Scene, White_Dragon_Scenes, Winner)
from sorrow_func import the_sorrow
from bag_func import *
from hp import *

###get input string, copy all keys found within to list. If only a main trigger word, i.e., sell
###was input, request more information. If two appropriate keys were entered funnel to matching
###function.

###a is either buy, sell or trade
###b is any item

def passive_encounter(self, current_space):
    current_scenes = encounter[current_space]
    current_dict = encounter_directory[current_space]
    intro_scene = current_scenes[0]
    print format_text('self', intro_scene)
    val = 0
    a, b = 0, 0
    text = 0
    action = 0
    #Check dictionary for request to exit encounter.
    while val != 1:
        u_i = raw_input("> ")
        key_list = pull_action_keys('self', current_space, u_i)
        sub_key_list = pull_sub_keys('self', current_space, u_i)
        text = check_for_dialogue('self', current_space, u_i)
        ###Need to print
        if len(text) != 0:
            print text
            #if current_dict[text] == 1:
            #        val = 1
            #else:
            #    print "hello"
        elif len(key_list) != 0:
            for action in key_list:
                a = action
                if len(sub_key_list) == 0:
                    print "What would you like to %r ?" % a
                elif len(sub_key_list) != 0:
                    b = sub_key_list
                    buy_sell_trade('self', a, b)
        elif len(sub_key_list) != 0:
            print "What would you like to do with your %r ?" % sub_key_list
            b = sub_key_list.pop()

    print format_text('self', current_scenes[1])

######################Parse input#########################################

def check_for_dialogue(self, current_space, u_i):
    current_dict = encounter_directory[current_space]
    current_scenes = encounter[current_space]
    text = []
    c = 0

    while c < len(current_dict): 
        itemized = u_i.split()
        for key in current_dict:
                c += 1
                if key in itemized:
                    text = current_scenes[current_dict[key]]
                elif key not in itemized:
                    continue              
    else:
        return text 

def pull_action_keys(self, current_space, u_i):
    key_list = []
    c = 0

    while c < len(action_directory): 
        itemized = u_i.split()

        for key in action_directory:
                c += 1
                if key in itemized:
                    if current_space in action_directory[key]:
                        key_list.append(key)
                    elif current_space not in action_directory[key]:
                        print "You cannot %r here." % key    
                elif key not in itemized:
                    continue              
    else:
        return key_list                     

def pull_sub_keys(self, current_space, u_i):
    itemized = u_i.split()
    sub_key_list = []
    c = 0

    while c < len(itemized):
        for key in item_map:
            c += 1
            if key in itemized:
                if current_space in item_map[key][0]:
                    sub_key_list.append(key)
                elif current_space not in item_map[key]:
                    print "You cannot deal in %r here." % key    
            else:
                continue    
    else:
        return sub_key_list


################Run Functionality################################ 
###a = value of item
###b = item name
###c = value change of item       

def buy_sell_trade(self, a, b):
    a = var_index('self', a)
    for key in item_map:
        if key in b:
            price = item_map[key][a]
            n_t = price + bag_dict["Gold"]
            if n_t <= 0:
                message = "You don't have enough gold to purchase this item."
            else:
                n_t = bag_dict["Gold"]  
                message = "You now have %r gold and %r %r." % (n_t, ) 
                if 'buy' in key:
                    c = 1
                elif 'sell' in key: 
                    c = -1
                    
    

def var_index(self, a):
    if "buy" in a:
        a = 1
    elif "sell" in a:
        a = 2
    
    return a

test = passive_encounter('self', 36)



###figure out how to get to nested space number in item map