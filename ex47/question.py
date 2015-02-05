#This is part of an engine for a game.


class Engine(object):
    north = "north"
    directions1 = {north: '-6', 'east': '1',
		  'south': '6', 'west': '-1'
		 } 
    directions = ('north', 'east', 'south', 'west') 

    def __init__(self, current_space):
        self.current_space = current_space

    def go(self, current_space):
      
        user = raw_input("direction?>  ")

        print hasattr((i in Engine.directions), user)
	        
	        
start = Engine(15)
start.go(15)



#look at each key in dictionary