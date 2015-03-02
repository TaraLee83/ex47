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

Red = {"Red claw attack": -20,
       "Red tail_swipe": -20,
       "Red fire_breath": -40,
       "Red finisher": -50,
      }
Green = {"Green claw attack": -16,
	 "Green tail_swipe": -16,
	 "Green fire_breath": -32,
	 "Green finisher": -40,
        }
Gold = {"Gold claws": -14,
	"Gold tail_swipe": -14,
        "Gold fire_breath": -28,
        "Gold finisher": -35,
       }
Dragons = {0: Red, 1: Green,
	   2: Gold
	  }

def dragon_attack(self, current_space):
    a = random.choice(Dragons.keys())
    x = random.randint(1, 2)
    b = random.choice(Dragons[a].keys())
    if x == 1:
        print b
    elif x != 0:
        print "Luck favors you and the Dragons' rage misses you."
        

    
 


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
go = dragon_attack('stuff', current_space)    