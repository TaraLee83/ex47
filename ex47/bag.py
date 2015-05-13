from book import *
from sys import exit
###Bag Functionality

#Add bag triggers gather, use to point meth
bluebells = "A bell shaped blue flower of light powdery fragrance. "
cactus_flower = "A white bloom, soft. Reminescent of a lily but with a green bulb beneath "
" the convergence of the blooms, that covered in wiry hairs."
book = "words"
##############################

consumables = [bluebells, cactus_flower]


specialty = {}


#name added to bag. desc. meth run with item used. item deleted from bag when used
def bag(self, current_space):
    u_input = raw_input("What item would you like to use?  ")
    while u_input != "close bag":
        if u_input == "bluebells":
            print health_booster(5)
        elif u_input == "cactus flower":
            print health_booster(7)
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

#use_bag_item = {"book": book('self'), "bluebells": health_booster(5), "cactus_flower": health_booster(5)}
hero_hp = 30
current_space = 20

go = bag('self', current_space)