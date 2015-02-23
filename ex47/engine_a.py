from tile_desc import scene
from interpret import present, point

user = ["go to north run away"]

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
        self.present(current_space)

    def point(self, current_space):
        print "at point"
            
    def test_move(self, token, current_space):
        step = directions[token]
        possible = step + current_space
        if possible in graph[current_space]:
            current_space = possible
            self.scene(self, current_space)
        else:
            print "You can't go this way."
            self.scene(self, current_space)
                




token = 0	    
current_space = 5

go = Engine(current_space)
go.scene(current_space)