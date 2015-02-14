#Receive and analyze user input then direct game to next area

import re

directions = {'north': -6, 'east': +1, 
	      'south': +6, 'west': -1
	     }		    
actions = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: directions, 1: actions}




def incoming(self, current_space, user):
    print "at incoming"
    print user
    p = re.compile(user, re.IGNORECASE)
    print p
    for keys in directory:
        for subkeys in directory[keys]:
            p.match(subkeys)
            print p.match(subkeys)
      
	    
    
    
user = raw_input("> ")
current_space = 15

incoming('stuff', current_space, user)    