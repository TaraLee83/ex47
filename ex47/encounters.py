#encounter functionality practice space

import random
from graph import encounter

direction = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
action = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: direction, 1: action, 2:encounter}

def roll(self, current_space):
    x = random.randint(1, 5) 
    y = 4
    if x == y:
        go = map_encounter('stuff', current_space)
    else:
        print x,"no"
        
def map_encounter(self, current_space):
    x = encounter[current_space]
    if 'Dragonlands' in x:
        go = dragon_chooser('stuff', current_space)
    elif 'Meadow' in x:
        pass
    elif 'Desert' in x:
        pass
    elif 'Forest' in x:
        pass
    
def dragon_chooser(self, current_space):
    dragon = random.randint(0, 2)
    if dragon == 0:
        red_dragon('stuff', current_space)
    elif dragon == 1:
        green_dragon('stuff', current_space)
    elif dragon == 2:
        gold_dragon('stuff', current_space)
        
def red_dragon(self, current_space):
    attack = ("go", "stay", "inbetween")
    print random.choice(attack)
    if sum(hero_hitpoints.py 
    
    
def green_dragon(self, current_space):
    print "green_dragon"
    attack = ("go", "stay", "inbetween")
    print random.choice(attack)
    
def gold_dragon(self, current_space):
    print "gold_dragon"
    attack = ("go", "stay", "inbetween")
    print random.choice(attack)
    
    
        
current_space = 10
go = dragon_chooser('stuff', current_space)
    
