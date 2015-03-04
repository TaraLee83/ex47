###pull from attacks dict randomly, print desc of attack, use value to calculate hp loss. If hero dead end game, if hero lives pass.
from foe_hitpoints import RedDragon
import random

attack = {0: ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
          1: ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
          2: ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
          3: ['drown', 'sorrow']
          }

Dragon1 = {5: "You drink a minor potion of 'protect against Dragon.'"}
Dragon2 = {15: "You don the fireopal encased in glass."}

Charms = {0: [Dragon1, Dragon2]}


Dragons = [['Red', [-20, "Red claw attack"], [-20, "Red tail_swipe"],
           [-40, "Red fire_breath"], [-50, "Red finisher"]],
           ['Green', [-16, "Green claw attack"], [-16, "Green tail_swipe"],
           [-32, "Green fire_breath"], [-40, "Green finisher"]],
	   ['Gold', [-14, "Gold claws"], [-14, "Gold tail_swipe"],
           [-28, "Gold fire_breath"],[-35, "Gold finisher"]]
	  ]

a = random.choice(Dragons)
print a
b = random.choice(a[1:5])
print b

def dragon_attack(self, current_space):
    dict = Dragons
    a = random.choice(Dragons.keys())
    x = random.randint(1, 2)
    b = random.choice(Dragons[a].items())
    if x == 1:
        go = damage(self, current_space, dict, a, b)		    
    elif x != 0:
        print "Luck favors you and the Dragons' rage misses you."
        
        
def damage(self, current_space, dict, a, b):
    pass
    
    

    
 


def dragon_chooser(self, current_space):
    dragon = random.randint(0, 2)
    if dragon == 0:
        red_dragon('stuff', current_space)
    elif dragon == 1:
        green_dragon('stuff', current_space)
    elif dragon == 2:
        gold_dragon('stuff', current_space)
        
def red_dragon(self, current_space):
    attack = ("go", "stay", "inbetween")
    print random.choice(attack)
    
def green_dragon(self, current_space):
    print "green_dragon"
    attack = ("go", "stay", "inbetween")
    print random.choice(attack)
    
def gold_dragon(self, current_space):
    print "gold_dragon"
    attack = ("go", "stay", "inbetween")
    print random.choice(attack)
    

current_space = 6    
#Sgo = dragon_attack('stuff', current_space)    