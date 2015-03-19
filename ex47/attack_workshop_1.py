###pull from attacks dict randomly, print desc of attack, use value to calculate hp loss. If hero dead end game, if hero lives pass.
import random
import textwrap
from sys import exit
from library import Dragons, Hit_Points, encounter



def hero_health(self):
    hero_hp = Hit_Points['Hero']
    return hero_hp
 
def hero_health_change(self, change):
    new = hero_health('self') + change
    for key, value in Hit_Points.items():
        Hit_Points["Hero"] = new
    return new
  
#def attacker_health_change(self, change):


def choose_attack(self, current_space):
    foe = encounter[current_space]
    chooser = random.choice(foe)
    return chooser          


def attack_engine(self, current_space):
    val = 0  
    chooser = choose_attack('self', current_space)
    group = random.choice(chooser[2:5])
    h_change = -10
    f_change = -10
    lucky_line = "But luck favors you and the attack misses completely."
    lucky = lucky_line, str(chooser[1:2])
    first_attack = str(chooser[1:2]), str(group[1:2])

    while hero_health('self') > 0:
        hero_update = "Your health is now %s." % hero_health_change('self', h_change)
        #foe_update = foe_health_change('self', f_change)
        group = random.choice(chooser[2:5])
        subsequent_attacks = str(group[1:2])

        if foe_health > 0:

            roll = random.randint(0, 4)
            if roll != 1 and val == 0:
                print first_attack, hero_update
                val = 1
            elif roll != 1 and val == 1:
                print subsequent_attacks, hero_update 
                val = 1       
            elif roll == 1 and val == 0:
                print lucky
                val = 1
            elif roll == 1 and val == 1:
                print lucky_line


        else:
            print "Your foe perishes at your feet. At surviving, you are victorious."
            #self.scene()

    print "With your last breath you scream \"Arturia!\" then you breath no more."
    exit(1)            
            
    #only print if health above zero. Exit game if health 0.                          
 

###The following two should be combined.
def foe_health_change(self, f_change):
    new_foe_hp = hit_foe(self, chooser, current_space) + hit
    print new_foe_hp

def foe_health(self, chooser, current_space):
    creature = (str(chooser[0:1]).strip("[]")).strip("'") 
    foes = encounter[current_space]
    current_health = Hit_Points[foes][creature]
    return current_health   


    
    

current_space = 4 
change = -20


go = tester('stuff', current_space)    