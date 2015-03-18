###pull from attacks dict randomly, print desc of attack, use value to calculate hp loss. If hero dead end game, if hero lives pass.
import random
from library import Dragons, Hit_Points, encounter
import textwrap



def hero_health(self):
    hero_hp = Hit_Points['Hero']
    return hero_hp
 
def hero_health_change(self, change):
    new = hero_health('self') + change
    Hit_Points = {'Hero': new}
    return new
  
#def attacker_health_change(self, change):
    
    
#def attack_engine(self, current_space):
#    while (hero_health('self') > 0) and (attacker_health > 0):
#        print "attacky stuff"

        #print "Your health is now %d" % hero_health_change('stuff', )
#        break


def choose_attack(self, current_space):
    foe = encounter[current_space]
    chooser = random.choice(foe)
    group = random.choice(chooser[2:5])
    val = sum(group[0:1])
    lucky = "%r But luck favors you and the attack misses completely." % str(chooser[0:1])
    attack = str(chooser[0:1]), str(group[1:2])
    roll = random.randint(0, 4)
    if roll == 1:
        return lucky
    elif roll != 1:
        return attack  
 

###The following two should be combined.
def health_change(self, val):
    hit = -20
    new_foe_hp = hit_foe(self, chooser, current_space) + hit
    print new_foe_hp

def foe_health(self, chooser, current_space):
    creature = (str(chooser[0:1]).strip("[]")).strip("'") 
    foes = encounter[current_space]
    current_health = Hit_Points[foes][creature]
    return current_health   



def foe_attack(self, current_space):
    now = chooser(self, inc_attacker, current_space)
    
    
    

current_space = 4 

go = choose_attack('stuff', current_space)    