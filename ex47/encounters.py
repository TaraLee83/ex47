#encounter dictionaries
import random

def roll(self):
    x = random.randint(1, 5) 
    y = 4
    if x == y:
        print x
        print "encounter happens"
    else:
        print x,"no"
        


encounter = {}

go = encounter('stuff')
    
    
Meadow = {
	 }

Dragonlands = {'red': ['4', '5', '6', '10', '11', '12', '16', '17', '18'],
	       'green': ['4', '5', '6', '10', '11', '12', '16', '17', '18'],
	       'gold': ['4', '5', '6', '10', '11', '12', '16', '17', '18'],
               'his_tears': ['16', '10']
	      }

Desert = {
         }

Forest = {
	 }

charms = {'godswear': ['red', 'green', 'gold']
         }

attacks = {'red': ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
           'green': ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
           'gold': ['fire_breath', 'claws', 'tail_swipe', 'finisher'],
           'his_tears': ['drown', 'sorrow']
          }