

directions = {'north':1,'south':2,'east':3,'west':4}

actions = {'run':1,'walk':2,'jog':3}

big_sucker = {0:directions,1:actions}

pretend_input = 'walk on'

for key in big_sucker:
    for subkey in big_sucker[key]:
        if subkey in pretend_input:
	    print subkey