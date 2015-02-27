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
        go = referee('stuff', current_space)
    else:
        print x,"no"
        
def referee(self, current_space):
    x = encounter[current_space]
    if 'Dragonlands' in x:
        go = dragonlands('stuff', current_space)
    elif 'Meadow' in x:
        pass
    elif 'Desert' in x:
        pass
    elif 'Forest' in x:
        pass

    
def dragonlands(self, current_space):
    print "at dragonlands"
 
        
current_space = 10
go = referee('stuff', current_space)
    
