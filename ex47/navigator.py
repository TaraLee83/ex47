user = raw_input("> ")    
    
def go(self, current_space, user):

    else:
        print "You can't go this way."
        
  	      

directions = {'north': -6, 
	      'east': +1, 
	      'south': +6, 
	      'west': -1
	     }
current_space = 0

test = go(directions, current_space, user)


find words in incoming string. Invoke def based on 



      
    def move(self, current_space):
        print current_space
               
        user = raw_input("> ")
        print Engine.directions.get('north')
        
        match = next(val for key, val in Engine.directions.items() if user in key)
        
        self.go(current_space, user)
