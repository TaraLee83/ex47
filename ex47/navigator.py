#Receive direction key, access value within formula, decide if move is possible. If so- move, if not- say so.
from graph import graph
from tile_desc import scene

user = ["go to sleep north to run east away"]

directions = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
actions = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: directions, 1: actions}


def test_move(self, token, current_space):
    step = directions[token]
    possible = step + current_space
    if possible in graph[current_space]:
        print "You can go this way."
    else:
        print "You can't go this way."

    
current_space = 12    
token = 'south'
go = test_move('stuff', token, current_space)
	       
