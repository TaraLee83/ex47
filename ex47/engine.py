from tile_desc import scene
from graph import graph
from encounters import encounter

user = ["go to sleep north run away"]

directions = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
actions = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: directions, 1: actions}

class Engine(object):
    
    def __init__(self, current_space):
        self.current_space = current_space
        
    def scene(self, current_space):
        print scene[int(current_space)]
        self.encounter(current_space)
        
    def encounter(self, current_space):
        print "at encounter"
        self.incoming(current_space)
        
    def incoming(self, current_space):
        print "at incoming"
        user = raw_input(["direction?>  "])
        print user
    






	    
current_space = 5

go = Engine(current_space)
go.scene(current_space)