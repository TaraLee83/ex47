import random
from tile_desc import scene
from graph import graph

direction = {'north': -6, 'east': 1, 
	      'south': 6, 'west': -1
	     }		    
action = {'sleep': +3, 'open bag': 0, 
	   'sing': +1
	  }
directory = {0: direction, 1: action}

class Engine(object):
    
    def __init__(self, current_space):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
        self.current_space = current_space
        
    def scene(self, current_space):
        print scene[int(current_space)]
        self.encounter_roll(current_space)
        
    def encounter_roll(self, current_space):
        x = random.randint(1, 5) 
        y = 4
        if x == y:
            self.map_encounter(current_space)
        else:
            print "No encounter rolled."
#If encounter is rolled            
    def map_encounter(self, current_space):
        x = encounter[current_space]
        if 'Meadow_Gen' in x:
            print "Some sort of Meadow AATTTAAACK!"
        elif 'Twiggins' in x:
            print "Twiggins attack!"
        elif 'Dragons' in x:
            print "Dragon Attack!"
        elif 'The_Sorrow' in x:
            print "Attack of Sorrow!"
	elif 'Scorpion' in x:
	    print "Scorpion attack!"
	elif 'Spewer' in x:
	    print "Spewer attack!"
        
    def foe_attack(self, inc_attacker, current_space):
        foe = inc_attacker
        chooser = random.choice(foe)
        group = random.choice(chooser[1:5])
        intro = chooser[0:1]
        val = group[0:1]
        beginning = str(group[1:2])
        end = str(group[2:3])
        roll = random.randint(0, 4)
        health = sum(hero_hp)
        change = sum(val)
        new_val = health + change
        update = "Your health went from %r to %r." % (health, new_val)
        complete = beginning + end + update
        complete = complete.replace("[", "")
        complete = complete.replace("]", "")
        complete = complete.replace("'", " ")
        print complete  
#If no encounter is rolled.
    def user_input(self, current_space):																																																																																																																																																																																																																																																							
        user = raw_input(">  ")
        good_value = 0
        for key in directory:
            for subkey in directory[key]:
	        if subkey in user:
		    good_value = 0
		    print "got subkey, it's r%." % subkey
		    #self.point(subkey, current_space)
	
	if good_value == 0:
	    print "I'm afraid I didn't understand your command. Please try again."
	    self.user_input(current_space)
        
        
	    
current_space = 34

go = Engine(current_space)
go.scene(current_space)        