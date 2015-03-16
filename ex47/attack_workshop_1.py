###pull from attacks dict randomly, print desc of attack, use value to calculate hp loss. If hero dead end game, if hero lives pass.
import random
from library import Dragons, Hit_Points
import textwrap
from graph import encounter


def chooser(self, inc_attacker, current_space):
    chooser = random.choice(inc_attacker)
    group = random.choice(chooser[2:5])
    #print group
    intro = str(chooser[0:1])
    #val = sum(group[0:1])
    #attack_desc = str(group[1:2])
    #roll = random.randint(0, 4)
    #lucky_line = "But luck favors you and the attack misses completely."
    #missed_attack = intro, lucky_line
    #successful_attack = intro, attack_desc
    #return missed_attack
    #return successful_attack
    creature = 

def hero_health_change(self, creature, val):
    



###The following two should be combined.
def health_change(self, creature):
    hit = -20
    new_foe_hp = hit_foe(self, chooser, current_space) + hit
    print new_foe_hp

def hit_foe(self, chooser, current_space):
    creature = (str(chooser[0:1]).strip("[]")).strip("'") 
    foes = encounter[current_space]
    current_health = Hit_Points[foes][creature]
    return current_health   



def foe_attack(self, current_space):
    now = chooser(self, inc_attacker, current_space)
    
    
    

inc_attacker = Dragons
current_space = 6 

go = chooser('stuff', inc_attacker, current_space)    