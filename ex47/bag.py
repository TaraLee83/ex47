from sys import exit
from book import *
from maps import *
from library import *

###Bag Functionality

#Add bag triggers gather, use to point meth

##############################

bag_contents = [["book"], ["weapons", "dagger", "polearm"], ["medicinals", "salve"]]
#bag_contents = [book]
bag_description = {"book":{0: "A dusty faded red tome, pungeant with time and forgotten magic."},
"bluebells":{10: "A bell shaped blue flower of light powdery fragrance."}, 
"cactus_flower":{10: "A white bloom, soft. Reminescent of a lily but with a green bulb beneath "
"the convergence of the blooms, that covered in wiry hairs."}, "dagger":{-15: "A knife with a jagged edge." }}

def add_to_bag(self, current_space):
    if current_space in gather_index:
        item = gather_index[current_space]
        bag_contents.append(item)
        print "You put %s in your bag." % gather_map[current_space]
        print bag_contents
    else:
        print "There is nothing here to take." 

def del_from_bag(self, item):
#ITEM NEEDS TO PASSED IN AS EITHER 1 OR 2
    if len(bag_contents[item]) > 1:
        if item == 2:
            medicinals = bag_contents[2]
            medicinals.pop(1)            
        elif item == 1:    
            weapons = bag_contents[1]
            weapons.pop(1)

        print "    Your bag feels a little bit lighter."  

    else:
        pass


              

#name added to bag. desc. meth run with item used. item deleted from bag when used
def bag(self, current_space):
#Parse input, check if requested item is in bag, return usage from related meth.
    print
    u_input = raw_input("What item would you like to use?  ")
    while u_input != "close bag":
        if u_input == "bluebells":
            print health_booster(5)
        elif u_input == "honeysuckle":
            print health_booster(5)    
        elif u_input == "cactus flower":
            print health_booster(5)
        elif u_input == "book":
            print book('stuff') 
        else:
            print "nope"

        go = bag('stuff', current_space)

    print "You close the bag."
    exit(1)            

def health_booster(booster):
    ###tie in to hero_hp
    hero_hp = 30
    hero_hp = booster + hero_hp
    return hero_hp

def book(self):
    left, right = 0,0
    print pages[left][right]
    u_input = raw_input("> ")
    while left < (len(pages) - 1):
        if "turn" in u_input:
            left = left + 1
            print pages[left][right]
            u_input = raw_input("> ")
        elif "close" or "shut" in u_input:
            print "close"
            break    
    else:
        print "     You turn the last page over and close the book"

    #def strength_booster(self):
    #   pass

