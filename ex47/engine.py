from tile_desc import scene
from graph import graph
from encounters import encounter

direction = raw_input("direction?  >")

class Engine(object):
    var = 'o'
  
    directions = {'north': 1, 'east': 2,
		  'south': 3, 'west': 4
		 }
		    
    actions = ['sleep', 'open bag', 'sing']
    
    def go(self, current_space):
        print Engine.directions
        map(direction, Engine.directions)
    
#for each object in direction check each object in directions
 

        
        
current_space = 16
test = Engine()
test.go(current_space)     


Engine.directions[direction]