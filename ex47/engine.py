from tile_desc import scene
from graph import graph
#from encounters import encounter

direction = {'north': -6, 'east': 1,
            'south': 6, 'west': -1
            }		    
action = {'sleep': +3, 'open bag': 0, 
	     'sing': +1
	     }
directory = {0: direction, 1: action}

class Engine(object):
    
    def __init__(self, current_space):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
        self.current_space = current_space
        
    def scene(self, current_space):
        print scene[int(current_space)]
        self.encounter(current_space)
        
#Lookup area, run get_resistance func which provides percent-chance to defend against local foes.
#Lookup bag and if local weapon, get weapon health and skill,
#Pass to move_or_act to allow user to navigate.
    def encounter(self, current_space):
        print "at encounter"
        self.move_or_act(current_space)
        
    def move_or_act(self, current_space):
    ###Take input, lookup in dict, run changes if key in dict, otherwise print error and recycle.																																																																																																																																																																																																																																																							
        user = raw_input(">  ")
        good_value = 0
        for key in directory:
            for subkey in directory[key]:
	            if subkey in user:
		            good_value = 1
		            self.point(subkey, current_space)
	
	    if good_value == 0:
	        print "I'm afraid I didn't understand your command. Please try again."
	        self.move_or_act(current_space)
		    
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
            self.move_or_act(current_space)
            
    def actions(self, subkey, current_space):
        pass





	    
current_space = 34

go = Engine(current_space)
go.move_or_act(current_space)