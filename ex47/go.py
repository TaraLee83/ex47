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
        