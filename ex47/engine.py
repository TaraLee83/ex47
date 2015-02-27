from tile_desc import scene
from graph import graph
from encounters import encounter

direction = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
action = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: direction, 1: action, 2:encounter}

class Engine(object):
    
    def __init__(self, current_space):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
        self.current_space = current_space
        
    def scene(self, current_space):
        print scene[int(current_space)]
        self.encounter(current_space)
        
    def encounter(self, current_space):
        print "at encounter"
        self.waldo(current_space)
        
    def pass_in(self, current_space):
        user = None
        self.waldo(current_space)
        
    def waldo(self, current_space):																																																																																																																																																																																																																																																							
        user = raw_input(">  ")
        good_value = 0
        for key in directory:
            for subkey in directory[key]:
	        if subkey in user:
		    good_value = 0
		    self.point(subkey, current_space)
	
	if good_value == 0:
	    print "I'm afraid I didn't understand your command. Please try again."
	    self.waldo(current_space)
		    
    def point(self, subkey, current_space):
        if subkey in direction:
	    self.test_move(subkey, current_space)
	elif subkey in action:
	    self.action(subkey, current_space)
		 
    def test_move(self, subkey, current_space):
        step = direction[subkey]
        possible = step + current_space
        if possible in graph[current_space]:
            current_space = possible
            self.scene(current_space)
        else:
            print "You can't go this way."
            self.scene(current_space)
            
    def actions(self, subkey, current_space):
        pass





	    
current_space = 34

go = Engine(current_space)
go.scene(current_space)