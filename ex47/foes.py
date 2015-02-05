#random attack 

import random

class RandRoll(object):

    def attack_roll(self):
        n = random.randint(1, 10)
        #Send attack if these numbers are rolled, otherwise let pass.
        if n == 2:
            print "attack"
        elif n == 5:
    	    print "attack"
        elif n == 7:
    	    print "attack"
        else:
    	    go = self
    	    go.friendly_roll()
	
    def friendly_roll(self):
        n = random.randint(1, 10)
        #Friendly appears if these numbers are rolled, otherwise, no event.
        if n == 1:
            print "friendly"
        elif n == 3:
    	    print "friendly"
        elif n == 5:
    	    print "friendly"
        else:
    	    print "no encounter"
 
    

go = RandRoll()    
go.attack_roll()


         