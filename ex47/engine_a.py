from tile_desc import scene

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
        
    def present(self, current_space):
        print "at present"
        x = str(user)
        for keys in directory:
            for subkeys in directory[keys]:
                token = subkeys
                
        waldo = x.find(token)
        if waldo == -1:
            self.present(current_space)
        if waldo >= 0:
            self.point(token, current_space)

    def point(self, token, current_space):
        print "at point"
        if token in directions:
            self.test_move(token, current_space)
        if token in actions:
            self.action(token, current_space)
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

go = Engine(current_space)
go.scene(current_space)