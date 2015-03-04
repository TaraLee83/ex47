###pull from attacks dict randomly, print desc of attack, use value to calculate hp loss. If hero dead end game, if hero lives pass.
from foe_hitpoints import RedDragon
import random
from library import Dragons

hero_hp = [65]

def dragon_attack(self, current_space):
    dragon_chooser = random.choice(Dragons)
    print dragon_chooser
    group = random.choice(dragon_chooser[1:5])
    pull_val = group[0:1] 
    pull_desc_a = group[1:2]
    pull_desc_b = group[2:3]
    intro = (", ".join(repr(e) for e in pull_desc_a))
    conclusion = (", ".join(repr(e) for e in pull_desc_b))
    roll = random.randint(0, 4)
    print intro
    if roll == 1:
        print "You're lucky!"		    
    elif roll != 1:
        print conclusion
        health = sum(hero_hp)
        change = sum(pull_val)
        new_val = health + change
        print "Your health went from %r to %r." % (health, new_val)
        del hero_hp[:]
        hero_hp.append(new_val)

        
        
def damage(self, current_space, dict, a, b):
    pass
    
    



current_space = 6    
go = dragon_attack('stuff', current_space)    