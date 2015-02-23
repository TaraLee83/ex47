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

  	
  	        #U = iter(user)
#V = U.next()


    if token in directions:
        go = direction('stuff', token, current_space)
    if token in actions:
        go = action('stuff', token, current_space)"""
        
user = ["go to north run away"]

directions = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
actions = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: directions, 1: actions}

    
def __init__(self, current_space):
    self.current_space = current_space
    
def scene(self, current_space):
    print "at scene"
    go = encounter('stuff', current_space)
    
def encounter(self, current_space):
    print "at encounter"
    go = incoming('stuff', current_space)
    
def incoming(self, current_space):
    print "at incoming"
    go = present('stuff', current_space)
      

def present(self, current_space):
    x = str(user)
    for keys in directory:
        for subkeys in directory[keys]:
            token = subkeys
            break   
    waldo = x.find(token)
    if waldo == -1:
        go = present('stuff', current_space)
    if waldo >= 0:
        go = point('stuff', token, current_space)

def point(self, token, current_space):
    if token in directions:
        print "directions"
    if token in actions:
        print "actions"
    else:  
        print "system failure"
            
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

go = scene('stuff', current_space)        