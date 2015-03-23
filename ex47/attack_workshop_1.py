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
    print Hit_Points[gen_foe][foe]
    

  
def choose_attack(self, current_space):
    foe = encounter[current_space]
    chooser = random.choice(foe)
    return chooser          

def defense_input(self, foe):
    user = raw_input("> ")    
    
    if 'hit' in user:
        f_change = -10
        update_line = "Your foes health is now %s." % foe_health_change('self', foe, f_change)
        return update_line


    else:
         return "no hit"
      

def attack_engine(self, current_space):
    val = 0  
    chooser = choose_attack('self', current_space)
    group = random.choice(chooser[2:5])
    h_change = sum(group[0:1])
    #f_change = 
    lucky_line = "Luck favors you and the %s attack misses completely." % (str(chooser[0:1]).strip("[]")).strip("'")
    lucky = str(chooser[1:2]), lucky_line
    first_attack = str(chooser[1:2]), str(group[1:2])
    while hero_health('self') > 0:
        #foe_health = 
        foe = (str(chooser[0:1]).strip("[]")).strip("'")
        group = random.choice(chooser[2:5])
        subsequent_attacks = str(group[1:2])
        hero_update = "Your health is now %s." % hero_health_change('self', h_change)

        if foe_health > 0:
            roll = random.randint(0, 4)
            if roll != 1 and val == 0:   #should just update here
                print str(chooser[1:2]), defense_input('self', foe)
                val = 1
            elif roll != 1 and val == 1:
                print subsequent_attacks, hero_update, defense_input('self', foe)
                val = 1       
            elif roll == 1 and val == 0:
                print lucky, defense_input('self', foe)
                val = 1
            elif roll == 1 and val == 1:
                print lucky_line, defense_input('self', foe)
                val = 1

        else:
            print "Your foe perishes at your feet. At surviving, you are victorious."
            #self.scene()

       
    print "With your last breath you scream \"Arturia!\" then you breath no more."
    exit(1)            
 
current_space = 4 
f_change = -10

foe = 'red_dragon'
go = foe_health_change('stuff', current_space, foe, f_change)    