### Meadow Mystic handling
from library import Meadow_Mystic

def meadow_mystic(self):
    user_input = raw_input("> ")

    if "parent" or "family" or "mom" or "dad" in user_input:
        print Meadow_Mystic[12]
    elif "talk" or "information" or "knowledge" or "tell" in user_input:
    	print Meadow_Mystic[9]
    elif "dragons" or "daughter" or "soul" or "how" in user_input:
        print Meadow_Mystic[10]
    else:
        print Meadow_Mystic[14]    

go = meadow_mystic('stuff')        