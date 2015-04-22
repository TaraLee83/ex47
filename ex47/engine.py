import random
from tile_desc import scene
from graph import graph, foe_map
from library import (encounter, Dragons, Hero, Hit_Points, Meadow_Mystic, 
Scorpian, Spewer, Tree_Disease, Twiggins)


###Input Parsing Dictionaries
direction = {'north': -6, 'east': 1,
            'south': 6, 'west': -1
            }		    
action = {'sleep': +3, 'open bag': 0, 
	     'sing': +1
	     }
###I.P.D. - Passive Encounters  
blacksmith = {'stuff': 1, 'stuff': 2, 'stuff': 3, 'stuff': 4}  
desert_scholar = {'stuff': 1, 'stuff': 2, 'stuff': 3, 'stuff': 4}
herbalist = {'stuff': 1, 'stuff': 2, 'stuff': 3, 'stuff': 4} 
meadow_mystic = {'buy': 1, 'oils': 1, 'healing': 1, 'trade': 1, 'poison': 1,
'information': 4, 'soul shard': 4, 'where': 4, 'how': 4, 'the sorrow': 5,
'daughter': 5, 'Arturia': 5, 'dragons': 5, 'Dragons': 5, 'I': 6, 'me': 6,
'family': 7, 'mother': 7, 'father': 7, 'goodbye': 10, 'thank you': 10}
white_dragon = {'stuff': 1, 'stuff': 2, 'stuff': 3, 'stuff': 4}

directory = {0: direction, 1: action, 2: blacksmith, 3: desert_scholar, 
4: herbalist, 5: meadow_mystic, 6: white_dragon}

class Game(object):
    
    def __init__(self, current_space):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
        self.current_space = current_space
        
    def scene(self, current_space):
        print scene[int(current_space)]
        self.encounter_roll(current_space)
        
### Encounters    
    def encounter_roll(self, current_space):
        p_e_list = (3, 5, 8, 9, 11, 15, 25, 29, 30)
        x = random.randint(1, 5) 
        y = 4
        if x == y and current_space not in p_e_list:
            self.attack_engine(current_space)
        elif x == y and current_space in p_e_list:
            self.passive_encounter(current_space)   
        elif x != y:
            self.user_input(current_space)
           

### When encounter is rolled on hostile square           

    def hero_health(self):
        hero_hp = Hit_Points['Hero']
        return hero_hp

    def hero_health_change(self, h_change):
        new = hero_health('self') + h_change
        for key, value in Hit_Points.items():
            Hit_Points["Hero"] = new
            if new <= 0:
                print """\tYour last breath comes quickly. Your daughter flashes before your eyes.
            She reaches out to you. You die, leaving her trapped forever.
            """
                exit(1)
        return new
 

    def foe_health_change(self, current_space, foe, f_change):
        gen_foe = foe_map[current_space]
        old_val = Hit_Points[gen_foe][foe]
        new_val = old_val + f_change
        Hit_Points[gen_foe][foe] = new_val
        return new_val
  
    def choose_attack(self, current_space):
        foe = encounter[current_space]
        foe_group = random.choice(foe)
        return foe_group          

    def defense_input(self, current_space, foe):
        user = raw_input("> ")    
    
        if 'hit' in user:
            f_change = -10
            update_line = "Your foes health is now %s." % foe_health_change('self', current_space, foe, f_change)
            return update_line

        if 'scream' in user:
            return "scream"
        else:
            not_found = "You're not even sure of what you were trying to do as you floundered to save your skin." 
            return not_found   

    def attack_engine(self, current_space):
        val = 0  
        gen_foe = foe_map[current_space]
        foe_group = self.choose_attack(current_space)
        lucky_line = "Luck favors you and the %s attack misses completely." % (str(foe_group[0:1]).strip("[]")).strip("'")
        lucky = str(foe_group[1:2]), lucky_line
    
        ###While hero is alive, while foe is alive, if first time in, if subsequent times in.
        while self.hero_health() > 0: 
            foe = (str(foe_group[0:1]).strip("[]")).strip("'")
        
            while Hit_Points[gen_foe][foe] > 0:
                roll = random.randint(0, 4)
                chosen_attack = random.choice(foe_group[2:5])

                if val == 0:
                    print str(foe_group[1:2])
                
                    if roll != 1:
                        print defense_input('self', current_space, foe)                                                                                                                                                                      
                        val = 1    
                    elif roll == 1:
                        print lucky, defense_input('self', current_space, foe)
                        val = 1

                elif val == 1:

                    if roll == 1 and val == 1:
                        print lucky_line, defense_input('self', current_space, foe)
                        val = 1
                    elif roll != 1:
                        h_change = sum(chosen_attack[0:1])
                        print chosen_attack[1:2], "Your health is now %s." % hero_health_change('self', h_change), defense_input('self', current_space, foe)
                        val = 1


            print "Your foe perishes at your feet. At surviving, you are victorious."
            #self.scene()

        print "With your last breath you scream \"Arturia!\" then you breath no more."
        exit(1)     

### When encounter is rolled on passive_encounter square
    def passive_encounter(self, current_space):
        pass

### When no attack is rolled            
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
        elif subkey in blacksmith and blacksmith in encounter[current_space]:
            pass
        elif subkey in desert_scholar:
            pass
        elif subkey in herbalist:
            pass
        elif subkey in meadow_mystic and meadow_mystic in encounter[current_space]:
            print "booyah"
        elif subkey in white_dragon:
            pass    
		 
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
        if subkey == "open bag":
            self.bag(current_space)
        else:
            print "not here"

    def bag(self, current_space):
        pass        





	    
current_space = 8

go = Game(current_space)
go.scene(current_space)