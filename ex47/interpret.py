#Receive and analyze user input then direct game to next area
#Dictionaries

user = ["go to sleep north to run east away"]

directions = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
actions = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: directions, 1: actions}

def present(self, current_space):    
    x = str(user)
    print len(x)
    for keys in directory:
        for subkeys in directory[keys]:
            token = subkeys
            
    waldo = x.find(token)
    if waldo == -1:
        forward = present('stuff', current_space)
    if waldo >= 0:
        print token
        go = point('stuff', token, current_space)

def point(self, token, current_space):
    if token in directions:
        go = direction('stuff', token, current_space)
    if token in actions:
        go = action('stuff', token, current_space)
    else:  
        print "system failure"

def action(self, token, current_space):
    

def direction(self, token, current_space):



token = 0
current_space = 2
run = present('stuff', current_space)