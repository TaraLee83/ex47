import random
from tile_desc import scene
from graph import graph, foe_map
from library import *



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

### When encounter is rolled on passive_encounter square. Remain in encounter until exit scene is triggered
###
    def passive_encounter(self, current_space):
        ###print intro scene, pass to input, when exit is triggered return to self.scene(current_space)
        current_dict = encounter_directory[current_space]
        print encounter[current_space][0]
        user = raw_input("> ")
        for key in current_dict:
            if key in user:
                value = current_dict[key]
                if value == 2:
                    print encounter[current_space][value]
                    #self.scene(current_space)
                elif value != 2:
                    print encounter[current_space][current_dict[key]]
            #if key in user and current_dict[key] == 2:
             #   print "back to scene"    

###Is input action or encounter

### When no attack is rolled            
    def user_input(self, current_space):
    ###Take input, lookup in dict, run changes if key in dict, otherwise print error and recycle.																																																																																																																																																																																																																																																							
        user = raw_input(">  ")
        good_value = 0
        for key in main_directory:
            for subkey in main_directory[key]:
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
        elif subkey in encounter_directory[current_space]:
            self.passive_encounter(current_space)        
		 
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
go.user_input(current_space)