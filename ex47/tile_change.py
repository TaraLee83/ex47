import random

def tile_change(self):
   ###scramble current tile
   sec_1 = (1,2,3,7,8,9,13,14,15)
   current_space = random.choice(sec_1)
   print current_space


go = tile_change('stuff')  

