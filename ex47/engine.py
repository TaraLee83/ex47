import random
from sys import exit
from tile_desc import scene
from format_incoming import format_text
from help_f import help_func
from input_parsing import *
from maps import graph, foe_map, tile_loc, gather_map, weapon_efficacy_map
from merchant import sell, merchant_func
from sorrow_lake import sorrow_lake
from scenes import (Red_Dragon_Scenes, Green_Dragon_Scenes, Gold_Dragon_Scenes, Scorpian_Scenes,
Spewer_Scenes, The_Sorrow_Lake_Scenes, The_Sorrow_Island_Scenes, Tree_Disease_Scenes, Twiggins_Scenes, 
Twiggins_Swarm_Scenes, Blacksmith_Scenes, Herbalist_Scenes, Desert_Scholar_Scenes, Meadow_Mystic_Scenes,
Memory_Nymphs_Scenes, Merchant_Scenes, Tile_Change_Scene, White_Dragon_Scenes, Winner)
from sorrow_func import the_sorrow
from bag import *
from hp import *




class Game(object):
    
    def __init__(self, current_space):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
        self.current_space = current_space
        
    def scene(self, current_space):
        incoming = scene[int(current_space)]
        print format_text('stuff', incoming)
        self.encounter_roll(current_space)
        
### Encounters    
    def encounter_roll(self, current_space):
        i_e_list = (8, 23, 25, 29, 30)
        poison_list = (20, 21, 26, 27, 28, 35, 35, 36)
        x = random.randint(1, 5) 
        y = 4
        if current_space in i_e_list:
            self.interactive_encounter(current_space)
        elif current_space == 15:
            print merchant_func('self')
            self.user_input(current_space)
        elif current_space == 5:
            print sorrow_lake('stuff') 
            self.user_input(current_space)   
        #elif current_space == 5 or current_space == 11:
        #    a, b, c = the_sorrow('self', current_space)
        #    print a 
        #    print b 
        #    print c
        #    self.user_input(current_space)
        elif current_space == 22 or current_space == 24:
            self.user_input(current_space)         
        elif x == y:
            if current_space in poison_list:
                self.poison_encounter(current_space)
            elif 3 == current_space or 14 == current_space:
                print format_text('self', Tile_Change_Scene[0])
                current_space = random.randint(1, 36)
                self.scene(current_space)
            elif current_space == 23:
                self.memory_nymph(current_space)
            else:
                self.attack_engine(current_space)    
        elif x != y:
            self.user_input(current_space)
        

