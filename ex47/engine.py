import random
from tile_desc import scene
from graph import graph, foe_map
from library import encounter, Dragons, Hero, Meadow_Mystic, Scorpians, Spewer, Tree_Disease, Twiggins


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
        
###Encounters        
    def encounter_roll(self, current_space):
        x = random.randint(1, 5) 
        y = 4
        if x == y:
            self.map_encounter(current_space)
        elif x != y:
            self.user_input(current_space)
           
    def map_encounter(self, current_space):
        gen_foe = foe_map[current_space]
        path = 'none'

        if 'Twiggins' in gen_foe:
            inc_attacker = 'Twiggins'
            path = 'attack'
            print "Twiggins attack!"
        elif 'Tile_Change' in gen_foe:
            inc_attacker = 'Tile_Change'
            path = 'attack'
            print 'Tile_Change'    
        elif 'Dragons' in gen_foe:
            inc_attacker = 'Dragons'
            path = 'attack'
            print inc_attacker
        elif 'The_Sorrow' in gen_foe:
            inc_attacker = 'The_Sorrow'
            path = 'attack'
            print "Attack of Sorrow!"
        elif 'Scorpion' in gen_foe:
            inc_attacker = 'Scorpion'
            path = 'attack'
            print "Scorpion attack!"
        elif 'Spewer' in gen_foe:
            inc_attacker = 'Spewer'
            path = 'attack'
            print "Spewer attack!"
        elif 'Memory_Nymphs' in gen_foe:
            inc_attacker = 'Memory_Nymphs'
            path = 'attack'
            print "Memory_Nymphs attack!"            
        elif 'Tree_Disease' in gen_foe:
            inc_attacker = 'Tree_Disease'
            path = 'attack'
            print "Tree_Disease attack!" 
        elif 'Meadow_Mystic' in gen_foe:
            inc_friendly = 'Meadow_Mystic'
            path = 'friendly'
            print "Meadow_Mystic"  
        elif 'Desert_Scholar' in gen_foe:
            inc_friendly = 'Desert_Scholar'
            path = 'friendly'
            print 'Desert_Scholar'                         
        elif 'Herbalist' in gen_foe:
            inc_friendly = 'Herbalist'
            path = 'friendly'
            print "Herbalist encounter"            
        elif 'Blacksmith' in gen_foe:
            inc_friendly = 'Blacksmith'
            path = 'friendly'
            print "Blacksmith encounter"
        else:
            print "none" 

        if path == 'friendly':
            self.friendlies(inc_friendly, current_space)
        elif path == 'attack':
            self.foe_attack(inc_attacker, current_space)

### When no ecounter is rolled            
    def user_input(self, current_space):
    ###Take input, lookup in dict, run changes if key in dict, otherwise print error and recycle.																																																																																																																																																																																																																																																							
        user = raw_input(">  ")
        good_value = 0
        for key in directory:
            for subkey in directory[key]:
	            if subkey in user:
		            good_value = 1
		            self.point(subkey, current_space)
	
	    if good_value == 0:
	        print "I'm afraid I didn't understand your command. Please try again."
	        self.user_input(current_space)
		    
    def point(self, subkey, current_space):
        if subkey in direction:
            self.test_move(subkey, current_space)
        elif subkey in action:
            self.action(subkey, current_space)
		 
    def test_move(self, subkey, current_space):
        step = direction[subkey]
        possible = step + current_space
        if possible in graph[current_space]:
            current_space = possible
            self.scene(current_space)
        else:
            print "You can't go this way."
            self.user_input(current_space)
            
    def action(self, subkey, current_space):
        ###Check actions list [action[current_space, command], other_action[current_space, command]]
        pass





	    
current_space = 34

go = Engine(current_space)
go.user_input(current_space)