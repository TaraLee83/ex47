###pull from attacks dict randomly, print desc of attack, use value to calculate hp loss. If hero dead end game, if hero lives pass.
import random
import textwrap
from sys import exit
from library import Dragons, Hit_Points, encounter
from graph import foe_map



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
    chooser = choose_attack('self', current_space)
    lucky_line = "Luck favors you and the %s attack misses completely." % (str(chooser[0:1]).strip("[]")).strip("'")
    lucky = str(chooser[1:2]), lucky_line
    
    ###While hero is alive, while foe is alive, if first time in, if subsequent times in.
    while hero_health('self') > 0: 
        foe = (str(chooser[0:1]).strip("[]")).strip("'")
        
        while Hit_Points[gen_foe][foe] > 0:
            roll = random.randint(0, 4)
            chosen_attack = random.choice(chooser[2:5])

            if val == 0:
                print str(chooser[1:2])
                
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
 
current_space = 4 

go = attack_engine('stuff', current_space)    