### When encounter is rolled on hostile square           
    def hero_health(self):
        hero_hp = Hit_Points['Hero']
        return hero_hp

    def hero_health_change(self, h_change):
        new = Hit_Points['Hero'] + h_change
        for key, value in Hit_Points.items():
            Hit_Points["Hero"] = new
            if new <= 0:
                print "    "
                print "    Your last breath cames quickly. Your daughter flashed before your eyes. "
                print "She reached out to you. You died and left her trapped forever."
                exit(1)
        return new
 
    def foe_health_change(self, current_space, foe, f_change):
        new_val = Hit_Points[foe] + f_change
        Hit_Points[foe] = new_val
        return new_val
  
    def choose_attack(self, current_space):
        foe = encounter[current_space]
        foe_group = random.choice(foe)
        return foe_group          

    def weapon_check(self, weapon, foe):            
        ###Check weapons efficacy, total deductions
        if weapon in weapon_efficacy_map:
            val = 0
            for subkey in weapon_efficacy_map[weapon]:
                val += 1
                if foe in subkey:
                    return True
                elif foe not in subkey and val == len(weapon_efficacy_map[weapon]):
                    return False  

    def attack_totalling(self, weapon, foe):
        return weapon_efficacy_map[weapon][foe] + bag_description[weapon].keys()[0]  

    def defense_input(self, current_space, foe):
        #CHECK FOR WEAPON BONUS, AUTO USE WEAPON/ INSTRUCTIONS FOR USE
        u_i = raw_input("> ")
        ###Check input and weapon availability, obtain damage total
        if "throw" in u_i and "obsidian disk" in bag_contents[1]:
            weapon = "obsidian disk"
        elif "thrust" in u_i and "polearm" in bag_contents[1]:
            weapon = "polearm"
        elif "stab" in u_i and "dagger" in bag_contents[1]:
            weapon = "dagger"
        elif "hit" in u_i:
            new_total = Hit_Points[foe] - 5
            Hit_Points[foe] = (Hit_Points[foe] - 5)
            return "    You punch your foe. Your foes health is now %r." % new_total
        else:
            weapon = 0

        return self.defense_input_return(u_i, weapon, foe)    

    def defense_input_return(self, u_i, weapon, foe):            
        if weapon == 0:  
            return "    You flounder and lose ground."  
        elif weapon != 0:
            if self.weapon_check(weapon, foe) == True:
                new_total = Hit_Points[foe] + self.attack_totalling(weapon, foe)
                Hit_Points[foe] = new_total
                return "    You %s your %s. Your foes health is now %r." % (u_i, weapon, new_total)

            elif self.weapon_check(weapon, foe) == False:
                return "    This weapon is useless against your foe."          

    def attack_engine(self, current_space):
        val = 0 
        s_group = encounter[current_space] 
        scene_group = s_group[1:len(s_group)]
        scene = random.choice(scene_group) 
        #current_scene = scene[1] 
        foe = foe_map[current_space]
        lucky = "    Luck favors you and the %s attack misses completely." % foe    
        ###While hero is alive, while foe is alive, if first time in, if subsequent times in.
        while Hit_Points["Hero"] > 0: 
            
            while Hit_Points[foe] > 0:
                roll = random.randint(0, 4)
                scene = random.choice(scene_group) 
                current_scene = scene[1]

                if val == 0:
                    incoming = s_group[0][0]
                    print format_text('stuff', incoming)
                
                    if roll != 1:
                        print self.defense_input(current_space, foe)                                                                                                                                                                      
                        val = 1    
                    elif roll == 1:
                        print format_text('stuff', lucky), self.defense_input(current_space, foe)
                        val = 1

                elif val == 1:

                    if roll == 1:
                        print lucky, self.defense_input(current_space, foe)
                        val = 1
                    elif roll != 1:
                        h_change = scene[0]
                        print format_text('stuff', current_scene), "Your health is now %s." % self.hero_health_change(h_change), self.defense_input(current_space, foe)
                        val = 1


            print "    Your foe perishes at your feet. At surviving, you are victorious."
            self.scene(current_space)
            break

        print "    With your last breath you scream \"Arturia!\" then you breath no more."
        exit(1)     

    def interactive_encounter(self, current_space):
        ###print intro scene, take input until exit scene triggered then pass to self.scene(current_space).
        #Merchant_Inp
        current_dict = encounter_directory[current_space]
        current_scenes = encounter[current_space]
        intro_scene = current_scenes[0]
        print format_text('self', intro_scene)
        value = 0
        counter = 0

        while value != 2:
            u_i = raw_input("> ")
            for key in current_dict:
                if key in u_i:
                    value = current_dict[key]
                    current_scene = current_scenes[value] 
                    print format_text('self', current_scene)
                elif key not in u_i:
                    counter += 1
                    if counter == len(current_dict):
                        print "I don't understand."
                    else:
                        continue    
        print format_text('self', scene[current_space])
        self.user_input(current_space)

    def passive_encounter(self, current_space):
        current_scenes = encounter[current_space]
        intro_scene = current_scenes[0][0]
        print format_text('self', intro_scene)    

    def poison_encounter(self, current_space):
        scene_set = encounter[current_space]
        intro, scene = scene_set[0][0], scene_set[random.randint(1, (len(scene_set) -1))][1]
        print format_text('self', intro)
        print format_text('self', scene)
   
    def memory_nymph(self, current_space):
        format_text('self', Memory_Nymphs_Scenes[0][0])
        scenes = Memory_Nymphs_Scenes[1], Memory_Nymphs_Scenes[2]
        scene = random.choice(scenes)
        item = scene[1]
        u_i = raw_input("> ")
        if "sit" in u_i or "yes" in u_i or "talk" in u_i:
            print format_text("self", scene[2])
            print del_from_bag("stuff", item)
            self.user_input(current_space)            
        elif "run" in u_i or "no" in u_i or "walk away" in u_i:
            print "    You put some distance between yourself and the mysterious creature. "
            #Move player one space to the left.
            current_space = 22
            self.scene(current_space)
        else:
            print "    You can tell that the creature doesn't understand you but it continues anyway." 
            print format_text("self", scene[2])  
            print del_from_bag("stuff", item)
            self.user_input(current_space)  

### When no attack is rolled            
    def user_input(self, current_space):
    ### Take input, if in dict pass to point, if not raise error.																																																																																																																																																																																																																																																							
        user = raw_input(">  ")
        good_value = 0
        for key in main_directory:
            for subkey in main_directory[key]:
                if subkey in user:
                    good_value = 1
                    self.point(subkey, current_space)
        if "help" in user:
            print help_func('self')
            self.user_input(current_space)
        if good_value == 0:
            print "    I'm afraid I didn't understand your command. Please try again."
            self.user_input(current_space)
		    
    def point(self, subkey, current_space):
    ### Find which dictionary input key exists in, pass to related method.    
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
        elif subkey == "gather":
            add_to_bag("self", current_space)    
        else:
            print "not here"

    def bag(self, current_space):
        pass        





	    
current_space = 5

go = Game(current_space)
go.encounter_roll(current_space)
