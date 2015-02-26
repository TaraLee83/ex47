user = ["go to north run away"]

directions = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
actions = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: directions, 1: actions}


def present(self, current_space):
    for keys in directory:
        for subkeys in directory[keys]:
	    print "at present loop"
            token = subkeys
            print token
            go = waldo('stuff', token, current_space)
               
def waldo(self, token, current_space):
    print "at waldo"
    x = str(user)
    
    waldo = x.find(token)

    if waldo == -1:
        pass
    if waldo >= 0:
        go = stop('stuff', waldo, current_space)

    
    
def stop(self, waldo, current_space):
    print "at stop"

    #if waldo == -1:
    #    go = present('stuff', current_space)
   # if waldo >= 0:
      #  go = point('stuff', token, current_space)



current_space = 15

go = present('stuff', current_space)