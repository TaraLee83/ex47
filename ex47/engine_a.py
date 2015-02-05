from tile_desc import scene


class Engine(object):
        
    directions = {'north': -6, 'east': +1, 
	          'south': +6, 'west': -1
	         }		    
    actions = {'sleep': +3, 'open bag': 0, 
	       'sing': +1
	      }
    directory = {0: directions, 1: actions}
    
    def __init__(self, current_space):
        self.current_space = current_space
        
    def scene(self, current_space):
        print scene[int(current_space)]
        self.encounter(current_space)
        
    def encounter(self, current_space):
        print "at encounter"
        self.incoming(current_space)
        
    def incoming(self, current_space):
        user = raw_input("direction?>  ")
        
        for key in directory:
            for subkey in directory[key]:
                if subkey in user:
                    if subkey in directions:
                        print "yay"
                    elif subkey in actions:
                        print "woohoo!"
           
                
	    	  
	    
	
	
		
	#all values in directory
	#all values attatched to the values in directory (directions)
	#if value in user
	#key = 0
	#subkey = east
	
	#look at all values attatched to the values in directory (directions)
	#all values in directory
	

	
	
    def go(self, current_space, user):       
        proposed = 0
        
        if 'north' in user:
	    proposed -= 6
        elif 'east' in user:
            proposed += 1
        elif 'south' in user:
            proposed += 6
        elif 'west' in user:
            proposed -= 1
        else:
	    print "not working."
	
	print current_space
        current_space = proposed + current_space
        print current_space
  	
        
    def do(self, current_space, user):
        print "at do"      
        
        
      
        
        
        
        
#        else:
#	    print "not working."

        
 #       if self.proposed >= 1:
#	        current_space = self.proposed + current_space
#	        print current_space
#	        self.scene(current_space)
#	    else:
#	        print "The way here is blocked. You must go another way."
#	        self.scene(current_space)
#	    



	    
current_space = 5

go = Engine(current_space)
go.scene(current_space)


"""1 2 3 4  5 6
7 8 9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36
"""

"""initialize starting place with class instantiation. Desc prints. Encounter happens or doesn't. Blank prompt appears. At any time bag may be accessed. 
   Health data is stored and may be accessed at any time through prompt."""

        
"""   for i in user:
	    if i in Engine.directions:
	        print i
                direction = directions[user]
                print direction
            elif user in Engine.actions:
                self.do(current_space, user)
	    else:
	        print "Your health is too low to move, you must rest.
	        
	        and ((current_space - 6) >= 0)
	        
	                direction = Engine.directions[user]
        
        if direction == 'north':
	    current_space -= 6
        elif ('east' in user) and ((current_space + 1) != 7 or 13 or 19 or 25 or 31 or 37):
            current_space += 1 
        elif ('south' in user) and ((current_space + 6) <= 36):
            current_space += 6
        elif ('west' in user) and ((current_space - 1) != 0 or 6 or 12 or 18 or 24 or 31):
            current_space -= 1
        else:
  	    print "not working.
  	"""